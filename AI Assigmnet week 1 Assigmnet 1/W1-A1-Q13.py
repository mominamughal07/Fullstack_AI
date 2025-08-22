#Sum of First N Natural Numbers 
#Input a number n, calculate sum of first n natural numbers. 

n = int(input("Enter a number : "))
sum = 0
for i in range(0,n):
    sum = sum + i 

print(sum)