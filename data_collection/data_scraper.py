import asyncio
import aiohttp
import logging
from bs4 import BeautifulSoup
from typing import List

logger = logging.getLogger(__name__)

class DataScraper:
    def __init__(self, urls: List[str]):
        """
        Initializes the scraper with a list of URLs.
        """
        self.urls = urls

    async def fetch(self, session: aiohttp.ClientSession, url: str) -> str:
        """
        Asynchronously fetches data from a given URL.
        """
        try:
            async with session.get(url, timeout=10) as response:
                response.raise_for_status()
                text = await response.text()
                logger.debug(f"Fetched data from {url}")
                return text
        except Exception as e:
            logger.error(f"Error fetching data from {url}: {e}")
            return ""

    async def scrape_all(self) -> List[str]:
        """
        Asynchronously scrapes data from all the URLs.
        """
        async with aiohttp.ClientSession() as session:
            tasks = [self.fetch(session, url) for url in self.urls]
            html_contents = await asyncio.gather(*tasks)
            return [BeautifulSoup(html, 'html.parser').get_text() for html in html_contents if html]
