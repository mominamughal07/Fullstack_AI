import pandas as pd 
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import OrdinalEncoder
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



df_life = pd.read_csv("C:\\Users\\Lenovo\\Documents\\GitHub\\Fullstack_AI\\Machine learning\\Data_sets\\Regression\\Life Expectancy Data.csv")

print("\n                              – · • ✤ • · –  DATASET AS PANDAS DATAFRAME  – · • ✤ • · – ")
print("                              ===========================================================\n")
print(df_life)
print("=============================================================================================================================================================================================\n")

print("\n                              – · • ✤ • · –  EXPLORATORY DATA ANALYSIS – · • ✤ • · – ")
print("                              ===========================================================\n")
print(f"Shape of the dataset : {df_life.shape}")
print(f"Coloumns of dataset : {df_life.columns}")
print(f"Info of dataset : \n{df_life.info()}")
print(f"First 7 rows of dataset : \n {df_life.head()}")
print(f"Ramdon 7 rows of dataset : \n {df_life.sample()}")
print(f"Missing rows of dataset : {df_life.isnull().sum()}")
print(f"Duplicate rows of dataset : {df_life.duplicated().sum()}")
print(f"Stats of dataset : \n {df_life.describe()}")
print(f"shape of dataset : \n {df_life.shape}")
print("=============================================================================================================================================================================================\n")

print("\n                              – · • ✤ • · –  DATA CLEANING  – · • ✤ • · – ")
print("                              ===========================================================\n")

print("   ✤ Cleaning Spaces ✤ ")                                                                                              # str.strip() removes leading and trailing spaces.
df_life.columns = df_life.columns.str.strip().str.replace(" " , "_").str.replace("/" , "_")                                    # str.replace(' ', '_') changes spaces to underscores.
print("First five rows of df_life after cleaning spaces: \n")                                                                  # str.replace('/', '_') replaces the / with _.
print(df_life.head().to_string())
print("\n")

print("   ✤ Missing Values ✤ ")
df_life = df_life.dropna(subset=['Life_expectancy'])
print("Shape dafaframe after droping missing rows of life_expentency : \n")
print(df_life.shape)

df_life['Adult_Mortality'].fillna(df_life['Adult_Mortality'].median)

df_life['Alcohol'] = df_life.groupby('Status')['Alcohol'].transform(lambda x: x.fillna(x.median()))
df_life['Alcohol'] = df_life['Alcohol'].fillna(df_life['Alcohol'].median())

df_life['Hepatitis_B'] = df_life.groupby('Status')['Hepatitis_B'].transform(lambda x: x.fillna(x.median()))
df_life['BMI'] = df_life.groupby('Status')['BMI'].transform(lambda x: x.fillna(x.median()))
df_life['BMI'] = df_life['BMI'].fillna(df_life['BMI'].median())

df_life['Polio'] = df_life.groupby('Country')['Polio'].transform(lambda x: x.fillna(x.median()))

df_life['Total_expenditure'] = df_life.groupby('Status')['Total_expenditure'].transform(lambda x: x.fillna(x.median()))

df_life['Diphtheria'] = df_life.groupby('Country')['Diphtheria'].transform(lambda x: x.fillna(x.median()))

df_life['GDP'] = df_life.groupby('Status')['GDP'].transform(lambda x: x.fillna(x.median()))
df_life['GDP'] = df_life['GDP'].fillna(df_life['GDP'].median())

df_life['Population'] = df_life.groupby('Status')['Population'].transform(lambda x: x.fillna(x.median()))
df_life['Population'] = df_life['Population'].fillna(df_life['Population'].median())
print("Columns in df_life:")
print(df_life.columns.tolist())
df_life['thinness__1-19_years'] = df_life['thinness__1-19_years'].fillna(df_life['thinness__1-19_years'].median())

df_life['thinness_5-9_years'] = df_life['thinness_5-9_years'].fillna(df_life['thinness_5-9_years'].median())

df_life['Income_composition_of_resources'] = df_life.groupby('Status')['Income_composition_of_resources'].transform(lambda x: x.fillna(x.median()))

df_life['Schooling'] = df_life.groupby('Status')['Schooling'].transform(lambda x: x.fillna(x.median()))
df_life['Schooling'] = df_life['Schooling'].fillna(df_life['Schooling'].median())

print("After filling all the columns , checking the null values \n ")
print("Missing values : " , df_life.isnull().sum())
print("Shape dafaframe after droping missing rows of life_expentency : \n")
print(df_life.shape)

print("   ✤ Encoding Data ✤ ")                                                                                              # str.strip() removes leading and trailing spaces.
LB_encod_status = LabelEncoder()
df_life['Status'] = LB_encod_status.fit_transform(df_life['Status'])                                                                       # column transformer do all the transformation in one line 
df_life['Status'].value_counts()
df_life.drop(columns=['Country'], inplace=True)
print("=============================================================================================================================================================================================\n")

print("\n                              – · • ✤ • · –  SPLITING DATA INTO X AND Y  – · • ✤ • · – ")
print("                              ===========================================================\n")
X = df_life.drop(columns=['Life_expectancy'])
y = df_life['Life_expectancy']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print("=============================================================================================================================================================================================\n")

print("\n                              – · • ✤ • · –  FEATURE SELECTION & ENGINEERING  – · • ✤ • · – ")
print("                              ===========================================================\n")
std_scaler = StandardScaler()
X_train_scaled = std_scaler.fit_transform(X_train)
X_test_scaled = std_scaler.transform(X_test)
print("=============================================================================================================================================================================================\n")


print("\n                              – · • ✤ • · –  APPLYING ALGORITHUMS  – · • ✤ • · – ")
print("                              ===========================================================\n")
lr = LinearRegression()
lr.fit(X_train_scaled, y_train)
print("=============================================================================================================================================================================================\n")

print("\n                              – · • ✤ • · –  PREDICTIONS  – · • ✤ • · – ")
print("                              ===========================================================\n")
y_pred = lr.predict(X_test_scaled)

print("=============================================================================================================================================================================================\n")

print("\n                              – · • ✤ • · –  MODEL EVALUATIONS  – · • ✤ • · – ")
print("                              ===========================================================\n")
mae  = mean_absolute_error(y_test, y_pred)
mse  = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2   = r2_score(y_test, y_pred)

print(f"MAE:  {mae:.3f}")
print(f"MSE:  {mse:.3f}")
print(f"RMSE: {rmse:.3f}")
print(f"R²:   {r2:.3f}")
print("=============================================================================================================================================================================================\n")

print("\n                              – · • ✤ • · –  OPTIMIZING MODEL  – · • ✤ • · – ")
print("                              ===========================================================\n")
plt.figure(figsize=(6,6))
sns.scatterplot(x=y_test, y=y_pred, alpha=0.6)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')  # 45° line
plt.xlabel("Actual Life Expectancy")
plt.ylabel("Predicted Life Expectancy")
plt.title("Actual vs Predicted Life Expectancy (Random Forest)")
plt.show()
print("=============================================================================================================================================================================================\n")
























