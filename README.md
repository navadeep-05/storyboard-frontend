# 🌾 Prediction of Agriculture Crop Production in India  
### Machine Learning Project | Internship – upSkill Campus & UniConverge Technologies Pvt. Ltd. (UCT)

This repository contains the complete implementation of the project **“Prediction of Agriculture Crop Production in India”**, developed as part of the Industrial Internship organized by **upSkill Campus**, **The IoT Academy**, and **UniConverge Technologies Pvt. Ltd. (UCT)**.

The goal of this project is to build a **machine learning model** capable of predicting crop yield based on historical agricultural data, cost of cultivation, crop type, and state-level attributes.

---

## 📌 **Project Overview**

Agriculture plays a vital role in India’s economy, and accurate crop production prediction is essential for:

- Policy-making  
- Resource allocation  
- Supply chain planning  
- Minimizing risks for farmers  
- Improving agricultural decision-making  

This project uses supervised machine learning techniques (Random Forest Regression) to estimate **crop yield (Quintal/Hectare)** based on cost, crop, and location features.

---

## 📁 **Repository Structure**

Crop-Production-Prediction-India/
│
├── src/
│ ├── model.py # Main ML model code
│ ├── dataset1_cost_yield.csv # Dataset used for training
│ └── crop_yield_prediction_model.pkl # Saved trained model
│
├── report/
│ ├── Internship_Report.docx # Internship report (editable)
│ └── Internship_Report.pdf # Final report (for submission)
│
└── README.md # Project documentation

## 📊 **Dataset Description**

The dataset includes:

- **Crop**  
- **State**  
- **Cost of Cultivation (A2+FL)**  
- **Cost of Cultivation (C2)**  
- **Cost of Production (C2)**  
- **Yield (Quintal/Hectare)** *(Target variable)*  

This data was preprocessed, encoded, and used to train the machine learning model.

---

## 🤖 **Machine Learning Model Used**

### **Random Forest Regressor**
Chosen due to:

- High accuracy  
- Good performance on tabular agricultural data  
- Ability to handle both numerical and categorical features  
- Lower risk of overfitting
