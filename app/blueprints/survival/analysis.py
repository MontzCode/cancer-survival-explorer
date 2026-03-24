import pandas as pd
from lifelines import KaplanMeierFitter
import plotly.graph_objects as go
import plotly.io as pio

DATA_PATH = r'C:\Users\CCLeyton\Documents\cancer_survival_app\app\data\BreastCancerMETABRIC.csv'

def load_data():
    df = pd.read_csv(DATA_PATH)
    df = df.dropna(subset=['Overall Survival (Months)', 'Overall Survival Status'])
    df['deceased'] = (df['Overall Survival Status'] == 'Deceased').astype(int)
    return df

def survival_by_stage():
    df = load_data()
    df = df.dropna(subset=['Tumor Stage'])
    
    kmf = KaplanMeierFitter()
    fig = go.Figure()

    for stage in sorted(df['Tumor Stage'].unique()):
        mask = df['Tumor Stage'] == stage
        kmf.fit(
            durations=df.loc[mask, 'Overall Survival (Months)'],
            event_observed=df.loc[mask, 'deceased'],
            label=f'Stage {int(stage)}'
        )
        sf = kmf.survival_function_
        fig.add_trace(go.Scatter(
            x=sf.index,
            y=sf.iloc[:, 0],
            mode='lines',
            name=f'Stage {int(stage)}'
        ))

    fig.update_layout(
        title='Overall Survival by Tumour Stage',
        xaxis_title='Time (Months)',
        yaxis_title='Survival Probability',
        hovermode='x unified',
        plot_bgcolor='white',
        paper_bgcolor='white'
    )

    return pio.to_html(fig, full_html=False)