import streamlit as st
import pandas as pd
import pickle


# PAGE CONFIG

st.set_page_config(
    page_title="Customer Churn Risk Analyzer",
    page_icon="📊",
    layout="centered"
)


# LOAD MODEL

with open("models/churn_model_simple.pkl", "rb") as file:
    model = pickle.load(file)


# HEADER

st.title("📊 Customer Churn Risk Analyzer")

st.markdown("""
Predict the likelihood of customer churn based on recent
engagement and purchasing behavior.
""")

st.divider()


# USER INPUTS

col1, col2 = st.columns(2)

with col1:

    session_recency_min = st.number_input(
        "Days Since Last Visit",
        min_value=0,
        value=2,
        step=1
    )

    purchase_recency_min = st.number_input(
        "Days Since Last Purchase",
        min_value=0,
        value=2,
        step=1
    )

    purchase_count_month_lag0 = st.number_input(
        "Purchases This Month",
        min_value=0,
        value=3,
        step=1
    )

with col2:

    purchase_count_month_ma3 = st.number_input(
        "Average Purchases (Last 3 Months)",
        min_value=0.0,
        value=2.0
    )

    purchase_revenue_month_lag0 = st.number_input(
        "Revenue This Month ($)",
        min_value=0.0,
        value=100.0
    )

    session_count_month_lag0 = st.number_input(
        "Visits This Month",
        min_value=0,
        value=5,
        step=1
    )

st.divider()


# PREDICTION

if st.button("Predict Churn Risk", use_container_width=True):

    input_data = pd.DataFrame({

        "session_recency_min": [session_recency_min],

        "purchase_recency_min": [purchase_recency_min],

        "purchase_count_month_lag0": [purchase_count_month_lag0],

        "purchase_count_month_ma3": [purchase_count_month_ma3],

        "purchase_revenue_month_lag0": [purchase_revenue_month_lag0],

        "session_count_month_lag0": [session_count_month_lag0]

    })

    probability = model.predict_proba(input_data)[0][1]

    churn_percent = probability * 100


    # RESULT
   
    st.subheader("Prediction Result")

    st.metric(
        "Churn Probability",
        f"{churn_percent:.2f}%"
    )
    st.progress(float(probability))


    # RISK STATUS
  
    if churn_percent < 30:

        st.success("🟢 Customer Status: Healthy")

    elif churn_percent < 60:

        st.warning("🟡 Customer Status: Needs Attention")

    else:

        st.error("🔴 Customer Status: High Churn Risk")


    # BUSINESS INTERPRETATION
    
    st.subheader("Business Interpretation")

    if churn_percent >= 60:

        st.write("""
The customer shows strong indicators of churn.

Recent engagement and purchasing behavior suggest declining activity.
Immediate retention actions are recommended.
        """)

    elif churn_percent >= 30:

        st.write("""
The customer shows moderate churn risk.

Monitoring activity and increasing engagement may help prevent future churn.
        """)

    else:

        st.write("""
The customer appears active and engaged.

Current behavior indicates a low likelihood of churn.
        """)


    
    # RECOMMENDATIONS
    
    st.subheader("Recommended Action")

    if churn_percent >= 60:

        st.markdown("""
- 🎯 Send a personalized retention offer
- 💰 Provide discount coupons
- 📧 Launch a re-engagement email campaign
- 🤝 Contact customer directly if possible
        """)

    elif churn_percent >= 30:

        st.markdown("""
- 📈 Monitor customer behavior
- 🛍 Recommend relevant products
- 📧 Increase engagement through targeted campaigns
        """)

    else:

        st.markdown("""
- ✅ Continue regular engagement
- ⭐ Reward customer loyalty
- 📊 Monitor activity periodically
        """)
