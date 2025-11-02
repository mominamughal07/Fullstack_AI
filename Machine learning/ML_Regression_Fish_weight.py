import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler



print("    >>>>  DATASET AS PANDAS DATAFRAME  <<<<  " )
print("          ---------------------------         ")
df_Fish = pd.read_csv('C:\\Users\\Lenovo\\Documents\\GitHub\\Fullstack_AI\\Machine learning\\Data_sets\\Regression\\Fish[1].csv')
print("\n" , df_Fish)
print("---------------------------------------------------------------------------------------------------------------------------------\n")


print("    >>>>  EXPLORING AND ANALYSIZING DATA  <<<<  " )
print("          ------------------------------         ")
print(f"Shape of the dataset : {df_Fish.shape}")
print(f"Coloumns of dataset : {df_Fish.columns}")
print(f"Info of dataset : \n{df_Fish.info()}")
print(f"First 7 rows of dataset : \n {df_Fish.head()}")
print(f"Ramdon 7 rows of dataset : \n {df_Fish.sample()}")
print(f"Missing rows of dataset : {df_Fish.isnull().sum()}")
print(f"Duplicate rows of dataset : {df_Fish.duplicated().sum()}")
print(f"Stats of dataset : \n {df_Fish.describe()}")
print(f"shape of dataset : \n {df_Fish.shape}")

print("--------------------------------------------------------------------------------------------------------------------------\n")

print("    >>>>  SPLIITING DATASET INTO TRAIN AND TEST  <<<<  " )
print("          -------------------------------------         ")

X = df_Fish[['Species' , 'Length1' , 'Length2' , 'Length3' , 'Height' , 'Width']]
y = df_Fish['Weight']

x_train , x_test , y_train , y_test = train_test_split(X , y , test_size=0.2 , random_state= 42)
print("X_Train : \n " , x_train)
print("Y_Train : \n " , y_train)
print("X_Test : \n " , x_test)
print("y_Test : \n " , y_test)
print("--------------------------------------------------------------------------------------------------------------------------\n")

print("    >>>>  ENCODING DATA  <<<<  " )
print("          -------------------         ")
lable_encodr = LabelEncoder()
x_train['Species'] = lable_encodr.fit_transform(x_train['Species'])
x_test['Species'] = lable_encodr.transform(x_test['Species'])

print("Y_train : \n" , y_train)
print("Y_test : \n " , y_test)
print("--------------------------------------------------------------------------------------------------------------------------\n")

print("    >>>>  SCALING DATA  <<<<  " )
print("          ------------       ")
scale_x = StandardScaler()
x_train = scale_x.fit_transform(x_train)
x_test = scale_x.transform(x_test)

print("After scaling x train : \n " , x_train)
print("After scaling x test : \n " , x_test)
print("--------------------------------------------------------------------------------------------------------------------------\n")

print("    >>>>  VISUALIZING THE DATA  <<<<  " )
print("          --------------------         ")  

x_list = X.drop('Species', axis=1)
y_list = y

for col in x_list.columns:
    plt.figure(figsize=(6, 4))
    sns.scatterplot(x=x_list[col], y=y_list, hue=X['Species'])
    plt.title(f'{col} vs. Weight (by Species)')
    plt.xlabel(col)
    plt.ylabel('Weight')
    plt.show()
print("--------------------------------------------------------------------------------------------------------------------------\n")

print("    >>>>  APPLIING ALGORITHMS ON MODEL  <<<<  " )
print("          ----------------------------         \n")  

linReg_mod = LinearRegression()
linReg_mod.fit(x_train , y_train)

train_acc = linReg_mod.score(x_train , y_train)
test_acc = linReg_mod.score(x_test , y_test)
print("train_acc : " , train_acc )
print("test_acc : " , test_acc )
print("--------------------------------------------------------------------------------------------------------------------------\n")

print("    >>>>  PREDICTION  <<<<  " )
print("          ----------         \n")  
y_predic = linReg_mod.predict(x_test)
print(y_predic)
print("--------------------------------------------------------------------------------------------------------------------------\n")

print("    >>>>  VISUALIZATION  <<<<  " )
print("          -------------         \n")  

plt.scatter(y_test, y_predic)
plt.xlabel("Actual Values")
plt.ylabel("Predicted Values")
plt.title("Actual vs Predicted")
plt.show()

print("    >>>>  EVALUATION  <<<<  " )
print("          -------------         \n") 

MAE = mean_absolute_error(x_test , y_predic)
print("Mean absolute error : " , MAE)

MSE = mean_squared_error(x_test , y_predic)
print("Mean squared error : " , MSE)


