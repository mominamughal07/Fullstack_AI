# This is a Python Program to find the largest number in a list. The program takes a list and prints 
#the largest number in the list.

first_list = list()

print("Print any 10 digits in it :")
i = 0 
while i < 10 :
    first_list.append(input())
    i += 1

maximum_number = max(first_list)
print("Maximum number in list : ", maximum_number)

# The program takes a list and prints the largest number in the list. The program takes a list and 
#prints the second largest number in the list.

second_list = list()

print("Print any 10 digits in it :")
i = 0 
while i < 10 :
    second_list.append(input())
    i += 1

print("largets number in this list is : " , max(second_list))

second_list.sort()
print("Second larget number in list is : " , second_list[-2])

# Python Program to Print Largest Even and Largest Odd Number in a List. The program takes in a 
#list and prints the largest even and largest off number in it.  

even_list = list()
odd_list = list()

third_list = list()

print("Print any 10 digits in it :")
i = 0 
while i < 10 :
    third_list.append(int(input()))
    i += 1

i = 0 
while i < 10:
    if third_list[i] % 2 == 0 :
        even_list.append(third_list[i])
    elif third_list[i] % 2 != 0 :
        odd_list.append(third_list[i])
    i += 1

print(f"Largest even no. : {max(even_list)} \nlargest odd no. : {max(odd_list)}")


# Python Program to Find Average of a List. The program takes the elements of the list one by one 
#and displays the average of the elements of the list. 


Fourth_list = list()

print("Print any 10 digits in it :")
i = 0 
while i < 10 :
    Fourth_list.append(int(input()))
    i += 1

average = None
sum = 0 
i = 0 
while i < 10 :
    sum = sum + Fourth_list[i]
    i += 1

average = sum / len(Fourth_list)

print(f"Average of list is {average}")


# Python Program to Count Occurrences of Element in List. The program takes a number and 
#searches the number of times the particular number occurs in a list. 

fifth_list = [16 , 0 , 17 , 8 , 4 , 1 , 7, 10 , 14 , 1 , 20 , 2 , 16 , 5 , 20 , 10 , 14 , 9 , 16 , 7 , 5 , 11 , 14 , 7, 3 , 5 , 6 , 20 , 1, 12 , 19 , 13 , 18 , 1 , 15 , 10 , 7]

no = int(input("Enter a number between 0 to 20 to find occurance in list : " ))

print(f"The occurance of {no} in list is {fifth_list.count(no)} times ")


# Python Program to Remove Duplicates from a List. The program takes a lists and removes the 
#duplicate items from the list. 

sixth_list = [13 , 5 , 7 , 16 , 19 , 13 , 8 , 5 , 0 , 5 , 17 , 8 , 19 , 19 , 8 , 5 , 4 , 1 , 13 , 5 , 8 , 19 , 7 , 5 , 0 , 7, 10 , 8 , 7 , 13 , 14 , 19 , 1 , 20  , 5 , 0 , 2 , 19 , 8 , 5 , 13 ,  7 , 13  ,16 , 19 , 7 ,5 , 5 , 5 , 20 , 19 , 1 , 8 , 13 , 10 , 7 , 14 , 19 , 13 , 5 , 9 , 0 , 7 , 8 , 19 , 19 , 16 , 5 , 13 , 5, 7 , 13 , 7 , 5 , 19 , 1 , 7 , 11 , 5 , 13 , 14 , 7, 3 , 5 , 7 , 13 , 5 ,  6 , 7 , 5, 0 , 20 , 1, 7 , 12 , 5  , 1 , 13 , 5 ,19 , 13 , 7 , 13 , 18 , 5 , 1 , 15 , 10 , 1 , 7,7]

print("Original list is : " , sixth_list)
remove_duplicate = set(sixth_list)
print("After removeeing duplicate : " , remove_duplicate)

# Python Program to Find the Number Occurring Odd Number of Times in a List. A list is given in 
#which all elements except one element occurs an even number of times. The problem is to find 
#the element that occurs an odd number of times. 

seventh_list = [13 , 5 , 7 , 16 , 19 , 13 , 8 , 5 , 0 , 5 , 17 , 8 , 19 , 19 , 8 , 5 , 4 , 1 , 13 , 5 , 8 , 19 , 7 , 5 , 0 , 7, 10 , 8 , 7 , 13 , 14 , 19 , 1 , 20  , 5 , 0 , 2 , 19 , 8 , 5 , 13 ,  7 , 13  ,16 , 19 , 7 ,5 , 5 , 5 , 20 , 19 , 1 , 8 , 13 , 10 , 7 , 14 , 19 , 13 , 5 , 9 , 0 , 7 , 8 , 19 , 19 , 16 , 5 , 13 , 5, 7 , 13 , 7 , 5 , 19 , 1 , 7 , 11 , 5 , 13 , 14 , 7, 3 , 5 , 7 , 13 , 5 ,  6 , 7 , 5, 0 , 20 , 1, 7 , 12 , 5  , 1 , 13 , 5 ,19 , 13 , 7 , 13 , 18 , 5 , 1 , 15 , 10 , 1 , 7,7]

lenght_of_7th_list = len(seventh_list)
i = 0

print("Numbers that have odd occurance are : ")
while i < lenght_of_7th_list:
    if seventh_list.count(i) % 2 != 0 :
        print(f"Number {seventh_list[i]} have {seventh_list.count(i)} times occurance : ")
    i += 1

# Python Program to Find the Union of Two Lists. The program takes two lists and finds the unions 
#of the two lists. 

list1 = [19 , 6 , 4 , 1 , 13 , 3]
list2 = [14 , 17 , 0 , 2 , 18 , 3]

list1.extend(list2)

print(list1)


# Python Program to Swap the First and Last Element in a List. Python Program to Swap the First 
#and Last Element in a List 

new_eights_list = [19, 6, 4, 1, 13, 3, 14, 17, 0, 2, 18, 3]

a = new_eights_list[0]
b = new_eights_list[-1]
new_eights_list[0] = b
new_eights_list[-1] = a

print("after swaping : " , new_eights_list)

# Python Program to Return the Length of the Longest Word from the List of Words. The program 
#takes a list of words and returns the word with the longest length. 

ninth_list = ['an', 'hit ', 'farazh' , 'monopoli' , 'seventeen' , 'hiba' , 'momina' ,'seven' ,'a']

print(f"Longest word is {max(ninth_list)} with lenght of {len(max(ninth_list))} ")