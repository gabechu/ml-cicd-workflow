import math
from unittest.mock import Mock, patch

from src.training.train_model import train_random_forest


@patch("src.training.train_model._persist_model")
def test_train_xgboost(mock_registry):
    mock_registry = Mock()
    actual = train_random_forest(
        n_estimators=100, max_depth=3, min_samples_split=2, min_samples_leaf=1, registry=mock_registry
    )
    assert math.isclose(actual, 12.69298603704, rel_tol=1e-4)
