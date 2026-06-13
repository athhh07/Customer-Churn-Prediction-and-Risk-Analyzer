<div align="center">

# 📊 Customer Churn Prediction System

**End-to-end Machine Learning solution to identify at-risk customers — before they leave.**

[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)](https://scikit-learn.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![ROC-AUC](https://img.shields.io/badge/ROC--AUC-0.901-22C55E?style=for-the-badge)](https://en.wikipedia.org/wiki/Receiver_operating_characteristic)
[![Status](https://img.shields.io/badge/Status-Completed-22C55E?style=for-the-badge)](.)

[**🚀 Live Demo**](#-live-demo) · [**📂 Dataset**](#-dataset) · [**📈 Results**](#-model-performance) · [**▶️ Quick Start**](#️-quick-start)

---

</div>

## 🎯 Overview

Customer churn directly eats into revenue and growth. This project delivers a **full ML pipeline** — from raw behavioral data to a deployed, interactive prediction app — that flags at-risk customers before they leave.


---

## ✨ Features at a Glance

| Module | What it does |
|---|---|
| 🔍 **EDA** | Uncovers churn patterns across behavioral & transactional signals |
| ⚙️ **Feature Engineering** | Derives recency, frequency, and monetary indicators |
| 📌 **Feature Selection** | Reduces 250+ features to the most predictive subset |
| 🤖 **Model Training** | Trains and tunes a high-accuracy classifier |
| 📊 **Evaluation** | Validates with ROC-AUC, precision-recall, and confusion matrix |
| 🌐 **Streamlit App** | Business-friendly UI with real-time churn probability |
| 🚦 **Risk Tiers** | Actionable categories: Healthy / Needs Attention / High Risk |
| 💡 **Recommendations** | Per-customer retention suggestions |

---

## 🚀 Live Demo

<<<<<<< HEAD
> 🔗 **https://customer-churn-prediction-and-risk-analyzer-by-atharva-desai.streamlit.app/**
=======
> 🔗 **[Add your Streamlit Cloud URL here]**
>>>>>>> 1abe0ab (Updated churn prediction model)

---

## 📂 Dataset

Customer behavioral and transactional data covering engagement, purchasing, and revenue patterns.

<div align="center">

| Attribute | Detail |
|---|---|
| **Records** | 112,610 |
| **Features** | 250+ |
| **Target** | Customer Churn (binary) |
| **Type** | Behavioral & Transactional |

</div>

---

## 🔄 Pipeline

```mermaid
flowchart LR
    A([🗂️ Raw Data]) --> B([🔍 EDA])
    B --> C([⚙️ Feature\nEngineering])
    C --> D([📌 Feature\nSelection])
    D --> E([🤖 Model\nTraining])
    E --> F([📊 Evaluation])
    F --> G([🌐 Streamlit\nDeployment])

    style A fill:#6366f1,color:#fff,stroke:none
    style B fill:#8b5cf6,color:#fff,stroke:none
    style C fill:#a855f7,color:#fff,stroke:none
    style D fill:#ec4899,color:#fff,stroke:none
    style E fill:#f43f5e,color:#fff,stroke:none
    style F fill:#f97316,color:#fff,stroke:none
    style G fill:#22c55e,color:#fff,stroke:none
```

---

## 📈 Model Performance

<div align="center">

| Metric | Score |
|---|---|
<<<<<<< HEAD
| **ROC-AUC** | **0.856** ✅ |

</div>

> The model achieves a **ROC-AUC of 0.856**, demonstrating strong discrimination between churned and active customers on held-out data. This means the model correctly ranks a churning customer above an active one ~86% of the time.
=======
| **ROC-AUC** | **0.901** ✅ |

</div>

> The model achieves a **ROC-AUC of 0.901**, demonstrating strong discrimination between churned and active customers on held-out data. This means the model correctly ranks a churning customer above an active one ~90% of the time.
>>>>>>> 1abe0ab (Updated churn prediction model)

---

## 🖥️ Streamlit Application

The deployed app takes six intuitive business inputs and returns a churn probability with an actionable risk label.

### 🎛️ Input Features

| Feature | Business Meaning |
|---|---|
| Days Since Last Visit | How recently the customer engaged |
| Days Since Last Purchase | How recently they bought |
| Purchases This Month | Current purchase activity |
| Avg. Purchases (Last 3 Months) | Historical purchase trend |
| Revenue This Month | Monetary contribution |
| Visits This Month | Website / App engagement |

### 🚦 Risk Categories

| Churn Probability | Risk Level | Recommended Action |
|---|---|---|
| `< 10%` | 🟢 **Healthy** | Standard engagement |
| `10% – 20%` | 🟡 **Needs Attention** | Proactive outreach |
| `> 20%` | 🔴 **High Churn Risk** | Immediate retention offer |

---

## 📸 Screenshots

<<<<<<< HEAD
Home Page  

<img width="1187" height="611" alt="Screenshot 2026-06-11 172724" src="https://github.com/user-attachments/assets/3c3a008a-1a3a-45a7-9b18-333de2942a33" />

Prediction Results

<img width="1296" height="620" alt="Screenshot 2026-06-11 172751" src="https://github.com/user-attachments/assets/feab3ed4-114c-4621-8c31-a517ad39cc08" />
 
=======
| Home Page | Prediction Results |
|---|---|
| _Add screenshot_ | _Add screenshot_ |
>>>>>>> 1abe0ab (Updated churn prediction model)

---

## 🛠️ Tech Stack

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=flat-square&logo=scikitlearn&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=flat-square)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=flat-square&logo=plotly&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)

</div>

---

## 📁 Project Structure

```
customer-churn-prediction/
│
├── 📄 app.py                        # Streamlit application
├── 📄 requirements.txt
├── 📄 README.md
│
├── 📦 models/
│   └── churn_model_simple.pkl       # Trained model artifact
│
├── 📓 notebooks/
│   ├── 01_EDA.ipynb
│   ├── 02_Preprocessing.ipynb
│   ├── 03_Feature_Selection.ipynb
│   ├── 04_Model_Building.ipynb
│   ├── 05_Evaluation.ipynb
│   └── 06_Top_Features_For_App.ipynb
│
└── 📂 data/
```

---

## ▶️ Quick Start

```bash
# 1. Clone the repo
git clone https://github.com/your-username/customer-churn-prediction.git
cd customer-churn-prediction

# 2. Install dependencies
pip install -r requirements.txt

# 3. Launch the app
streamlit run app.py
```

---

## 💼 Business Impact

- 📉 **Reduce revenue loss** by acting on churn signals early
- 🎯 **Target retention campaigns** at the right customers
- 📈 **Increase Customer Lifetime Value** through proactive engagement
- ✅ **Enable data-driven decisions** with explainable risk tiers

---

## 🔮 Roadmap

- [ ] Explainable AI with SHAP values
- [ ] Customer segmentation layer
- [ ] Real-time prediction API (FastAPI)
- [ ] Automated model monitoring & retraining
- [ ] Cloud-based deployment pipeline (AWS / GCP)

---

## 👨‍💻 Author

<div align="center">

<<<<<<< HEAD
**Atharva Desai**
=======
**Atharv**
>>>>>>> 1abe0ab (Updated churn prediction model)
*B.Tech CSE — Data Science*

[![Portfolio](https://img.shields.io/badge/Portfolio-000000?style=for-the-badge&logo=About.me&logoColor=white)](#)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](#)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](#)

📊 Data Analytics &nbsp;|&nbsp; 🤖 Machine Learning &nbsp;|&nbsp; 📈 Business Intelligence

</div>

---

<div align="center">

⭐ **Found this useful? Give it a star — it helps more people discover the project!**

</div>
