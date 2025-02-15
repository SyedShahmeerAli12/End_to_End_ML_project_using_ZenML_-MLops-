import logging
import pandas as pd
from zenml import step

class IngestData:
    def __init__(self , data_path : str):
        self.data_path = data_path
        pass
    def get_data(self):
        logging.info(f"ingesting Data from {self.data_path}")
        return pd.read_csv(self.data_path)