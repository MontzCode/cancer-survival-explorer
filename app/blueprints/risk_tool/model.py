import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler

DATA_PATH = r'C:\Users\CCLeyton\Documents\cancer_survival_app\app\data\BreastCancerMETABRIC.csv'

FEATURES = [
    'Age at Diagnosis',
    'Tumor Size',
    'Tumor Stage',
    'Neoplasm Histologic Grade',
    'Nottingham prognostic index',
    'Lymph nodes examined positive',
    'Mutation Count'
]

def train_model():
    df = pd.read_csv(DATA_PATH)
    df = df.dropna(subset=['Overall Survival Status'])
    df['deceased'] = (df['Overall Survival Status'] == 'Deceased').astype(int)
    df_model = df[FEATURES + ['deceased']].dropna()

    X = df_model[FEATURES]
    y = df_model['deceased']

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)

    return model

def predict_survival(age, tumor_size, tumor_stage, grade, npi, lymph_nodes, mutation_count):
    model = train_model()

    input_data = pd.DataFrame([{
        'Age at Diagnosis': age,
        'Tumor Size': tumor_size,
        'Tumor Stage': tumor_stage,
        'Neoplasm Histologic Grade': grade,
        'Nottingham prognostic index': npi,
        'Lymph nodes examined positive': lymph_nodes,
        'Mutation Count': mutation_count
    }])

    prob = model.predict_proba(input_data)[0]
    survival_prob = round(prob[0] * 100, 1)
    deceased_prob = round(prob[1] * 100, 1)

    return survival_prob, deceased_prob