from zenml import pipeline
from steps.ingest_data import ingest_df
from steps.clean_data import clean_df
from steps.model_train import train_model
from steps.evaluation import evaluation_model

@pipeline
def train_pipeline(data_path:str):
    df = ingest_df(data_path)
    X_train , X_test , Y_train , Y_test = clean_df(df)
    model = train_model(X_train , X_test , Y_train , Y_test )
    r2_score  , rmse = evaluation_model(model , X_test , Y_test)
    







