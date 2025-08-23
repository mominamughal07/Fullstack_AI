#Loop Manipulation 
#1. Print first 10 natural numbers using while.

i = 1

while i <= 10:
    print(i , end=" ")
    i+=1

#2.  Take Input from user , and print even number till that input number .

value = int(input("Enter a number : "))

for i in range(0 , value):
    if i % 2 == 0:
        print(i, end=" ")

#3. Take Input from user , and print odd number till that input number .

value = int(input("Enter a number : "))

for i in range(0 , value):
    if i % 2 != 0:
        print(i, end=" ")

#4. Take Input from user , and print prime number till that input number 

value = int(input("Enter a number : "))

for i in range(1 , value+1):
    if value % i == 0:
        print(i, end=" ")

#5  Print multiplication table of a given number 

value = int(input("Enter a number : "))

for i in range(1 , 10+1):
    print("{} * {} = {}".format(i , i , value*i))

