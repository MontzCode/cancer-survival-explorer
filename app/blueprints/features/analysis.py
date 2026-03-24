import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import plotly.graph_objects as go
import plotly.io as pio

DATA_PATH = r'C:\Users\CCLeyton\Documents\cancer_survival_app\app\data\BreastCancerMETABRIC.csv'

def load_data():
    df = pd.read_csv(DATA_PATH)
    df = df.dropna(subset=['Overall Survival Status'])
    df['deceased'] = (df['Overall Survival Status'] == 'Deceased').astype(int)
    return df

def feature_importance_chart():
    df = load_data()

    features = [
        'Age at Diagnosis',
        'Tumor Size',
        'Tumor Stage',
        'Neoplasm Histologic Grade',
        'Nottingham prognostic index',
        'Lymph nodes examined positive',
        'Mutation Count'
    ]

    df_model = df[features + ['deceased']].dropna()

    X = df_model[features]
    y = df_model['deceased']

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)

    importance_df = pd.DataFrame({
        'Feature': features,
        'Importance': model.feature_importances_
    }).sort_values('Importance', ascending=True)

    fig = go.Figure(go.Bar(
        x=importance_df['Importance'],
        y=importance_df['Feature'],
        orientation='h',
        marker_color='#2196F3'
    ))

    fig.update_layout(
        title='Clinical Variables by Predictive Importance',
        xaxis_title='Feature Importance Score',
        yaxis_title='',
        plot_bgcolor='white',
        paper_bgcolor='white',
        hovermode='y unified'
    )

    return pio.to_html(fig, full_html=False)