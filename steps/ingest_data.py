import logging
import pandas as pd
from zenml import step

class IngestData:
    def __init__(self , data_path : str):
        self.data_path = data_path
    def get_data(self):
        logging.info(f"ingesting Data from {self.data_path}")
        return pd.read_csv(self.data_path)
    

@step
def ingest_df(data_path : str) -> pd.DataFrame:
    try:
        Ingest_Data = IngestData(data_path)
        df = Ingest_Data.get_data()
        return df
    except Exception as e:
        logging.error("error while ingestind data" , e)
        raise e
     

