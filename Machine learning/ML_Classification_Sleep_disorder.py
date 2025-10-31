import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import OrdinalEncoder
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import confusion_matrix, accuracy_score
np.set_printoptions(suppress=True)                                                                                                 # this is will later on fix the e values in confusion mats

df_Sleep_Disorder = pd.read_csv("C:\\Users\\Lenovo\\Documents\\GitHub\\Fullstack_AI\\Machine learning\\Data_sets\\Classifications\\Sleep_health_and_lifestyle_dataset.csv")

print("    >>>>  DATASET AS PANDAS DATAFRAME  <<<<  " )
print("          ---------------------------         ")
print(df_Sleep_Disorder)
print("---------------------------------------------------------------------------------------------------------------------------------\n")

print("    >>>>  EXPLORING THE DATA  <<<<  " )
print("          ------------------         ")                                                                                # Goal Here:
print("Shape of dataset : " , df_Sleep_Disorder.shape)                                                          
print("Info of dataset : " , df_Sleep_Disorder.info())                                                                        # Understand the columns
print("Head of dataset : \n" , df_Sleep_Disorder.head().to_string())                                                          # Identify which is the target (y) and which are inputs (X)       
print("Finding nulls of dataset : \n" , df_Sleep_Disorder.isnull().sum())                                                     # Spot issues: missing data, wrong types, or weird values
print("Finding Duplicates of dataset : \n" , df_Sleep_Disorder.duplicated().sum()) 
print("---------------------------------------------------------------------------------------------------------------------------------\n")

print("        >>>>  CLEANING THE DATA  <<<<  " )
print("              -----------------         ") 
print("\n....... Dropping the nunecessory columns ....... ")
print("        --------------------------------      ")
df_Sleep_Disorder = df_Sleep_Disorder.drop(columns=['Person ID'])                                                            # person id is of no use while identifying
print("After droping the person ID , the columns are : \n ")                                                                                      # since its not gona help identifying the sleep disorder                    
print(df_Sleep_Disorder.columns)      

print("\n....... Splitting the bp column since its have two saperate values ....... ")
print("        -----------------------------------------------------------      ")
df_Sleep_Disorder[['Systolic_BP' ,'Diastolic_BP']] = df_Sleep_Disorder['Blood Pressure'].str.split('/' , expand=True)        # adding two new coloumns to dataframe. spliting a column of BP and puting the values in two coloumns                                          
df_Sleep_Disorder = df_Sleep_Disorder.drop(columns=['Blood Pressure'])                                                       # person id is of no use while identifying
print(df_Sleep_Disorder.sample(5).to_string())

print("\n....... Filling the NaN values with none in sleepDisorder coloum ....... ")
print("        -----------------------------------------------------------      ")                                           
df_Sleep_Disorder['Sleep Disorder'].fillna('None' , inplace=True)                                                           # filling all the null values with 'none'
print(df_Sleep_Disorder.to_string())                                                                                        # to_string means show all the coloumns without ....
print(df_Sleep_Disorder['Sleep Disorder'].value_counts())

print("\n....... Converting the Sleep duration into integer colum ....... ")
df_Sleep_Disorder['Sleep Duration'] = df_Sleep_Disorder['Sleep Duration'].astype(int)                                       # since the sleep duration is in hours according to the
print("After changing data type of Sleep Duration column : \n " , df_Sleep_Disorder['Sleep Duration'])                      # dataset information then hours doesnt need to be in float            
print("        -----------------------------------------------------------      ")

print("    >>>>  Spliting data as train and test  <<<<  " )
print("          -------------------------------         ")
X = df_Sleep_Disorder[['Gender' , 'Age' , 'Occupation' , 'Sleep Duration' ,'Quality of Sleep' , 'Physical Activity Level' , 'Stress Level' , 'BMI Category' , 'Heart Rate' , 'Daily Steps' , 'Systolic_BP' , 'Diastolic_BP']]
Y = df_Sleep_Disorder['Sleep Disorder']
x_train , x_test , y_train , y_test = train_test_split(X , Y , test_size=0.8 , random_state=42 )
print("--------------------------------------------------------------------------------------------------------------------------------\n")

print("\n....... Encoding catagorical data into numaric data for machine to understand ....... ")
print("        -----------------------------------------------------------      ")

sleepDisorder_encoding = LabelEncoder()                                                                                     # make a encoder for y (target) column 
y_train = sleepDisorder_encoding.fit_transform(y_train)
y_test = sleepDisorder_encoding.transform(y_test)

colums_transform = ColumnTransformer(transformers=[                                                                         # column transformer do all the transformation in one line 
    ('ohe' , OneHotEncoder(sparse_output=False , drop='first' , handle_unknown='ignore') , ['Gender' , 'Occupation']) , 
    ('oe' , OrdinalEncoder(categories = [['Normal' , 'Normal Weight' , 'Obese' , 'Overweight']] ,  handle_unknown='use_encoded_value', unknown_value=-1) , ['BMI Category']),
    ('scaler', StandardScaler(), ['Age', 'Sleep Duration', 'Quality of Sleep', 'Stress Level',
                                      'Physical Activity Level', 'Heart Rate', 'Daily Steps',
                                      'Systolic_BP', 'Diastolic_BP'])
     ] , remainder='passthrough')                                                                                           # pass through means keepin all the other columnd as it is 
X_train_fit_trans = colums_transform.fit_transform(x_train)
X_test_Transform = colums_transform.transform(x_test)
column_names = colums_transform.get_feature_names_out()                                                                     # the above function will return a numpy array where all the columns names are also numeri so this will take the column names so later we can give it ti datafram
new_df_sleep = pd.DataFrame(X_train_fit_trans , columns=column_names)
print(new_df_sleep.head().to_string())

print("    >>>>  VISUALIZING THE DATA  <<<<  " )
print("          --------------------         ")
corr = new_df_sleep.corr(numeric_only=True)

plt.figure(figsize=(10, 6))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap — Numeric Features')
plt.show()


print("    >>>>  APPLIYING ALGORITHMS ON MODEL  <<<<  " )
print("          ----------------------------         \n")

print("LOGISTIC REGRESSION")
print("---  ---  ---  ---  --- ")  

Log_reg_mod = LogisticRegression()
Log_reg_mod.fit(X_train_fit_trans, y_train)

train_acc = Log_reg_mod.score(X_train_fit_trans, y_train)
test_acc = Log_reg_mod.score(X_test_Transform, y_test)

print("Train Accuracy:", train_acc)
print("Test Accuracy:", test_acc)
print("\n")

print("K-NEAREST NEIGHBOURS (KNN)")
print("---  ---  ---  ---  --- ")  

KNN_mod = KNeighborsClassifier(n_neighbors=3)
KNN_mod.fit(X_train_fit_trans, y_train)

train_acc_knn = KNN_mod.score(X_train_fit_trans, y_train)
test_acc_knn = KNN_mod.score(X_test_Transform, y_test)

print("Train Accuracy:", train_acc_knn)
print("Test Accuracy:", test_acc_knn)
print("\n")

print("SUPPORT VECTOR MACHINE (SVM)")
print("---  ---  ---  ---  --- ")  

svm_mod = SVC(kernel='rbf')
svm_mod.fit(X_train_fit_trans, y_train)

train_acc_svm = svm_mod.score(X_train_fit_trans, y_train)
test_acc_svm = svm_mod.score(X_test_Transform, y_test)

print("Train Accuracy:", train_acc_svm)
print("Test Accuracy:", test_acc_svm)
print("\n")

print("DECISION TREE CLASSIFIER")
print("---  ---  ---  ---  --- ")  

dt_mod = DecisionTreeClassifier(random_state=42)
dt_mod.fit(X_train_fit_trans, y_train)

train_acc_dt = dt_mod.score(X_train_fit_trans, y_train)
test_acc_dt = dt_mod.score(X_test_Transform, y_test)

print("Train Accuracy:", train_acc_dt)
print("Test Accuracy:", test_acc_dt)
print("\n")

print("RANDOM FOREST CLASSIFIER")
print("---  ---  ---  ---  --- ")  

rf_mod = RandomForestClassifier(n_estimators=100, random_state=42)
rf_mod.fit(X_train_fit_trans, y_train)

train_acc_rf = rf_mod.score(X_train_fit_trans, y_train)
test_acc_rf = rf_mod.score(X_test_Transform, y_test)

print("Train Accuracy:", train_acc_rf)
print("Test Accuracy:", test_acc_rf)
print("\n")

print("---------------------------------------------------------------------------------------------------------------------------------\n")

print("    >>>>  PREDICTION <<<<  " )
print("          ----------         \n")  

Log_reg_pred = Log_reg_mod.predict(X_test_Transform)
KNN_pred = KNN_mod.predict(X_test_Transform)
SVM_pred = svm_mod.predict(X_test_Transform)
Dec_tree_pred = dt_mod.predict(X_test_Transform)
Ran_forest_pred = rf_mod.predict(X_test_Transform)

print(f"\nPrediction through logistic regression: \n " , Log_reg_pred)
print(f"\nPrediction through KNN : \n " , KNN_pred)
print(f"\nPrediction through SVM : \n " , SVM_pred)
print(f"\nPrediction through Decision tree: \n " , Dec_tree_pred)
print(f"\nPrediction through Random forest : \n " , Ran_forest_pred)

print("    >>>>  CONFUSION MATRIX <<<<  " )
print("          ----------------         \n")  

con_matrix_LR = confusion_matrix(y_test , Log_reg_pred) 
con_matrix_KNN = confusion_matrix(y_test , KNN_pred) 
con_matrix_SVM = confusion_matrix(y_test , SVM_pred)
con_matrix_Dec_tree = confusion_matrix(y_test , Dec_tree_pred) 
con_matrix_Rnd_for = confusion_matrix(y_test , Ran_forest_pred)

print("\nLogistic Regression Confusion Matrix:\n", pd.DataFrame(con_matrix_LR))
print("\nKNN Confusion Matrix:\n", pd.DataFrame(con_matrix_KNN))
print("\nSVM Confusion Matrix:\n", pd.DataFrame(con_matrix_SVM))
print("\Decision tree Confusion Matrix:\n", pd.DataFrame(con_matrix_Dec_tree))
print("\Random forest Confusion Matrix:\n", pd.DataFrame(con_matrix_Dec_tree))

sns.heatmap(con_matrix_LR , annot=True)
plt.title("CONFIUSION MATRIX FOR LOGISTIC REGRESSION")
plt.show()

sns.heatmap(con_matrix_KNN , annot=True)
plt.title("CONFIUSION MATRIX FOR K-NEAREST NEIGHBOURS (KNN)")
plt.show()

sns.heatmap(con_matrix_SVM , annot=True)
plt.title("CONFIUSION MATRIX FOR SUPPORT VECTOR MACHINE (SVM)")
plt.show()

sns.heatmap(con_matrix_Dec_tree , annot=True)
plt.title("CONFIUSION MATRIX FOR DECISION TREE CLASSIFIER")
plt.show()

sns.heatmap(con_matrix_Rnd_for , annot=True)
plt.title("CONFIUSION MATRIX FOR RANDOM FOREST CLASSIFIER")
plt.show()
