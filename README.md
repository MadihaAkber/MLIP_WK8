# 🏠 California House Price Prediction | End-to-End Machine Learning

## Project Overview
An end-to-end machine learning project developed as part of my MSc Applied Artificial Intelligence at the University of Westminster.

This project predicts median housing values in California using machine learning, with an interactive Streamlit application and a FastAPI prediction endpoint.

## Machine Learning Models
Three regression algorithms were trained and evaluated:

| Model | R² Score | RMSE |
|---|---:|---:|
| Linear Regression | 0.5758 | 0.7456 |
| Random Forest | 0.7939 | 0.5197 |
| XGBoost | 0.8456 | 0.4498 |

**Best Model: XGBoost (R² = 0.8456)**

RMSE is reported in units of $100,000.

## Technologies Used
- Python
- Pandas
- Scikit-learn
- XGBoost
- MLflow
- FastAPI
- Streamlit
- Joblib
- Git and GitHub

## Project Workflow
1. Load the California Housing dataset.
2. Split data into training and testing sets.
3. Train three regression models.
4. Evaluate model performance using R² and RMSE.
5. Track experiments using MLflow.
6. Save the best-performing model.
7. Create a prediction API using FastAPI.
8. Develop an interactive website using Streamlit.

## Running the Project

Install dependencies:

```bash
pip install -r requirements.txt
```

Train the models:

```bash
python -m src.train
```

Launch the FastAPI application:

```bash
uvicorn app.api:app --reload
```

Launch the Streamlit website:

```bash
streamlit run app/streamlit_app.py
```

## Key Skills Demonstrated
- Regression modelling and model comparison
- Model evaluation and selection
- ML experiment tracking
- Model serialization
- REST API development
- Interactive application development
- End-to-end machine learning workflows

## Limitations
The model predicts median housing values at the neighbourhood level, not individual property sale prices. Predictions are estimates and may not generalise to current housing market conditions.

## Author
Madiha Fatima Agha

MSc Applied Artificial Intelligence  
University of Westminster

GitHub: https://github.com/MadihaAkber