import pytest
from trend_analysis.trend_detector import TrendDetector

@pytest.fixture
def sample_documents():
    """
    Fixture to generate mock documents for trend detection.
    """
    return [
        "Bitcoin is surging to new highs",
        "Meme coins are becoming popular",
        "AI and cryptocurrency are the future of finance"
    ]

def test_trend_detector(sample_documents):
    """
    Test that the trend detector identifies topics correctly.
    """
    trend_detector = TrendDetector(n_topics=2, n_top_words=3)
    trends = trend_detector.detect_trends(sample_documents)
    
    assert len(trends) == 2, "There should be two detected trends"
    assert "Bitcoin" in trends[0], "First trend should mention Bitcoin"
    assert "Meme coins" in trends[1], "Second trend should mention Meme coins"

