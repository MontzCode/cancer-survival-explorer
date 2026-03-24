import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-key-change-in-production'
    DATA_PATH = os.path.join(os.path.dirname(__file__), 'app', 'data', 'Breast_Cancer_METABRIC.csv')