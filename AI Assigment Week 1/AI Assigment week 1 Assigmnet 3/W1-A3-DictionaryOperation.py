#Python Program to Check if a Key Exists in a Dictionary or Not[This is a Python Program to check 
#if a given key exists in a dictionary or not.] 

key = {
    'car' : "Honda" ,
    'brand' : "toyata" , 
    "year" : 78
}

check_key = input("Enter key to check : ")

for keys in key:
    if check_key == keys:
        print("Exist!!")
 
#Python Program to Add a Key-Value Pair to the Dictionary. The program takes a key-value pair 
#and adds it to the dictionary. 

new_key = input("Enter key : ")
new_value = input("Enter value : ")

key.update({new_key : new_value})
print(key)

#Python Program to Find the Sum of All the Items in a Dictionary The program takes a dictionary 
#and prints the sum of all the items in the dictionary. 

new_sum_dic = dict()

a = None
b = None

i = 0 
while i <= 3:
    a = input(f"ENTER {i}th key : ")
    b = input(f"ENTER {i}th value : ")
    new_sum_dic.update({ a : b})
    i += 1

print("Entered dictionary is : " ,new_sum_dic)
sum = 0

for i in new_sum_dic.values():
    sum = sum + int(i)

print("sum of all the values : " , sum)

#Python Program to Multiply All the Items in a Dictionary. The program takes a dictionary and 
#prints the sum of all the items in the dictionary.   

new_mul_dic = dict()

first_num = None
second_num = None

i = 0 
while i <= 3:
    first_num = input(f"ENTER {i}th key : ")
    second_num = input(f"ENTER {i}th value : ")
    new_mul_dic.update({ first_num : second_num})
    i += 1


print("Entered dictionary is : " , new_mul_dic)
mul = 1

for i in new_mul_dic.values():
    mul = mul * int(i)


print("multiplication of all the values : " , mul)

#Python Program to Create Dictionary that Contains Number. The program takes a number from 
#the user and generates a dictionary that contains numbers (between 1 and n) in the form 
#(x,x*x). 

new_end_dic = dict()
n = int(input("enter the ending number: "))

i = 0
id = 100
while i <= n:
    new_end_dic.update({id : i})
    i +=1
    id +=1

print("Printing data till now : " ,new_end_dic)

#Python Program to Concatenate Two Dictionaries. The program takes two dictionaries and 
#concatenates them into one dictionary.

fisrt_dic = dict()
second_dic = dict()

third = None
fourth = None

for i in range(0,2):
    third = input(f"first {i} key : ")
    fourth = input(f"first {i} value : ")
    fisrt_dic.update({third:fourth})


third = None
fourth = None
for i in range(0,2):
    third = input(f"second {i} key : ")
    fourth = input(f"second {i} value : ")
    second_dic.update({third:fourth})

print("First dic : " , fisrt_dic)
print("second dic : " , second_dic)

new_con_dict = dict()

# | between two dictionary makess it combines into new dictionary

diction = fisrt_dic | second_dic
print(diction)