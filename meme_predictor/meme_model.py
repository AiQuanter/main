import logging
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from xgboost import XGBClassifier
import joblib
from typing import Any

logger = logging.getLogger(__name__)

class MemeModel:
    def __init__(self, model_path: str = "models/meme_model.joblib"):
        """
        Initializes the meme prediction model with specified parameters.
        """
        self.model = XGBClassifier(
            n_estimators=300,
            learning_rate=0.05,
            max_depth=12,
            subsample=0.7,
            colsample_bytree=0.7,
            objective='binary:logistic',
            eval_metric='logloss',
            use_label_encoder=False
        )
        self.model_path = model_path
        logger.info("MemeModel initialized with XGBoost classifier")

    def train(self, X: Any, y: Any) -> None:
        """
        Trains the meme prediction model.
        """
        try:
            X_train, X_val, y_train, y_val = train_test_split(
                X, y, test_size=0.2, random_state=42, stratify=y
            )
            self.model.fit(
                X_train, y_train,
                early_stopping_rounds=20,
                eval_set=[(X_val, y_val)],
                verbose=True
            )
            predictions = self.model.predict(X_val)
            report = classification_report(y_val, predictions)
            logger.info(f"Training completed successfully\n{report}")
        except Exception as e:
            logger.error(f"Error training meme prediction model: {e}")

    def predict(self, X: Any) -> Any:
        """
        Makes predictions about meme success with probability scores.
        """
        try:
            predictions = self.model.predict_proba(X)[:, 1]
            logger.info("Meme prediction completed successfully")
            return predictions
        except Exception as e:
            logger.error(f"Error in meme prediction: {e}")
            return None

    def save_model(self) -> None:
        """
        Saves the trained model to a file.
        """
        try:
            joblib.dump(self.model, self.model_path)
            logger.info(f"Model saved to {self.model_path}")
        except Exception as e:
            logger.error(f"Error saving model: {e}")

    def load_model(self) -> None:
        """
        Loads a trained model from a file.
        """
        try:
            self.model = joblib.load(self.model_path)
            logger.info(f"Model loaded from {self.model_path}")
        except Exception as e:
            logger.error(f"Error loading model: {e}")
