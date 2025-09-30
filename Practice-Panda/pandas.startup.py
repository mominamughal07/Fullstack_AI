import pandas as pd 

dataframe = pd.read_csv("Startups in 2021 end.csv" , delimiter = "," ,  parse_dates=["Date Joined"], dayfirst=True )

print("whole datafram : " , dataframe)
print("data types of each colomn : " , dataframe.dtypes)
print("Summary of rows , non-null values , columns data : " , dataframe.info())

print("\n           LAST VALUES             ")
print("last 3 rows : " , dataframe.tail(3))
print("last 5 rows : " , dataframe.tail(5))
print("last 1 rows : " , dataframe.tail(1))

print("\n           First VALUES             ")
print("first 1 rows : " , dataframe.head(1))
print("first 5 rows : " , dataframe.head(5))
print("first 7 rows : " , dataframe.head(7))

print("\n           ALL STATISTICS             ")
print("All the statictic of dataframe : " , dataframe.describe())
print("No. of coloumns and row " , dataframe.shape)

print("\n           COLUMN ACCESS              ")
print("accessing single columns : ", dataframe['Country'])
print("accessing multiple columns : " , dataframe[['Valuation ($B)' , 'City']])

print("\n       ACCESS COLUMN USING .LOC       ") #loc picks data using primary key 
print("single row (seconf) using .loc : " , dataframe.loc[1])
print("multiple rows (first to 6th) using .loc : " , dataframe.loc[[0 , 5]])
print("multiple rows (5 to 15) using .loc : " , dataframe.loc[[4 , 14]])


print("\n       SLICING USING .LOC       ")
print("sclicing from 1st to 9th row : " , dataframe.loc[0:8])
print("sclicing from starting to 6th row : " , dataframe.loc[:5])
print("sclicing from 100 to end row : " , dataframe.loc[100:])

print("\n     CONDITIONAL SELECTION USING .LOC       ")
a = dataframe.loc[dataframe['Country'] == 'China']
print("Specific data : " , a)
print("printing specific rows from a column : ", dataframe.loc[:2 , 'City'])
print("multiple columns with spcfic rows : " , dataframe.loc[:4 ,['Company' , 'Industry']])
print("range of coloumns with specific rows : " , dataframe.loc[3:6 , 'Company' : 'Industry'])
print("condition on row and  coulmns : "  ,dataframe.loc[dataframe['Country'] == 'China' , 'Date Joined' : 'Industry'  ] )

