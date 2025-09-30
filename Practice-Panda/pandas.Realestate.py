import pandas as pd 

# Load CSV
dataframe = pd.read_csv(r"Fullstack_AI\practice\RealEstate-USA.csv", delimiter=",")

# Display full DataFrame and info
print("Whole DataFrame:\n", dataframe)
print("\nData types of each column:\n", dataframe.dtypes)
print("\nSummary of rows, non-null values, columns data:\n", dataframe.info())

# LAST VALUES
print("\n           LAST VALUES")
print("Last 3 rows:\n", dataframe.tail(3))
print("Last 5 rows:\n", dataframe.tail(5))
print("Last 1 row:\n", dataframe.tail(1))

# FIRST VALUES
print("\n           FIRST VALUES")
print("First 1 row:\n", dataframe.head(1))
print("First 5 rows:\n", dataframe.head(5))
print("First 7 rows:\n", dataframe.head(7))

# STATISTICS
print("\n           ALL STATISTICS")
print("All statistics of DataFrame:\n", dataframe.describe())
print("Number of rows and columns:", dataframe.shape)

# COLUMN ACCESS
print("\n           COLUMN ACCESS")
print("Accessing single column 'city':\n", dataframe['city'])
print("Accessing multiple columns 'price' and 'city':\n", dataframe[['price', 'city']])

# USING .LOC (label-based)
print("\n       ACCESS ROWS USING .LOC")
print("Single row (second) using .loc:\n", dataframe.loc[1])
print("Multiple rows (first and sixth) using .loc:\n", dataframe.loc[[0,5]])
print("Multiple rows (fifth and fifteenth) using .loc:\n", dataframe.loc[[4,14]])

# SLICING USING .LOC
print("\n       SLICING USING .LOC")
print("Slicing from 1st to 7th row:\n", dataframe.loc[0:8]) 
print("Slicing from start to 6th row:\n", dataframe.loc[:5])
print("Slicing from 100th row to end:\n", dataframe.loc[100:])

# CONDITIONAL SELECTION USING .LOC
print("\n     CONDITIONAL SELECTION USING .LOC")
# Example: Select all rows where state is 'Puerto Rico'
state_data = dataframe.loc[dataframe['state'] == 'Puerto Rico']
print("Rows where state == 'Puerto Rico':\n", state_data)

# Specific rows and columns
print("Specific rows from 'city' column:\n", dataframe.loc[:2, 'city'])
print("Multiple columns for specific rows:\n", dataframe.loc[:4, ['brokered_by', 'status']])
print("Range of columns with specific rows:\n", dataframe.loc[3:6, 'brokered_by':'status'])
print("Condition on rows and columns:\n", dataframe.loc[dataframe['state']=='Puerto Rico', 'city':'status'])

dataframe11_loc = pd.read_csv(r"Fullstack_AI\practice\RealEstate-USA.csv" , index_col="brokered_by") 

print("\n     NEW DATAFRAME USING LOC with a primary key")
print("All of the dataframe : " , dataframe11_loc)
print("Data types of each column: " , dataframe11_loc.dtypes)
print("\nSummary of rows, non-null values, columns data:\n", dataframe11_loc.info())


print("Single row : " , dataframe11_loc.loc[103378])
print("Multiple rows : " , dataframe11_loc.loc[[103378 , 1205]])

