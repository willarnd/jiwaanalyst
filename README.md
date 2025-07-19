# 🧠 Life Insurance Claim Analysis

This is my very first project as an aspiring data analyst. I used data from Kaggle, where each row represents an individual life insurance claim. Through this dataset, I aimed to uncover insights that could support strategic business decisions, particularly those related to risk assessment and underwriting in the life insurance industry.

---

## 📁 Project Structure

```plaintext
life-insurance-claim-analysis/
│
├── Life_Insurance_Claim_Analysis.py   ← Main Python analysis script
├── data/
│   └── life_insurance_dataset.xlsx    ← Raw dataset (from Kaggle)
├── output_charts/                     ← Folder for generated visualizations
│   ├── age_distribution.png
│   ├── smoker_vs_age.png
│   ├── regresi_all_the_factor.png
│   └── ...
├── requirements.txt                   ← Required Python packages
└── README.md                          ← You're reading it 😍
```


---

## 📊 Dataset

Dataset used: [Individual Age of Death and Related Factors](https://www.kaggle.com/datasets/joannpineda/individual-age-of-death-and-related-factors/data)

Features include:

- Demographics (age, sex, weight, height)
- Lifestyle (smoking, alcohol, drug use)
- Family medical history
- Chronic conditions and health factors

Target variable: `age` — representing the age at which a life insurance claim occurred (due to death).

---

## 🔍 Key Questions

1. At what age do most life insurance claims occur?
2. Do lifestyle behaviors like smoking or opioid use significantly affect age at death?
3. Is there a link between family health history and claim timing?
4. What are the top predictors of age at death?

---

## 📈 Analysis Overview

- **Data Cleaning**: Missing values and data types were checked and handled.
- **Exploratory Analysis**: Visualized distributions and patterns across key variables.
- **Regression Modeling**: Identified most influential features on age at death.

---

## 📊 Visualizations (Examples)

### 1. Age Distribution
![Age Distribution](https://github.com/willarnd/life-insurance-claim-analysis/blob/main/output_charts/Distribusi%20Usia%20Kematian.png)

**Insight:** Most life insurance claims occur between ages 60–70. However, a significant number happen at younger ages, highlighting early-risk segments.

---

### 2. Age vs Smoking
![Smoking](https://github.com/willarnd/life-insurance-claim-analysis/blob/main/output_charts/Age_Vs_Smoke.png)

**Insight:** Smokers tend to die younger than non-smokers, reinforcing the impact of smoking on life expectancy.

---

### 3. Age vs Opioid Use
![Opioids](https://github.com/willarnd/life-insurance-claim-analysis/blob/main/output_charts/Age_vs_opiods.png)

**Insight:** Opioid users have lower average ages at death. Usage shows a strong negative correlation with longevity.

---

### 4. Age vs Alcohol Consumption
![Alcohol](https://github.com/willarnd/life-insurance-claim-analysis/blob/main/output_charts/age_vs_drinking.png)

**Insight:** Higher alcohol consumption is associated with earlier death.

---

### 5. Age vs Other Drug Use
![Drugs](https://github.com/willarnd/life-insurance-claim-analysis/blob/main/output_charts/age_vs_drugs.png)

**Insight:** Other drug usage also shows a negative correlation with age at death.

---

### 6. Family Cancer History
![Family Cancer](https://github.com/willarnd/life-insurance-claim-analysis/blob/main/output_charts/age_vs_familycancer.png)

**Insight:** Participants with family cancer history show slightly lower life expectancy.

---

### 7. Family Cholesterol History
![Family Cholesterol](https://github.com/willarnd/life-insurance-claim-analysis/blob/main/output_charts/age_vs_familycholesterol.png)

**Insight:** High cholesterol in family history appears to affect age at death but less strongly than lifestyle factors.

---

### 8. Family Heart Disease History
![Heart Disease](https://github.com/willarnd/life-insurance-claim-analysis/blob/main/output_charts/age_vs_familyheartdisease.png)

**Insight:** Participants with heart disease history in the family tend to have lower life expectancy.

---

### 9. Linear Regression: Most Influential Factors
![Regression](https://github.com/willarnd/life-insurance-claim-analysis/blob/main/output_charts/regresi_all_the_factor.png)

**Insight:** Addiction, immune deficiency, and opioid use are the strongest negative predictors of age at death, making them crucial variables in risk modeling.

---

## 💡 Business Recommendations

Based on the analysis, here are some actionable business recommendations for life insurance stakeholders:

- **Underwriting Optimization**: Include high-risk behaviors (e.g., addiction, opioid use) in underwriting criteria.
- **Tiered Premium Modeling**: Segment high-risk individuals into premium bands to reflect mortality risk.
- **Customer Education**: Promote healthy living through educational content targeting smoking, drug use, and alcohol abuse.
- **Wellness Incentives**: Partner with health providers to offer incentives for checkups and risk screenings.
- **Hereditary Factor Disclosures**: Allow applicants to declare family history of diseases as optional riders or factors.

---

## ⚙️ Tools Used

- Python (pandas, matplotlib, seaborn, scikit-learn)
- Visual Studio Code
- Dataset from Kaggle

---

## 🧪 Requirements

Install required packages using pip:

```bash
pip install -r requirements.txt


📌 Author
👤 Willy Sekewael
🔗 https://www.linkedin.com/in/willysekewael/
