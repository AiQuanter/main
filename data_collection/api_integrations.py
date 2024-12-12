import logging
import aiohttp
import asyncio
from typing import Any, Dict, List

logger = logging.getLogger(__name__)

class APIIntegrations:
    def __init__(self, twitter_bearer_token: str, reddit_client_id: str, reddit_client_secret: str):
        """
        Initializes APIIntegrations with Twitter and Reddit credentials.
        """
        self.twitter_bearer_token = twitter_bearer_token
        self.reddit_client_id = reddit_client_id
        self.reddit_client_secret = reddit_client_secret

    async def _fetch_data(self, session: aiohttp.ClientSession, url: str, headers: Dict[str, str], params: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generic method to fetch data from any given API endpoint.
        """
        try:
            async with session.get(url, headers=headers, params=params) as response:
                response.raise_for_status()
                data = await response.json()
                return data
        except aiohttp.ClientError as e:
            logger.error(f"API request failed with error: {e}, URL: {url}")
            return {}

    async def fetch_twitter_data(self, query: str, max_results: int = 100) -> Dict[str, Any]:
        """
        Fetches data from Twitter using their API.
        """
        url = "https://api.twitter.com/2/tweets/search/recent"
        headers = {
            "Authorization": f"Bearer {self.twitter_bearer_token}"
        }
        params = {
            "query": query,
            "max_results": max_results,
            "tweet.fields": "created_at,public_metrics"
        }
        async with aiohttp.ClientSession() as session:
            return await self._fetch_data(session, url, headers, params)

    async def fetch_reddit_data(self, subreddit: str, limit: int = 100) -> Dict[str, Any]:
        """
        Fetches data from Reddit using their API.
        """
        url = f"https://www.reddit.com/r/{subreddit}/new.json"
        headers = {
            "User-Agent": "QuanterAI/0.1"
        }
        params = {"limit": limit}
        async with aiohttp.ClientSession() as session:
            return await self._fetch_data(session, url, headers, params)

    async def gather_api_data(self, query: str, subreddit: str) -> List[str]:
        """
        Collects data from Twitter and Reddit asynchronously.
        """
        twitter_task = self.fetch_twitter_data(query)
        reddit_task = self.fetch_reddit_data(subreddit)
        twitter_data, reddit_data = await asyncio.gather(twitter_task, reddit_task)
        
        documents = []
        if 'data' in twitter_data:
            documents += [tweet['text'] for tweet in twitter_data['data']]
        if 'data' in reddit_data:
            documents += [post['data']['title'] for post in reddit_data['data']['children']]
        
        logger.debug(f"Collected {len(documents)} documents from APIs.")
        return documents
