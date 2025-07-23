# 🛡️ Phishing Website Detection using Machine Learning

## 📌 Project Overview

Phishing is a major cybersecurity threat where attackers deceive users into revealing sensitive information by impersonating legitimate websites. This project leverages Machine Learning (ML) techniques to detect phishing websites based on their characteristics and behavior.

This repository contains the implementation of a phishing website detection system using a trained ML model, deployed through a web interface using **Flask**. It analyzes website features and classifies them as either legitimate or phishing.

---

## 📊 Features

- 🚀 Detects phishing websites based on 30+ extracted features.
- 🔍 Uses ML models such as Random Forest, Logistic Regression, and XGBoost.
- 💾 Includes dataset preprocessing, feature engineering, and model training.
- 🌐 User-friendly web interface using Flask.
- 📁 Modular code: `app.py`, `feature.py`, `model.pkl`, etc.

---

## 🧠 Machine Learning Models Used

- Logistic Regression
- Random Forest
- XGBoost (optional for comparison)
- Isolation Forest (for anomaly detection / outliers)

---

## 🛠️ Tech Stack

| Component      | Technology        |
|----------------|-------------------|
| Language       | Python 3.x         |
| Libraries      | pandas, sklearn, numpy, Flask, joblib |
| Deployment     | Flask web app      |
| Dataset        | `phishing.csv` (31 columns including label `class`) |

---

## 📁 Project Structure

📦 phishing-detection-ml
├── app.py # Flask app for user interaction
├── feature.py # Feature extraction from URL or input
├── phishing.csv # Dataset used for training and testing
├── model.pkl # Trained machine learning model
├── phishing_model.ipynb# Notebook with full training pipeline
├── requirements.txt # Python dependencies
└── templates/
└── index.html # Web UI template
