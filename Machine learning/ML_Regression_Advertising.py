import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import matplotlib.pyplot as plt


df_Advertising = pd.read_csv("C:\\Users\\Lenovo\\Documents\\GitHub\\Fullstack_AI\\Machine learning\\Data_sets\\Regression\\advertising.csv")

print("\n                              – · • ✤ • · –  DATASET AS PANDAS DATAFRAME  – · • ✤ • · – ")
print("                              ===========================================================\n")
print(df_Advertising)
print("=============================================================================================================================================================================================\n")

print("\n                              – · • ✤ • · –  EXPLORING DATAFRAME  – · • ✤ • · – ")
print("                              ===========================================================\n")

print(f"Shape of the dataset : {df_Advertising.shape}")
print(f"Coloumns of dataset : {df_Advertising.columns}")
print(f"Info of dataset : \n{df_Advertising.info()}")
print(f"First 7 rows of dataset : \n {df_Advertising.head()}")
print(f"Ramdon 7 rows of dataset : \n {df_Advertising.sample()}")
print(f"Missing rows of dataset : {df_Advertising.isnull().sum()}")
print(f"Duplicate rows of dataset : {df_Advertising.duplicated().sum()}")
print(f"Stats of dataset : \n {df_Advertising.describe()}")
print(f"shape of dataset : \n {df_Advertising.shape}")

print(df_Advertising.corr())

print("=============================================================================================================================================================================================\n")


print("\n                              – · • ✤ • · –  VISUALIZING – · • ✤ • · – ")
print("                              ===========================================================\n")
plt.figure(figsize=(6,4))
sns.heatmap(df_Advertising.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()

features = ['TV', 'Radio', 'Newspaper']

for col in features:
    plt.figure(figsize=(5,4))
    sns.scatterplot(x=df_Advertising[col], y=df_Advertising['Sales'])
    plt.title(f"{col} vs Sales")
    plt.xlabel(col)
    plt.ylabel("Sales")
    plt.show()

print("=============================================================================================================================================================================================\n")

print("\n                              – · • ✤ • · –  SPLITING DATA INTO X AND Y  – · • ✤ • · – ")
print("                              ===========================================================\n")

X = df_Advertising[['TV', 'Radio', 'Newspaper']]
y = df_Advertising['Sales']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print("                              ===========================================================\n")

print("\n                              – · • ✤ • · – SCALING  – · • ✤ • · – ")
print("                              ===========================================================\n")

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
print("                              ===========================================================\n")

print("\n                              – · • ✤ • · – APPLYING ALGORITHUM   – · • ✤ • · – ")
print("                              ===========================================================\n")
model = LinearRegression()
model.fit(X_train_scaled, y_train)
print("                              ===========================================================\n")

print("\n                              – · • ✤ • · – PREDICTIONS  – · • ✤ • · – ")
print("                              ===========================================================\n")
y_pred = model.predict(X_test_scaled)

print("                              ===========================================================\n")

print("\n                              – · • ✤ • · – EVALUATIION  – · • ✤ • · – ")
print("                              ===========================================================\n")
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print(f"MAE: {mae:.2f}")
print(f"MSE: {mse:.2f}")
print(f"RMSE: {rmse:.2f}")
print(f"R² Score: {r2:.2f}")

print("                              ===========================================================\n")

print("\n                              – · • ✤ • · – VISUALLIZATION AFTER TRAINING  – · • ✤ • · – ")
print("                              ===========================================================\n")
plt.figure(figsize=(6, 4))
plt.scatter(y_test, y_pred, color='blue', alpha=0.6)
plt.xlabel("Actual Sales")
plt.ylabel("Predicted Sales")
plt.title("Actual vs Predicted Sales (Linear Regression)")
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color='red')  # perfect line
plt.show()
print("                              ===========================================================\n")

accuracy = r2_score(y_test, y_pred)
print(f"Model Accuracy (R²): {accuracy*100:.2f}%")


