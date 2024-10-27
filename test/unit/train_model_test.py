import math

from src.training.train_model import train_random_forest


def test_train_xgboost():
    actual = train_random_forest(n_estimators=100)
    # breakpoint()
    assert math.isclose(actual, 6.909231565384943, rel_tol=1e-4)
