# Cancer Survival Explorer

An interactive web application for exploring breast cancer survival data from the METABRIC dataset, covering 2,509 patients across 34 clinical variables.

Built with Flask, Plotly, scikit-learn and lifelines.

## Features

- **Survival Analysis** - Interactive Kaplan-Meier survival curves stratified by tumour stage
- **Feature Importance** - Random Forest model identifying which clinical variables best predict survival
- **Risk Stratification Tool** - Enter patient characteristics and get a survival probability estimate

## Tech Stack

- Python 3.11
- Flask
- Plotly
- scikit-learn
- lifelines
- pandas

## Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/MontzCode/cancer-survival-explorer.git
cd cancer-survival-explorer
```

### 2. Create a conda environment
```bash
conda create -n cancer_survival python=3.11
conda activate cancer_survival
pip install -r requirements.txt
```

### 3. Add the dataset

Download the METABRIC breast cancer dataset from Kaggle and place the CSV file at:
```
app/data/BreastCancerMETABRIC.csv
```

### 4. Run the app
```bash
python run.py
```

Then open `http://127.0.0.1:5000` in your browser.

## Dataset

METABRIC (Molecular Taxonomy of Breast Cancer International Consortium) clinical dataset covering 2,509 breast cancer patients. Available on Kaggle.

## Disclaimer

This tool is for educational and portfolio purposes only. It is not intended for clinical use.