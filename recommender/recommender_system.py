import logging
from typing import List, Dict

logger = logging.getLogger(__name__)

class RecommenderSystem:
    def __init__(self):
        """
        Initializes the RecommenderSystem.
        """
        logger.info("RecommenderSystem initialized")

    def generate_recommendations(self, trends: List[str], user_preferences: Dict[str, List[str]]) -> List[str]:
        """
        Generates recommendations for meme coin creation based on trends and user preferences.
        """
        try:
            recommendations = []
            for trend in trends:
                for interest in user_preferences.get("interests", []):
                    if interest.lower() in trend.lower():
                        recommendations.append(f"Create a meme coin based on {trend}")
                        break
            logger.info(f"Generated {len(recommendations)} recommendations")
            return recommendations
        except Exception as e:
            logger.error(f"Error generating recommendations: {e}")
            return []
