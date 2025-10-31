import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix

df_iris = pd.read_csv("C:\\Users\\Lenovo\\Documents\\GitHub\\Fullstack_AI\\Machine learning\\Data_sets\\Classifications\\iris.csv")

print("    >>>>  DATASET AS PANDAS DATAFRAME  <<<<  " )
print("          ---------------------------         ")
print(df_iris)
print("---------------------------------------------------------------------------------------------------------------------------------\n")

print("    >>>>  SPLITING THE DATA INTO X AND Y  <<<<  " )
print("          ------------------------------         ")
X = list()
X = df_iris[['sepal_length' , 'sepal_width' , 'petal_length' , 'petal_width' ]]
Y = df_iris['species']

print(f" X : \n{X} ")
print(f" Y : \n{Y} ")
print("---------------------------------------------------------------------------------------------------------------------------------\n")

print("    >>>>  EXPLORING THE DATA  <<<<  " )
print("          ------------------         ")                                                                                # Goal Here:
print(f"Shape of dataset : {df_iris.shape} \n")                                                          
print(f"Info of dataset : \n {df_iris.info()} \n")                                                                          # Understand the columns
print(f"Head of dataset :  \n {df_iris.head()} \n")                                                                         # Identify which is the target (y) and which are inputs (X)
print(f"samples of dataset :  \n {df_iris.sample(7)} \n")                                                                   # sample will pick uf sum random rows this will show whiuch type of data come acriss random rows        
print(f"Finding nulls of dataset : {df_iris.isnull().sum()}\n")                                                             # Spot issues: missing data, wrong types, or weird values
print(f"Finding Duplicates of dataset : {df_iris.duplicated().sum()} \n" ) 
print(f"Mathematical calculations of each column of dataset : \n{df_iris.describe()} \n" )                                  # count , mean , std , min , max , all the statistical data 
#print(f"correlation between each of the coloum with all other column : \n {df_iris.corr()} \n" ) 

print("---------------------------------------------------------------------------------------------------------------------------------\n")

print("    >>>>  PREPROCESSING DATA AND SCALLING  <<<<  " )
print("          ------------------         \n")  
print("Removing duplicates : ")
print("-------    -------   -----      ")  
df_iris = df_iris.drop_duplicates()
print("After removing the duplicates ")
print(f"Finding Duplicates of dataset : {df_iris.duplicated().sum()} \n" ) 

print("Encoding catagorical data into numerical data : ")
print("-------------        -------------       -------------         ")  
specie_encode = LabelEncoder()
df_iris['species'] = specie_encode.fit_transform(df_iris['species'])
print(f"After encoding species coloum is :\n {df_iris['species'].to_string()} \n ")
print(f"All the catagories number of spicie : \n {df_iris['species'].value_counts()} \n ")

print("Standerdizaton of all columns  : ")
print("-------------        -------------       -------------         ")  
scaling = StandardScaler()
X = scaling.fit_transform(X)

print("First 7 rows of X after scaling : \n" , X[:7])
print("\n")

print("---------------------------------------------------------------------------------------------------------------------------------\n")

print("    >>>>  VISUALIZING THE DATA  <<<<  " )
print("          --------------------         ")   
print("\nCount plot on sspecies to know must percentage each species holds : \n")
sns.countplot(x='species' , data=df_iris , color='tomato')
plt.title("Number of each species")
plt.show()

print("Scatter Plot: Petal Length vs Petal Width")
print("see how different flowers are grouped based on their petal measurements\n")
sns.scatterplot(x= 'petal_length' , y = 'petal_width' , data=df_iris , hue="species")
plt.title("Petal Length vs Petal Width")
plt.xlabel("Petal Length (cm)")
plt.ylabel("Petal Width (cm)")
plt.show()

correlations = df_iris.corr()
plt.figure(figsize=(10, 6))
sns.heatmap(correlations, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()
print("---------------------------------------------------------------------------------------------------------------------------------\n")


print("    >>>>  TRAIN-AND-TEST MODEL  <<<<  " )
print("          --------------------         \n")  

x_train , x_test , y_train , y_test = train_test_split(X , Y , test_size=0.8 , random_state= 42 )
print(f"Testing size of x : {x_test.shape}")
print(f"Testing size of Y : {y_test.shape}")
print(f"Training size of x : {x_train.shape}")
print(f"Training size of y : {y_train.shape}")
print("---------------------------------------------------------------------------------------------------------------------------------\n")

print("    >>>>  APPLIING ALGORITHMS ON MODEL  <<<<  " )
print("          ----------------------------         \n")  

print("LOGISTIC REGRESSION")
print("---  ---  ---  ---  --- ")  

Log_reg_mod = LogisticRegression()
Log_reg_mod.fit(x_train , y_train)

print("Accuracy of both training and testing sets .")
train_acc = Log_reg_mod.score(x_train, y_train)
test_acc = Log_reg_mod.score(x_test, y_test)

print("Train Accuracy:", train_acc)
print("Test Accuracy:", test_acc)
print("\n")

print("K-NEAREST NEIGHBOURS (KNN) ")
print("---  ---  ---  ---  --- ")  

KNN_mod = KNeighborsClassifier(n_neighbors=3)
KNN_mod.fit(x_train , y_train)

train_acc_knn = KNN_mod.score(x_train, y_train)
test_acc_knn = KNN_mod.score(x_test, y_test)

print("KNN Train Accuracy:", train_acc_knn)
print("KNN Test Accuracy:", test_acc_knn)
print("\n")

print("K-NEAREST NEIGHBOURS (KNN) ")
print("---  ---  ---  ---  --- ")  
svm_mod = SVC(kernel='rbf')

svm_mod.fit(x_train , y_train)

train_acc_svm = svm_mod.score(x_train , y_train)
test_acc_svm = svm_mod.score(x_test , y_test)


print("SVM Train Accuracy:", train_acc_svm)
print("SVM Test Accuracy:", test_acc_svm)
print("\n")
print("---------------------------------------------------------------------------------------------------------------------------------\n")

print("    >>>>  PREDICTION <<<<  " )
print("          ----------         \n")  

Log_reg_pred = Log_reg_mod.predict(x_test)
KNN_pred = KNN_mod.predict(x_test)
SVM_pred = svm_mod.predict(x_test)

print(f"\nPrediction through logistic regression: \n " , Log_reg_pred)
print(f"\nPrediction through KNN : \n " , KNN_pred)
print(f"\nPrediction through SVM : \n " , SVM_pred)


print("    >>>>  CONFUSION MATRIX <<<<  " )
print("          ----------------         \n")  

con_matrix_LR = confusion_matrix(y_test , Log_reg_pred) 
con_matrix_KNN = confusion_matrix(y_test , KNN_pred) 
con_matrix_SVM = confusion_matrix(y_test , SVM_pred) 

print("\n Confusion Matrix of LR : \n" , con_matrix_LR)
print("\n Confusion Matrix of KNN : \n" , con_matrix_KNN)
print("\n Confusion Matrix of SVM : \n" , con_matrix_SVM)

print("\nLogistic Regression Confusion Matrix:\n", pd.DataFrame(con_matrix_LR))
print("\nKNN Confusion Matrix:\n", pd.DataFrame(con_matrix_KNN))
print("\nSVM Confusion Matrix:\n", pd.DataFrame(con_matrix_SVM))

sns.heatmap(con_matrix_LR , annot=True)
plt.title("CONFIUSION MATRIX FOR LOGISTIC REGRESSION")
plt.show()