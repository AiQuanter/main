import logging
from typing import Dict, List

logger = logging.getLogger(__name__)

class UserProfile:
    def __init__(self, user_id: str):
        """
        Initializes the UserProfile with the provided user ID and loads preferences.
        """
        self.user_id = user_id
        self.preferences = self.load_preferences()

    def load_preferences(self) -> Dict[str, List[str]]:
        """
        Loads the user's preferences from a data source (e.g., database, file).
        For demonstration, it uses static data.
        """
        try:
            # In a real-world scenario, this method would fetch preferences from a database or other data source
            preferences = {
                "interests": ["crypto", "memes", "AI", "gaming", "NFTs"]
            }
            logger.info(f"Preferences loaded for user {self.user_id}")
            return preferences
        except Exception as e:
            logger.error(f"Error loading preferences for user {self.user_id}: {e}")
            return {}
