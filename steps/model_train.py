import logging
import pandas as pd
from src.model_dev import LinearRegressionModel
from sklearn.base import RegressorMixin
from zenml import step
from zenml.client import Client
from .config import ModelNameConfig

# experiment_tracker = Client().active_stack.experiment_tracker

@step
def train_model(
    x_train: pd.DataFrame,
    x_test: pd.DataFrame,
    y_train: pd.Series,
    y_test: pd.Series,
    config: ModelNameConfig,
) -> RegressorMixin:
    """
    Trains a regression model based on the given configuration.

    Args:
        x_train (pd.DataFrame): Training feature set.
        x_test (pd.DataFrame): Test feature set.
        y_train (pd.Series): Training target values.
        y_test (pd.Series): Test target values.
        config (ModelNameConfig): Configuration object containing model details.

    Returns:
        RegressorMixin: Trained regression model.
    """
    try:
        if config.model_name == "LinearRegression":
            model = LinearRegressionModel()
            trained_model = model.train(x_train, y_train)
            return trained_model
        else:
            raise ValueError(f"Model '{config.model_name}' is not supported.")
    except Exception as e:
        logging.exception("Error in training model")
        raise
