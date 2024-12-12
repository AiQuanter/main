import asyncio
import logging
from config.settings import settings
from data_collection.api_integrations import APIIntegrations
from trend_analysis.trend_detector import TrendDetector
from trend_analysis.sentiment_analysis import SentimentAnalysis
from meme_predictor.feature_extractor import FeatureExtractor
from meme_predictor.meme_model import MemeModel
from recommender.recommender_system import RecommenderSystem
from recommender.user_profile import UserProfile
from blockchain_integration.solana_connector import SolanaConnector
from error_handler import handle_error

# Setting up logging
logging.basicConfig(
    level=settings.log_level,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

async def main():
    try:
        # Initialize components
        api = APIIntegrations(
            twitter_bearer_token=settings.twitter_bearer_token,
            reddit_client_id=settings.reddit_client_id,
            reddit_client_secret=settings.reddit_client_secret
        )
        trend_detector = TrendDetector()
        sentiment_analyzer = SentimentAnalysis()
        feature_extractor = FeatureExtractor()
        meme_model = MemeModel()
        recommender = RecommenderSystem()
        user_profile = UserProfile(user_id="user123")
        solana = SolanaConnector(rpc_url=settings.solana_rpc_url)

        # Collect data from APIs
        documents = await api.gather_api_data(query="meme", subreddit="crypto")

        # Detect trends
        trends = trend_detector.detect_trends(documents)

        # Sentiment analysis
        sentiments = sentiment_analyzer.analyze_sentiment(documents)

        # Feature extraction
        features = feature_extractor.fit_transform(documents)

        # Train the model (using synthetic labels for demo)
        import numpy as np
        y = np.random.randint(0, 2, size=features.shape[0])
        meme_model.train(features, y)

        # Meme success prediction
        predictions = meme_model.predict(features)

        # Generate recommendations
        recommendations = recommender.generate_recommendations(trends, user_profile.preferences)

        # Blockchain interaction example
        wallet_address = "YourWalletAddressHere"
        balance = await solana.get_balance(wallet_address=wallet_address)
        logger.info(f"Wallet Balance for {wallet_address}: {balance} lamports")

        # Print recommendations
        for rec in recommendations:
            logger.info(f"Recommendation: {rec}")

        # Close blockchain connections
        await solana.close()

    except Exception as e:
        handle_error(e)

if __name__ == "__main__":
    asyncio.run(main())
