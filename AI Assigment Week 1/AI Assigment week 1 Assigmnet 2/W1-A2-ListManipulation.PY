# List Manipulation 
# 1.  Reverse a list in Python

shopping = ["milk", "bread", "eggs", "cheese"]
shopping1 = shopping[::-1]
print(shopping1)

 
# 2.  Turn every item of a list into its square 

list_simple = [2 , 3 ,4 ,5 , 6 ,7 , 8 , 9]

list_square = []

for i in list_simple:
    square = i*i
    list_square.append(square)

print("After Square list : " , list_square)

# 3.  Remove empty strings from the list of strings 

data = ["apple", "", "banana", "", "", "cherry", "date", ""]
count = len(data)

i = count - 1

while i > 0:
    if len(data[i]) == 0:
        del data[i]
    i-=1

print(data)
        
# 4. Add new item to list after a specified item 

animals = ["lion", "tiger", "elephant", "giraffe", "zebra"]

animals.insert(3 , "hippo")
print(animals)

# 5.  Replace list’s item with new value if found 

animal = ["lion", "tiger", "elephant", "giraffe", "zebra"]

find_value = input("Enter animal name to find : ")
replace_value = input("Enter animal name to replace : ")


index=0
for i in animal:
    if i == find_value:
        animal[index] = replace_value
        print(animal)
        break
    index+=1
 