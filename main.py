from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel
import pandas as pd
import pickle
import os

BASE_DIR = os.path.dirname(__file__)
MODEL_PATH = os.path.join(BASE_DIR, "model.pkl")

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

app = FastAPI()

class CustomerData(BaseModel):
    tenure: int
    MonthlyCharges: float
    TotalCharges: float
    Contract: str
    PaymentMethod: str

@app.get("/", response_class=HTMLResponse)
def index():
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Customer Churn Predictor</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                max-width: 600px;
                margin: auto;
                padding: 20px;
                background: #f9f9f9;
            }
            h1 { text-align: center; }
            input, select {
                width: 100%;
                padding: 10px;
                margin: 8px 0;
                box-sizing: border-box;
            }
            button {
                background-color: #4CAF50;
                color: white;
                padding: 12px 20px;
                border: none;
                cursor: pointer;
                width: 100%;
            }
            button:hover { background-color: #45a049; }
            #result {
                margin-top: 20px;
                font-size: 1.2em;
                font-weight: bold;
                color: #333;
            }
        </style>
    </head>
    <body>
        <h1>Customer Churn Predictor</h1>
        <label>Tenure:</label>
        <input type="number" id="tenure" required>

        <label>Monthly Charges:</label>
        <input type="number" step="0.01" id="MonthlyCharges" required>

        <label>Total Charges:</label>
        <input type="number" step="0.01" id="TotalCharges" required>

        <label>Contract:</label>
        <input type="text" id="Contract" required>

        <label>Payment Method:</label>
        <input type="text" id="PaymentMethod" required>

        <button onclick="predictChurn()">Predict Churn</button>

        <div id="result"></div>

        <script>
            async function predictChurn() {
                const data = {
                    tenure: parseInt(document.getElementById('tenure').value),
                    MonthlyCharges: parseFloat(document.getElementById('MonthlyCharges').value),
                    TotalCharges: parseFloat(document.getElementById('TotalCharges').value),
                    Contract: document.getElementById('Contract').value,
                    PaymentMethod: document.getElementById('PaymentMethod').value
                };

                const response = await fetch('/predict', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(data)
                });

                const result = await response.json();
                document.getElementById('result').innerText = 
                    `Churn Probability: ${result.churn_probability}%`;
            }
        </script>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)

@app.post("/predict")
def predict(data: CustomerData):
    df = pd.DataFrame([{
        "tenure": data.tenure,
        "MonthlyCharges": data.MonthlyCharges,
        "TotalCharges": data.TotalCharges,
        "Contract": data.Contract,
        "PaymentMethod": data.PaymentMethod
    }])
    y_pred = model.predict_proba(df)[0][1]
    return JSONResponse(content={"churn_probability": round(float(y_pred) * 100, 2)})

