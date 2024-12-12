import pytest
import numpy as np
from meme_predictor.meme_model import MemeModel

@pytest.fixture
def sample_data():
    """
    Fixture to generate random sample data for model testing.
    """
    X = np.random.rand(100, 10)  # Mock feature data
    y = np.random.randint(0, 2, size=100)  # Random binary target data
    return X, y

def test_meme_model_training(sample_data):
    """
    Test that the meme model can be trained successfully.
    """
    X, y = sample_data
    model = MemeModel(model_path="test_meme_model.joblib")
    model.train(X, y)
    assert model.model is not None, "Model should be trained and not None"

def test_meme_model_prediction(sample_data):
    """
    Test that the meme model can generate predictions.
    """
    X, y = sample_data
    model = MemeModel(model_path="test_meme_model.joblib")
    model.train(X, y)
    predictions = model.predict(X)
    assert predictions is not None, "Predictions should not be None"
    assert len(predictions) == X.shape[0], "Predictions should match the number of samples"
    
def test_model_save_load():
    """
    Test saving and loading of the meme model.
    """
    model = MemeModel(model_path="test_model.joblib")
    model.save_model()  # Save the model
    new_model = MemeModel(model_path="test_model.joblib")
    new_model.load_model()  # Load the model
    assert new_model.model is not None, "Model should be loaded successfully"
