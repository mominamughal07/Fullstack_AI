import pandas as pd
from sklearn.model_selection import train_test_split

data = {
    'Hours_Studied': [1,2,3,4,5,6,7,8,9,10],
    'Marks': [35,40,50,60,70,75,80,85,90,95]
}

print("ORIGINAL DATA : " , data)

data_as_tabular = pd.DataFrame(data)
print("Data as dataframe : " , data_as_tabular)

X = data_as_tabular['Hours_Studied']
Y = data_as_tabular['Marks']

print("X : " , X )
print("Y : " , Y )
print("-------------------------------------------------------------------------\n")


#Q1:

#Split the data with 80% train and 20% test.
#→ Print the length of X_train and X_test.
#now creating x and y to give it to funtion 


x_train , x_test , y_train , y_test = train_test_split(X , Y , test_size=0.2 , random_state=42)

print("      >>>    SPLITING 80% INTO TRAINING & 20% INTO TEST    <<<")
print("             ------------------------------------------           ")
print("len of x_train " , len(x_train))
print("x_train ")
print(x_train)
print("-------------------------------------------------------------------------\n")

print("len of y_train " , len(y_train))
print("y_train ")
print(y_train)
print("-------------------------------------------------------------------------\n")


print("len of x_test " , len(x_test))
print("x_test ")
print(x_test)
print("-------------------------------------------------------------------------\n")


print("len of y_test " , len(y_test))
print("y_test ")
print(y_test)
print("-------------------------------------------------------------------------\n")

#Q2:

#Use random_state=1, split again with test_size=0.3.
#→ Print which student indexes went to the test set.

x_train , x_test , y_train , y_test = train_test_split(X , Y , random_state=1 , test_size=0.3)

print("      >>>    RANDOM_STATE = 1 & TEST_SIZE = 0.3    <<<")
print("             ----------------------------------         ")

print("x_train ")
print(x_train)
print("-------------------------------------------------------------------------\n")

print("y_train ")
print(y_train)
print("-------------------------------------------------------------------------\n")

print("x_test ")
print(x_test)
print("-------------------------------------------------------------------------\n")

print("x_test ")
print(y_test)
print("-------------------------------------------------------------------------\n")

print("The index 1 in x has value of x_train is  ")
print("x_train[1]" , x_train[1])
print("The index 4 in y has value of y_train is  ")
print("y_train[4]" , y_train[4])
print("\n")

#🔹 Q3:

#Change the random_state to 2 (same test_size=0.3).
#→ Compare: Are the test samples same or different?

x_train , x_test , y_train , y_test = train_test_split(X , Y , random_state=2 , test_size=0.3)

print("      >>>    RANDOM_STATE = 2 & TEST_SIZE = 0.3    <<<")
print("             ----------------------------------         ")

print("x_train ")
print(x_train)
print("-------------------------------------------------------------------------\n")

print("y_train ")
print(y_train)
print("-------------------------------------------------------------------------\n")

print("x_test ")
print(x_test)
print("-------------------------------------------------------------------------\n")

print("x_test ")
print(y_test)
print("-------------------------------------------------------------------------\n")

print("random state 1 and random state 2 are results in different sets")
print("-------------------------------------------------------------------------\n")


#🔹 Q4:

#If you do not set any random_state,
#→ Run the same code twice and show if your train/test sets are same or not.

print("      >>>    WITHOUT SETTING ANY RANDOM STATE    <<<")
print("             --------------------------------         ")
x_train , x_test , y_train , y_test = train_test_split(X , Y , test_size=0.3 , random_state= False)

print("PRINTING TWO TIMES TO SEE IF THESE IS ANY DIFFERENCE ")
print("x_train ")
print(x_train)
print("-------------------------------------------------------------------------\n")

print("y_train ")
print(y_train)
print("-------------------------------------------------------------------------\n")

print("x_test ")
print(x_test)
print("-------------------------------------------------------------------------\n")

print("x_test ")
print(y_test)
print("-------------------------------------------------------------------------\n")

x_train , x_test , y_train , y_test = train_test_split(X , Y , test_size=0.3 , random_state=False)

print("x_train ")
print(x_train)
print("-------------------------------------------------------------------------\n")

print("y_train ")
print(y_train)
print("-------------------------------------------------------------------------\n")

print("x_test ")
print(x_test)
print("-------------------------------------------------------------------------\n")

print("x_test ")
print(y_test)
print("-------------------------------------------------------------------------\n")


#🔹 Q5:

#Use train_size=0.6 instead of test_size.
#→ How many samples go to training?

print("      >>>    SETTING TRAIN SIZE = 0.6 INSTEAD OF TEST SIZE   <<<")
print("             ---------------------------------------------         ")
x_train , x_test , y_train , y_test = train_test_split(X , Y , random_state=2 , train_size=0.6)

print("x_train ")
print(x_train)
print("-------------------------------------------------------------------------\n")

print("y_train ")
print(y_train)
print("-------------------------------------------------------------------------\n")

print("x_test ")
print(x_test)
print("-------------------------------------------------------------------------\n")

print("x_test ")
print(y_test)
print("-------------------------------------------------------------------------\n")


#🔹 Q6:

#Set shuffle=False and test_size=0.3.
#→ Which 3 samples go to the test set?

print("      >>>    SUFFLE = FALSE    <<<")
print("             --------------      ")

x_train , x_test , y_train , y_test = train_test_split(X , Y , random_state=2 , test_size=0.3 , shuffle=False)

print("Random state = 2 ")

print("x_train ")
print(x_train)
print("-------------------------------------------------------------------------\n")

print("y_train ")
print(y_train)
print("-------------------------------------------------------------------------\n")

print("x_test ")
print(x_test)
print("-------------------------------------------------------------------------\n")

print("x_test ")
print(y_test)
print("-------------------------------------------------------------------------\n")


#🔹 Q7:

#Use shuffle=True with same test_size=0.3 and random_state=42.
#→ Which 3 samples go to the test set now?

print("      >>>    SUFFLE = TRUE    <<<")
print("             --------------      ")

x_train , x_test , y_train , y_test = train_test_split(X , Y , random_state=2 , test_size=0.3 , shuffle= True)

print("x_train ")
print(x_train)
print("-------------------------------------------------------------------------\n")

print("y_train ")
print(y_train)
print("-------------------------------------------------------------------------\n")

print("x_test ")
print(x_test)
print("-------------------------------------------------------------------------\n")

print("x_test ")
print(y_test)
print("-------------------------------------------------------------------------\n")


#🔹 Q8:

#If your dataset is very small (only 5 rows) and you set test_size=0.8,
#→ How many samples will go to train and how many to test?

print("      >>>    SMALL DATA SET AND USE TEST SIZE = 0.8   <<<")
print("             --------------------------------------     ")

data2 = {
    'Hours_Studied': [10 , 34 , 45 , 48 , 23],
    'Marks': [90 , 101 , 23 , 89 , 3]
}

print("ORIGINAL DATA : " , data2)

data2_as_tabular = pd.DataFrame(data2)
print("Data as dataframe : " , data2_as_tabular)


X2 = data2_as_tabular['Hours_Studied']
Y2 = data2_as_tabular['Marks']

print("X2 : " , X2 )
print("Y2 : " , Y2 )
print("-------------------------------------------------------------------------\n")

x2_train , x2_test , y2_train , y2_test = train_test_split(X2 , Y2 , random_state=2 , test_size=0.8)


print("x2_train ")
print(x2_train)
print("-------------------------------------------------------------------------\n")

print("y2_train ")
print(y2_train)
print("-------------------------------------------------------------------------\n")

print("x2_test ")
print(x2_test)
print("-------------------------------------------------------------------------\n")

print("y2_test ")
print(y2_test)
print("-------------------------------------------------------------------------\n")
