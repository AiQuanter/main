import logging
from typing import List
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import NMF
from sklearn.preprocessing import normalize

logger = logging.getLogger(__name__)

class TrendDetector:
    def __init__(self, n_topics: int = 10, n_top_words: int = 10):
        """
        Initializes the TrendDetector with the specified number of topics and top words per topic.
        """
        self.n_topics = n_topics
        self.n_top_words = n_top_words
        self.vectorizer = TfidfVectorizer(max_df=0.95, min_df=5, stop_words='english')
        self.model = NMF(n_components=self.n_topics, random_state=42)

    def detect_trends(self, documents: List[str]) -> List[str]:
        """
        Detects trends using NMF for topic modeling.
        """
        try:
            tfidf = self.vectorizer.fit_transform(documents)
            W = self.model.fit_transform(tfidf)
            H = self.model.components_
            feature_names = self.vectorizer.get_feature_names_out()
            
            trends = []
            for topic_idx, topic in enumerate(H):
                top_features = [feature_names[i] for i in topic.argsort()[:-self.n_top_words - 1:-1]]
                trends.append(f"Trend {topic_idx + 1}: " + ", ".join(top_features))
            logger.info("Trends detected successfully")
            return trends
        except Exception as e:
            logger.error(f"Error in trend detection: {e}")
            return []
