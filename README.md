# Life Insurance Claim Analysis 🕊️

This project explores patterns in life insurance claim data to understand:  
**What are the key factors that contribute to early death?**

By combining storytelling and data exploration, I analyzed how health conditions, lifestyle choices, and family history impact the age at which individuals pass away — which is at the core of life insurance claims.

---

## 🧪 Background

Life insurance claims are on the rise.  
But the question is: **Why?**

Is it poor lifestyle choices? Pre-existing health conditions? Or something inherited from family?

This project started with a simple curiosity:
> “What’s really behind the growing number of life insurance claims?”

---

## 🎯 Project Objectives

- Explore the age distribution of life insurance claimants
- Analyze the impact of lifestyle factors (smoking, alcohol, drug use) on age at death
- Examine whether family medical history contributes to early mortality
- Build a simple regression model to identify which features most significantly affect life expectancy

---

## 🗂️ Dataset Overview

File: `life_insurance_dataset.xlsx`

Each row represents a **confirmed life insurance claim** (i.e., the individual has passed away).  
Columns include:
- Demographics: age, gender, weight, height, blood pressure
- Lifestyle: smoking, drinking, drug use, addiction
- Health: diabetes, heart disease, cholesterol levels, immune deficiency
- Family history: cancer, heart disease, cholesterol issues

---

## 🔍 Key Findings

### 📊 Age Distribution
Most claims occurred between the ages of 60–75. However, around 18% of deaths occurred **under age 50**, raising concern.

### 🚬 Lifestyle Impact
Smokers and opioid users tended to die younger.  
On average, individuals using opioids passed away **11 years earlier** than non-users.

### 🧬 Family Medical History
Participants with a family history of **heart disease or cancer** also showed a lower average age at death.

### 📈 Linear Regression Insights
The most impactful features in predicting early death were:
- **Immune deficiency**
- **Addiction and opioid use**
- **Heart disease and diabetes**
- **Family health history**

Meanwhile, physical attributes like weight, height, or cholesterol showed minimal influence.

---

## 🔧 Tools Used

- **Visual Studio Code** – primary development environment
- **Python** – for data processing and modeling
- **pandas, seaborn, matplotlib, scikit-learn** – for EDA, visualization, and regression modeling
- **Excel** – original data format

---

## 📁 Repository Structure

