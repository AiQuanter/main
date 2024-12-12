import logging
from transformers import pipeline
from typing import List

logger = logging.getLogger(__name__)

class SentimentAnalysis:
    def __init__(self, model_name: str = "nlptown/bert-base-multilingual-uncased-sentiment"):
        """
        Initialize sentiment analysis pipeline with the specified model.
        """
        try:
            self.sentiment_pipeline = pipeline("sentiment-analysis", model=model_name)
            logger.info(f"SentimentAnalysis initialized with model {model_name}")
        except Exception as e:
            logger.error(f"Failed to load sentiment model: {e}")
            raise e

    def _process_sentiment(self, result: dict) -> float:
        """
        Processes individual sentiment result into a consistent score.
        """
        label = result['label']
        score = result['score']
        if label.lower() in ['1 star', '2 stars']:
            return -score
        elif label.lower() in ['4 stars', '5 stars']:
            return score
        return 0.0

    def analyze_sentiment(self, texts: List[str]) -> List[float]:
        """
        Analyzes sentiment for a list of texts.
        """
        try:
            results = self.sentiment_pipeline(texts)
            sentiments = [self._process_sentiment(result) for result in results]
            logger.info(f"Sentiment analysis completed for {len(texts)} texts.")
            return sentiments
        except Exception as e:
            logger.error(f"Error during sentiment analysis: {e}")
            return []
