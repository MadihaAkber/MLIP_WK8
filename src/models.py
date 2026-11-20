from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor

def get_model(name, params=None):
    params = params or {}

    # Remove unsupported configuration keys
    params = {k: v for k, v in params.items() if k != "type"}

    if name == "LinearRegression":
        return LinearRegression(**params)

    elif name == "RandomForest":
        return RandomForestRegressor(**params)

    elif name == "XGBoost":
        return XGBRegressor(**params)

    else:
        raise ValueError(f"Unknown model: {name}")