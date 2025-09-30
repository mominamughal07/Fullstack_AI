#Tuple Manipulation 
# 1. Reverse the tuple

data = ("John", 25, 5.9, True, None, "student")

reversed_data = data[::-1]

print(reversed_data)


# 2. Access value 20 from the tuple 

numbers = (10, 20, 30, 40, 50, 60)
count = len(numbers)
index = 0 
while index < count:
    if numbers[index] == 20:
        print("Index : {} \nValue : {}".format(index , numbers[index]))
    index+=1

# 3. Swap two tuples in Python 

house_items = ("sofa", "lamp", "bed", "fridge", "shower", "door")
colors = ("red", "blue", "green", "yellow", "purple", "orange")

temp = house_items
house_items = colors
colors = temp

print("house hold : " , house_items)
print("colors : " , colors)
