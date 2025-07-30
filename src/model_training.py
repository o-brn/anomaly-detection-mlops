import pandas as pd
from sklearn.ensemble import IsolationForest


def train_anomaly_detector(data: pd.DataFrame) -> IsolationForest:
    """
    Treina um modelo IsolationForest nos dados fornecidos.
    """
    model = IsolationForest(contamination="auto", random_state=42)
    model.fit(data[["value"]])
    return model


def predict_anomalies(model: IsolationForest, data: pd.DataFrame) -> pd.DataFrame:
    """
    Usa um modelo treinado para prever anomalias.
    """
    data["anomaly"] = model.predict(data[["value"]])
    return data
