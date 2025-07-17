# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder

# Load dataset dari GitHub
url = "https://raw.githubusercontent.com/willarnd/jiwaanalyst/main/data/life_insurance_dataset.xlsx"
df = pd.read_excel(url, engine="openpyxl")

# Cek struktur data
print(df.info())
print(df.describe())
print(df.isnull().sum())

# Distribusi usia
plt.figure(figsize=(8,5))
sns.histplot(df['age'], bins=20, kde=True)
plt.title("Distribusi Usia Kematian")
plt.xlabel("Usia")
plt.ylabel("Jumlah Klaim")
plt.show()

# Perbandingan usia per gender
plt.figure(figsize=(8,5))
sns.boxplot(x='sex', y='age', data=df)
plt.title("Usia Kematian Berdasarkan Gender")
plt.xlabel("Jenis Kelamin")
plt.ylabel("Usia")
plt.show()

# Analisis gaya hidup
lifestyle_cols = ['smoker', 'opioids', 'drinks_aweek', 'addiction']

for col in lifestyle_cols:
    plt.figure(figsize=(6,4))
    sns.boxplot(x=col, y='age', data=df)
    plt.title(f"Usia Meninggal Berdasarkan {col.capitalize()}")
    plt.show()

# Statistik usia perokok vs non-perokok
print(df.groupby('smoker')['age'].describe())

# Analisis riwayat keluarga
family_cols = ['family_cancer', 'family_heart_disease', 'family_cholesterol']

for col in family_cols:
    plt.figure(figsize=(6,4))
    sns.boxplot(x=col, y='age', data=df)
    plt.title(f"Usia Meninggal vs {col.replace('_', ' ').title()}")
    plt.show()

# Regresi linier: pengaruh fitur terhadap usia meninggal
df_model = df.copy()
categorical_cols = df_model.select_dtypes(include='object').columns

for col in categorical_cols:
    df_model[col] = LabelEncoder().fit_transform(df_model[col])

X = df_model.drop('age', axis=1)
y = df_model['age']

model = LinearRegression()
model.fit(X, y)

# Visualisasi koefisien
feature_importance = pd.DataFrame({
    'Feature': X.columns,
    'Coefficient': model.coef_
}).sort_values(by='Coefficient')

plt.figure(figsize=(10,6))
sns.barplot(data=feature_importance, x='Coefficient', y='Feature')
plt.title("Pengaruh Fitur Terhadap Usia Meninggal (Regresi Linier)")
plt.show()
