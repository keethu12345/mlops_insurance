# mlops-insurance

# 🏥 Insurance Charges Prediction API

This project is a full-stack MLOps application that predicts medical insurance charges based on a user's input. It uses a machine learning model trained with scikit-learn, served via a FastAPI backend, and deployed on Render using Docker.

## 🚀 Live Demo

Access the API at: [https://insurance-api-mq3g.onrender.com/docs](https://insurance-api-mq3g.onrender.com'docs)

## 📊 Model Overview

- **Model Type**: Linear Regression
- **Dataset**: [Insurance Dataset](https://www.kaggle.com/datasets/mirichoi0218/insurance)
- **Target**: `charges`
- **Features**: `age`, `sex`, `bmi`, `children`, `smoker`, `region`

## 🧰 Tech Stack

- Python, FastAPI
- Scikit-learn
- Docker
- Render.com (for deployment)

## 📦 Project Structure

mlops-insurance/ ├── insurance.csv ├── model.pkl ├── train.py # Trains the model ├── predict.py # FastAPI app for predictions ├── Dockerfile # For containerization └── frontend/ └── index.html # Optional simple frontend


## 🧪 API Usage

Send a POST request to `/predict` with the following JSON:

json
{
  "age": 35,
  "sex": "male",
  "bmi": 28.5,
  "children": 2,
  "smoker": "yes",
  "region": "southeast"
}
{
  "predicted_charge": 32045.67
}

## 🐳 Docker Instructions
docker build -t insurance-api .
docker run -d -p 8000:8000 insurance-api

## ✨ Author
Built by keethu12345
