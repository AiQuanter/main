import logging
from sklearn.feature_extraction.text import TfidfVectorizer
from typing import List, Any
import joblib

logger = logging.getLogger(__name__)

class FeatureExtractor:
    def __init__(self, max_features: int = 10000, ngram_range: tuple = (1, 2)):
        """
        Initializes the feature extractor with the specified parameters.
        """
        self.vectorizer = TfidfVectorizer(
            max_features=max_features,
            ngram_range=ngram_range,
            stop_words='english',
            sublinear_tf=True
        )
        logger.info("FeatureExtractor initialized with TfidfVectorizer")

    def fit_transform(self, documents: List[str]) -> Any:
        """
        Extracts and fits TF-IDF features from the provided documents.
        """
        try:
            features = self.vectorizer.fit_transform(documents)
            logger.debug("Features extracted and vectorizer fitted.")
            return features
        except Exception as e:
            logger.error(f"Error in fit_transform: {e}")
            return None

    def transform(self, documents: List[str]) -> Any:
        """
        Transforms new documents using the fitted vectorizer.
        """
        try:
            features = self.vectorizer.transform(documents)
            logger.debug("New data transformed using existing vectorizer.")
            return features
        except Exception as e:
            logger.error(f"Error in transform: {e}")
            return None

    def save_vectorizer(self, filepath: str) -> None:
        """
        Saves the fitted vectorizer to a file.
        """
        try:
            joblib.dump(self.vectorizer, filepath)
            logger.info(f"Vectorizer saved to {filepath}")
        except Exception as e:
            logger.error(f"Error saving vectorizer: {e}")

    def load_vectorizer(self, filepath: str) -> None:
        """
        Loads the fitted vectorizer from a file.
        """
        try:
            self.vectorizer = joblib.load(filepath)
            logger.info(f"Vectorizer loaded from {filepath}")
        except Exception as e:
            logger.error(f"Error loading vectorizer: {e}")
