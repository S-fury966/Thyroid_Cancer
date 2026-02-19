import streamlit as st
import requests
import pandas as pd
import plotly.express as px

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="Thyroid Cancer Recurrence Prediction",
    page_icon="🦋",
    layout="wide"
)

# ------------------ TABS ------------------
tab1, tab2 = st.tabs(["🏠 Project Overview", "🔍 Predict Recurrence"])

# =================================================
# 🏠 TAB 1 : FRONT PAGE
# =================================================
with tab1:

    st.title("🦋 Thyroid Cancer Recurrence Prediction System")

    st.markdown(
        """
        ### Why this project?
        Thyroid cancer is among the **most common endocrine malignancies** worldwide.
        Although survival rates are high, **recurrence remains a major clinical challenge**.
        """
    )

    st.divider()

    # # ------------------ IMAGES ------------------
    # col1, col2, col3 = st.columns(3)

    # with col1:
    #     st.image(
    #         "https://upload.wikimedia.org/wikipedia/commons/4/4e/Thyroid_gland.svg",
    #         caption="Thyroid Gland Anatomy",
    #         use_container_width=True
    #     )

    # with col2:
    #     st.image(
    #         "https://www.cancer.gov/sites/g/files/xnrzdm211/files/styles/cgov_article/public/cgov_contextual_image/100/600/8/files/thyroid-cancer-anatomy.jpg",
    #         caption="Thyroid Cancer Location",
    #         use_container_width=True
    #     )

    # with col3:
    #     st.image(
    #         "https://www.researchgate.net/profile/Guang-Yang-22/publication/338572284/figure/fig1/AS:845273253335041@1578583324096/Recurrence-risk-stratification-in-thyroid-cancer.png",
    #         caption="Risk Stratification",
    #         use_container_width=True
    #     )

    # st.divider()

    # ------------------ NECESSITY ------------------
    st.subheader("🚨 Clinical Necessity")

    st.markdown(
        """
        - ❗ **Up to 30%** of thyroid cancer patients experience recurrence  
        - ❗ Recurrence may occur **years after initial treatment**  
        - ❗ Manual risk assessment is **time-consuming & subjective**
        
        ### 🔍 Solution
        This system uses **Machine Learning** to:
        - Analyze patient clinical & pathological features  
        - Predict **risk of recurrence early**
        - Assist doctors in **personalized follow-up planning**
        """
    )

    st.divider()

    # ------------------ CHARTS ------------------
    st.subheader("📊 Data Insights (Sample Visualization)")

    # Sample data for visualization
    chart_data = pd.DataFrame({
        "Risk Level": ["Low", "Intermediate", "High"],
        "Recurrence Rate (%)": [10, 35, 65]
    })

    fig = px.bar(
        chart_data,
        x="Risk Level",
        y="Recurrence Rate (%)",
        color="Risk Level",
        text="Recurrence Rate (%)",
        title="Recurrence Risk by Risk Category"
    )

    fig.update_layout(
        title_x=0.5,
        yaxis_title="Recurrence Probability (%)",
        xaxis_title=""
    )

    st.plotly_chart(fig, use_container_width=True)

    st.divider()

    # ------------------ WHY ML ------------------
    st.subheader("🤖 Why Machine Learning?")

    st.markdown(
        """
        ✔ Handles **complex interactions** between clinical variables  
        ✔ Reduces **human bias**  
        ✔ Provides **consistent and fast predictions**  
        ✔ Scalable for hospital-level deployment  
        
        > This project bridges **healthcare + AI**, making it highly relevant for
        **Data Science, ML, and AI-based roles**.
        """
    )

# =================================================
# 🔍 TAB 2 : PREDICTION PAGE
# =================================================
with tab2:

    st.title("🔍 Predict Thyroid Cancer Recurrence")
    st.markdown("Enter patient details to assess recurrence risk.")

    st.divider()

    with st.form("thyroid_form"):

        age = st.number_input("Age", min_value=1, max_value=120, step=1)
        gender = st.selectbox("Gender", ["Male", "Female"])
        smoking = st.selectbox("Smoking", ["Yes", "No"])
        hx_smoking = st.selectbox("History of Smoking", ["Yes", "No"])
        hx_radiotherapy = st.selectbox("History of Radiotherapy", ["Yes", "No"])

        thyroid_function = st.selectbox(
            "Thyroid Function",
            [
                "Euthyroid",
                "Clinical Hyperthyroidism",
                "Subclinical Hypothyroidism",
                "Subclinical Hyperthyroidism"
            ]
        )

        physical_exam = st.selectbox(
            "Physical Examination",
            [
                "Multinodular goiter",
                "Single nodular goiter-right",
                "Single nodular goiter-left",
                "Normal",
                "Diffuse goiter"
            ]
        )

        adenopathy = st.selectbox(
            "Adenopathy",
            ["No", "Right", "Bilateral", "Left", "Extensive", "Posterior"]
        )

        pathology = st.selectbox(
            "Pathology",
            ["Papillary", "Micropapillary", "Follicular", "Hurthel cell"]
        )

        focality = st.selectbox("Focality", ["Uni-Focal", "Multi-Focal"])
        risk = st.selectbox("Risk", ["Low", "Intermediate", "High"])

        tumor_stage = st.selectbox(
            "Tumor Stage",
            ["T1a", "T1b", "T2", "T3a", "T3b", "T4a", "T4b"]
        )

        node_stage = st.selectbox("Regional Node Stage", ["N0", "N1a", "N1b"])
        metastatic_stage = st.selectbox("Metastatic Stage", ["M0", "M1"])
        stage = st.selectbox("Overall Stage", ["I", "II", "III", "IVA", "IVB"])

        response = st.selectbox(
            "Response to Therapy",
            ["Excellent", "Structural Incomplete", "Intermediate", "Biochemical Incomplete"]
        )

        submit = st.form_submit_button("🔮 Predict")

    if submit:
        payload = {
            "age": age,
            "gender": gender,
            "smoking": smoking,
            "hx_smoking": hx_smoking,
            "hx_radiotherapy": hx_radiotherapy,
            "thyroid_function": thyroid_function,
            "physical_examination": physical_exam,
            "adenopathy": adenopathy,
            "pathology": pathology,
            "focality": focality,
            "risk": risk,
            "tumor_stage": tumor_stage,
            "regional_node_stage": node_stage,
            "metastatic_stage": metastatic_stage,
            "stage": stage,
            "response": response
        }

        try:
            res = requests.post("http://127.0.0.1:8000/predict", json=payload)

            if res.status_code == 200:
                prediction = res.json()["prediction"]

                st.divider()
                st.subheader("📌 Result")

                if prediction == 'Chances of Recursion':
                    st.error("⚠️ High Risk of Thyroid Cancer Recurrence")
                else:
                    st.success("✅ Low Risk of Thyroid Cancer Recurrence")

            else:
                st.error("Backend error. Check FastAPI server.")

        except Exception as e:
            st.error(f"Connection error: {e}")
