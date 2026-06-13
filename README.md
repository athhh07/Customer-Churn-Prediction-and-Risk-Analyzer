<div align="center">

<img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/XGBoost-Powered-FF6600?style=for-the-badge&logo=xgboost&logoColor=white"/>
<img src="https://img.shields.io/badge/Streamlit-Deployed-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"/>
<img src="https://img.shields.io/badge/ROC--AUC-0.856-2ECC71?style=for-the-badge&logo=checkmarx&logoColor=white"/>
<img src="https://img.shields.io/badge/Dataset-112K%20Records-8E44AD?style=for-the-badge&logo=databricks&logoColor=white"/>

<br/><br/>

# 📊 Customer Churn Prediction & Risk Analyzer

### *Predict. Prioritize. Retain.*

**An end-to-end Machine Learning system that identifies at-risk customers in real time and powers proactive retention strategies — trained on 112,610 behavioral records.**

<br/>

[![Live Demo](https://img.shields.io/badge/🚀%20Live%20Demo-Click%20Here-FF4B4B?style=for-the-badge)](https://customer-churn-prediction-and-risk-analyzer-by-atharva-desai.streamlit.app/)
[![GitHub Repo](https://img.shields.io/badge/📁%20GitHub-Repository-181717?style=for-the-badge&logo=github)](https://github.com/athhh07/Customer-Churn-Prediction-and-Risk-Analyzer)

</div>

---

## 🧭 Table of Contents

- [Project Overview](#-project-overview)
- [Dataset](#-dataset)
- [Features Used](#-features-used-in-deployment)
- [Model Performance](#-model-performance)
- [Streamlit Application](#️-streamlit-application)
- [Risk Categories](#-risk-categories)
- [Tech Stack](#️-tech-stack)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Business Value](#-business-value)
- [Author](#-author)

---

## 🎯 Project Overview

> Customer churn silently erodes revenue. This project turns behavioral signals into actionable predictions — before it's too late.

This solution delivers a **complete ML pipeline** from raw data to a deployed interactive web application:

| Stage | What Happens |
|---|---|
| 🧹 **Data Preprocessing** | Cleaning, normalization, handling missing values |
| 🔍 **Exploratory Analysis** | Business-focused EDA with visual insights |
| ⚙️ **Feature Engineering** | Selecting the most predictive behavioral signals |
| 🤖 **Model Training** | XGBoost with cross-validation and hyperparameter tuning |
| 🧠 **Explainability** | SHAP values for transparent, interpretable predictions |
| 🌐 **Deployment** | Real-time Streamlit web app with risk categorization |

---

## 📂 Dataset

<img src="https://img.shields.io/badge/Records-112%2C610-0D6EFD?style=flat-square"/> <img src="https://img.shields.io/badge/Source-Behavioral%20%26%20Transactional-6C757D?style=flat-square"/>

The model is trained on rich customer behavioral and transactional data, capturing signals across multiple dimensions:

- 📅 **Engagement Activity** — visit frequency, recency of interactions
- 🛒 **Purchase History** — monthly and historical purchase volumes
- 💰 **Revenue Metrics** — current and trend-based revenue signals
- 📱 **Session Behavior** — depth and frequency of platform usage

---

## ⚙️ Features Used in Deployment

The deployed model distills complex behavioral data into **6 intuitive business metrics**, making it accessible to non-technical stakeholders:

| # | Feature | Business Signal |
|---|---|---|
| 1 | 📅 **Days Since Last Visit** | Engagement recency |
| 2 | 🛒 **Days Since Last Purchase** | Purchase recency |
| 3 | 🔢 **Purchases This Month** | Current buying activity |
| 4 | 📊 **Avg. Purchases (Last 3 Months)** | Historical purchasing trend |
| 5 | 💵 **Revenue This Month** | Current customer value |
| 6 | 👁️ **Visits This Month** | Platform engagement frequency |

---

## 🤖 Model Performance

<div align="center">

| Metric | Score | Interpretation |
|---|---|---|
| 🎯 **ROC-AUC** | **0.856** | Strong discriminative power |

</div>

> A ROC-AUC of **0.856** means the model correctly ranks a churning customer above a non-churning one **85.6% of the time** — significantly better than random chance (0.5).

---

## 🖥️ Streamlit Application

The interactive web application brings ML predictions directly to business users — **no code required**.

**What you can do:**

- ✅ Enter live customer behavior metrics via a clean UI
- ✅ Get instant churn probability scores
- ✅ View color-coded risk classification
- ✅ Receive tailored, business-focused retention recommendations

---

## 🚦 Risk Categories

<div align="center">

| Churn Probability | Risk Level | Recommended Action |
|---|---|---|
| **< 30%** | 🟢 **Healthy** | Standard engagement |
| **30% – 60%** | 🟡 **Needs Attention** | Targeted outreach / offers |
| **> 60%** | 🔴 **High Churn Risk** | Immediate retention intervention |

</div>

---

## 🛠️ Tech Stack

<div align="center">

<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white"/>
<img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white"/>
<img src="https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=matplotlib&logoColor=white"/>
<img src="https://img.shields.io/badge/Seaborn-4CB8C4?style=for-the-badge&logoColor=white"/>
<img src="https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white"/>
<img src="https://img.shields.io/badge/XGBoost-FF6600?style=for-the-badge&logoColor=white"/>
<img src="https://img.shields.io/badge/SHAP-FF0000?style=for-the-badge&logoColor=white"/>
<img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"/>

</div>

---

## 📁 Project Structure

```
Customer-Churn-Prediction-and-Risk-Analyzer/
│
├── 📄 app.py                          # Streamlit web application
├── 📋 README.md                       # Project documentation
├── 📦 requirements.txt                # Python dependencies
│
├── 🧠 models/
│   └── churn_model_simple.pkl         # Trained XGBoost model
│
└── 📓 notebooks/
    ├── 01_data_understanding_and_cleaning.ipynb
    ├── 02_business_eda.ipynb
    ├── 03_feature_selection.ipynb
    ├── 04_model_training.ipynb
    ├── 05_model_explainability.ipynb
    ├── 06_deployment_model.ipynb
    └── 07_limited_features_model.ipynb
```

---

## ▶️ Installation

```bash
# 1. Clone the repository
git clone https://github.com/athhh07/Customer-Churn-Prediction-and-Risk-Analyzer.git

# 2. Navigate to the project directory
cd Customer-Churn-Prediction-and-Risk-Analyzer

# 3. Install dependencies
pip install -r requirements.txt

# 4. Launch the Streamlit app
streamlit run app.py
```

> 💡 **Tip:** It's recommended to use a virtual environment (`venv` or `conda`) to avoid dependency conflicts.

---

## 💼 Business Value

This project directly addresses one of the most costly challenges in customer-centric businesses:

```
📉  Reduce revenue loss from undetected churn
🎯  Identify at-risk customers weeks before they leave
💬  Equip retention teams with data-backed insights
📈  Improve ROI on customer success and marketing spend
🔄  Enable proactive, personalized retention strategies
```

---

## 👨‍💻 Author

<div align="center">

**Atharva Desai**
*B.Tech CSE (Data Science)*

[![GitHub](https://img.shields.io/badge/GitHub-athhh07-181717?style=for-the-badge&logo=github)](https://github.com/athhh07)

---

*If you found this project useful, please consider giving it a* ⭐

</div>
