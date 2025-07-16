from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import pandas as pd  # <-- ✅ use pandas!

# Load the pipeline
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

app = FastAPI()

class CustomerData(BaseModel):
    tenure: int
    MonthlyCharges: float
    TotalCharges: float
    Contract: str
    PaymentMethod: str

@app.get("/")
def root():
    return {"message": "Churn Prediction API running"}

@app.post("/predict")
def predict_churn(data: CustomerData):
    # ✅ Build a DataFrame with correct column names
    df = pd.DataFrame([{
        "tenure": data.tenure,
        "MonthlyCharges": data.MonthlyCharges,
        "TotalCharges": data.TotalCharges,
        "Contract": data.Contract,
        "PaymentMethod": data.PaymentMethod
    }])

    # ✅ Predict
    y_pred = model.predict_proba(df)[0][1]

    return {"churn_probability": round(float(y_pred), 2)}

