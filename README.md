# Thyroid Cancer Recurrence Prediction 🧠

A Machine Learning project that predicts whether a patient is likely to experience **thyroid cancer recurrence** based on clinical and pathological attributes.

---

## 📌 Problem Statement
Thyroid cancer has a generally good survival rate, but recurrence can occur years after treatment. Early prediction helps doctors:

- Plan follow‑up intensity
- Customize treatment strategies
- Reduce unnecessary hospital visits
- Improve patient survival and quality of life

This project builds a predictive model that estimates the probability of recurrence using patient medical data.

---

## 🎯 Objectives
- Analyze clinical thyroid cancer dataset
- Perform preprocessing and feature engineering
- Train multiple ML models
- Evaluate performance using medical‑relevant metrics
- Deploy a reliable recurrence prediction system

---

## 🗂 Dataset Description
The dataset contains patient medical information after thyroid cancer treatment.

### Example Features
| Feature | Description |
|-------|------|
| Age | Patient age at diagnosis |
| Gender | Male/Female |
| Smoking | Smoking history |
| Risk Category | Low / Intermediate / High |
| Tumor Size | Size of tumor in cm |
| Extrathyroidal Extension | Spread outside thyroid |
| Lymph Node Involvement | Cancer spread to nodes |
| Metastasis | Distant metastasis presence |
| Treatment Type | Surgery / Radioiodine |
| Recurrence | Target Variable (Yes/No) |

Target Variable:

```
Recurrence = 1 → Cancer returned
Recurrence = 0 → No recurrence
```

---

## ⚙️ Machine Learning Pipeline

### 1. Data Preprocessing
- Handling missing values
- Encoding categorical features
- Feature scaling
- Class imbalance handling (SMOTE)

### 2. Exploratory Data Analysis
- Distribution analysis
- Correlation heatmaps
- Risk factor identification

### 3. Models Used
- Logistic Regression
- Decision Tree
- Random Forest
- XGBoost
- Support Vector Machine

### 4. Hyperparameter Tuning
Performed using:
- Grid Search / Random Search / Optuna

### 5. Evaluation Metrics
Medical datasets require more than accuracy.

| Metric | Importance |
|------|------|
| Accuracy | Overall correctness |
| Precision | Avoid false alarms |
| Recall (Sensitivity) | Detect recurrence cases |
| F1 Score | Balance precision & recall |
| ROC‑AUC | Model discrimination ability |

> **Recall is prioritized** because missing a recurrence is dangerous in medical diagnosis.

---

## 🧪 Results (Example)
| Model | Accuracy | Recall | ROC‑AUC |
|-----|-----|-----|-----|
| Logistic Regression | 0.86 | 0.82 | 0.88 |
| Random Forest | 0.92 | 0.90 | 0.95 |
| XGBoost | 0.94 | 0.93 | 0.97 |

Best Model: **XGBoost Classifier**

---

## 🚀 How to Run

### 1. Clone Repository
```bash
git clone https://github.com/your-username/thyroid-recurrence-predictor.git
cd thyroid-recurrence-predictor
```

### 2. Create Environment
```bash
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\\Scripts\\activate       # Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Train Model
```bash
python train.py
```

### 5. Predict New Patient
```bash
python predict.py --age 45 --tumor_size 2.1 --nodes 1 --risk high
```

Output:
```
Recurrence Risk: HIGH (87%)
```

---

## 📁 Project Structure
```
thyroid-recurrence-predictor/
│
├── data/
├── notebooks/
├── models/
├── src/
│   ├── preprocessing.py
│   ├── train.py
│   ├── predict.py
│   └── evaluation.py
│
├── requirements.txt
├── README.md
└── app.py (optional deployment)
```

---

## 🔬 Future Improvements
- Deep learning survival analysis
- Time‑to‑recurrence prediction (not just yes/no)
- Integration with hospital EMR systems
- Web dashboard for doctors
- Explainable AI (SHAP values)

---

## ⚠️ Disclaimer
This project is for **educational and research purposes only**. It should not be used as a substitute for professional medical diagnosis.

---

## 👨‍💻 Author
Sayan Soumya

---

## 📜 License
MIT License

