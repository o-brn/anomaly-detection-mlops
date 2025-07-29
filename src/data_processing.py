import pandas as pd

def load_and_preprocess_data(file_path: str) -> pd.DataFrame:
    """
    Carrega os dados de um arquivo CSV, converte o timestamp e o define como índice.
    """
    df = pd.read_csv(file_path)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df.set_index('timestamp', inplace=True)
  