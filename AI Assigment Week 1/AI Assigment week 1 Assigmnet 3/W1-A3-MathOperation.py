#Python Program to Find the Area of a Triangle[The program takes three sides of a triangle and 
#prints the area formed by all three sides.]

base = float(input("Enter value of base : "))
height = float(input("Enter value of height : "))

area_of_triangle = (base * height) // 2

print("area of triangle : " , area_of_triangle)

#Python Program to Find Quotient and Remainder of Two Numbers[The program takes two 
#numbers and prints the quotient and remainder.]

print("Enter two number : ")
number1 = float(input())
number2 = float(input())

print("quotient : " , number1 // number2)
print("remainder : " , number1 % number2)

#Python Program to Print an Identity Matrix [The program takes a number n and prints an 
#identity matrix of the desired size.] 

n = int(input("Enter number: "))

matrix = []

for i in range(n):
    new = []
    for j in range(n):
        if i == j:
            new.append(1)
        else:
            new.append(0)
    matrix.append(new)

for row in matrix:
    print(new)


# Python Program to Find the LCM of Two Numbers [The program takes two numbers and prints 
#the LCM of two numbers.] 

list_of_num = list()

i = 0 
print("Enter two numbers : ")
while i < 2:
    list_of_num.append(int(input()))
    i+=1
print("LIST : " , list_of_num)

max_no = max(list_of_num)
print("Max number in list is : " , max_no )

a = 2
list3 = list()
b = list_of_num[0]
c = list_of_num[1]
while a <= max_no:
    if b % a == 0 and c % a == 0:
        b = b // a
        c = c // a
        list3.append(a)
    elif b % a == 0:
        b = b // a
        list3.append(a)
    elif c % a == 0:
        c = c // a
        list3.append(a)
    else:
         a += 1
   

print(list3)

LCM = 1

i = 0
while i < len(list3):
    LCM = LCM * list3[i]
    i+=1
    

print(f"LCM of {list_of_num[0]} and {list_of_num[1]} : " , LCM)

# Python Program to Find the Sum of Natural Numbers. [Write a program that takes the number 
#of terms and calculates the sum of the first N natural numbers.]
 
original_number = int(input("Enter a number : "))

i = 0
sum = 0
while i <= original_number:
    sum = sum + i

print("sum of all number is : "  , sum)

# Python Program to Find All Perfect Squares in the Given Range.

range_number = int(input("Enter a number to print perfect squres till that number : "))

i = 0 
square = 1
perfect_square = list()
while square < range_number:
    square = i * i
    perfect_square.append(square)
    i += 1

print(perfect_square)

# Python Program to Check Armstrong Number 
initial_number = input("Enter a number to check the armstrong : ")

len_of_num = len(initial_number)

number = list(initial_number)

i = 0
sum = 0
pow = None
sum = 0
while i < len_of_num:
    con_int = int(number[i])
    pow = con_int * con_int * con_int
    sum = sum + pow
    i += 1

if sum == int(initial_number):
    print("this is armstrong !")
else :
    print("this is not armstrong !")