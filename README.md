# 📞 Telecom Churn Prediction API

This repository contains a deployed Machine Learning API that predicts customer churn in the telecom sector. The project is built using **Python**, **FastAPI**, and deployed via **Render**. It demonstrates how to integrate ML models with backend APIs and serves as a great starting point for ML deployment workflows.

![Python](https://img.shields.io/badge/Python-3.10-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-💚-green)
![Render](https://img.shields.io/badge/Deployed%20on-Render-purple)
![VS Code](https://img.shields.io/badge/Code%20Editor-VS%20Code-blue)

---

## 🚀 Project Demo

🔗 **Live API Endpoint**: [[https://your-render-api-url.onrender.com](https://mlapi2-1.onrender.com)]

📮 **Try on Postman**: Use the `/predict` endpoint with sample JSON input:
```json
{
  "tenure": 12,
  "monthlycharges": 75.4,
  "totalcharges": 2345.50,
  "contract": "Month-to-month",
  "internetservice": "Fiber optic",
  "paymentmethod": "Electronic check"
}
📦 Features
🔮 Predicts if a telecom customer will churn

🚀 FastAPI-based asynchronous backend

🧠 Model trained using logistic regression / random forest / (custom ML model)

🌐 Deployed on Render

🧪 Fully testable using Postman

📁 Clean and modular codebase using VS Code

🛠️ Tech Stack
Language: Python

Framework: FastAPI

Model Training: scikit-learn / pandas / numpy

Deployment: Render (free tier)

Testing: Postman

IDE: VS Code

📁 Project Structure
graphql
Copy
Edit
telecom-churn-api/
│
├── app/
│   ├── main.py             # FastAPI app and routes
│   ├── model.py            # ML model loading and prediction logic
│   ├── schema.py           # Pydantic models for request/response
│   └── utils.py            # Helper functions
│
├── model/
│   └── churn_model.pkl     # Trained ML model
│
├── requirements.txt        # Python dependencies
├── render.yaml             # Render deployment configuration
├── .gitignore
└── README.md
🧠 Model Training (Overview)
The model is trained on a telecom churn dataset using preprocessing pipelines and ML algorithms such as:

Logistic Regression

Random Forest

XGBoost (optional)

Key features used:

Tenure, MonthlyCharges, TotalCharges

Contract type, InternetService, PaymentMethod

✅ Model is saved using joblib or pickle.

▶️ How to Run Locally
Clone the repository

bash
Copy
Edit
git clone https://github.com/yourusername/telecom-churn-api.git
cd telecom-churn-api
Create a virtual environment & install dependencies

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
Run the API locally

bash
Copy
Edit
uvicorn app.main:app --reload
Visit http://127.0.0.1:8000/docs to view the interactive Swagger UI.

☁️ Deployment on Render
Push your code to GitHub

Connect GitHub repo to Render

Add render.yaml or set build/run command:

Build Command: pip install -r requirements.txt

Start Command: uvicorn app.main:app --host 0.0.0.0 --port 10000

Deploy and go live!

📌 Make sure churn_model.pkl is in your repo and correctly loaded.

🧪 API Usage Guide
POST /predict
Request Body (JSON):

json
Copy
Edit
{
  "tenure": 24,
  "monthlycharges": 82.5,
  "totalcharges": 1980.2,
  "contract": "Two year",
  "internetservice": "DSL",
  "paymentmethod": "Mailed check"
}
Response:

json
Copy
Edit
{
  "churn_prediction": "No",
  "churn_probability": 0.13
}
🧠 Future Work
Add authentication for API access

Model versioning

Dockerize for portability

Add logging and monitoring (e.g. with Prometheus)

🙋‍♂️ Author
Anand Kumar
🔗 LinkedIn | 🐙 GitHub | 🐦 Twitter

📄 License
This project is licensed under the MIT License.

Built with 💡 curiosity, ☕ caffeine, and 🚀 FastAPI
