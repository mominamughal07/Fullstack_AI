#String manipulation: 
# Python Program to Check if a String is a Pangram or Not [The program takes a string and checks 
# if it is a pangram or not.] 

# Python Program to Check if a String is a Pangram or Not [The program takes a string and checks 
# if it is a pangram or not.] 
import string as s

letters = set()
alpha = s.ascii_lowercase

stringing = str(input("Input a sentence = "))
stringing = stringing.casefold()
stringing = stringing.replace(" " , "")
count = 0

while True:
    if stringing.isalpha() == False:
        print("Input error ! ")
        stringing = str(input("please enter a sentence containing only alpphabet : "))
    else:
        for ltrA in alpha:
            for ltrB in stringing:
                if ltrB == ltrA:
                    letters.add(ltrA)
                    break

        break

print(letters)

if len(letters) == 26:
    print("is pangram !")
else:
    print("is not pangram !")


#Python Program to Replace Every Blank Space with Hyphen in a String[The program takes a 
# string and replaces every blank space with a hyphen.] 

tringing_2 = str(input("Input a sentence = "))
stringing_2 = stringing_2.replace(" " , "-" )

print(stringing_2)

#This is a Python Program to display which letters are in the two strings but not in both. 

fst_str = str(input("Enter first string: "))
snd_str = str(input("Enter second string: "))

fst_str = fst_str.replace(" ", "")
snd_str = snd_str.replace(" ", "")

fst_set = set(fst_str)
snd_set = set(snd_str)

print("after removing duplicates:", fst_set)
print("after removing duplicates:", snd_set)

new_str = fst_set.symmetric_difference(snd_set)

print("Letters in one string but not both:", new_str)

#Python Program to Find the Larger String without using Built-in Functions[The program takes in 
#two strings and display the larger string without using built-in function.] 

#Python Program to Find the Larger String without using Built-in Functions[The program takes in 
#two strings and display the larger string without using built-in function.] 

string_1 = str(input("Enter First String : "))
string_2 = str(input("Enter second String : "))

len_str1 = 0
len_str2 = 0 

for char in string_1:
    len_str1 = len_str1 + 1

for char in string_2:
    len_str2 = len_str2 + 1

if len_str1 > len_str2:
    print("{} is larger then {}".format(string_1 , string_2))
elif len_str2 > len_str1:
    print("{} is larger then {}".format(string_2 , string_1))
else:
    print("Both are equal ! ") 

#Python Program to Count Number of Uppercase and Lowercase Letters in a String[The program 
#takes a string and counts the number of lowercase letters and uppercase letters in the string.]

import string as s 

upper = s.ascii_uppercase
lower = s.ascii_lowercase

count_uppercase = 0
count_lowercase = 0
str_3 = str(input("Enter string: "))
str_3 = str_3.replace(" " ,"")

for char in str_3:
    for char2 in upper:
        if char2 == char:
            count_uppercase+=1

for char in str_3:
    for char2 in lower:
        if char2 == char:
            count_lowercase+=1


print("Upper case letters : " , count_uppercase)
print("Upper lower letters : " , count_lowercase)

#Python Program to Check if Two Strings are Anagram. [An anagram in Python is a pair of strings 
#that have the same characters, but in a different order. It involves rearranging the letters of one 
#string to form the other.] 

str_4 = str(input("Enter First string: "))
str_5 = str(input("Enter second string: "))

str_4 = str_4.replace(" " ,"")
str_5 = str_5.replace(" " ,"")

str_4 = str_4.casefold()
str_5 = str_5.casefold()

str_4 = set(str_4)
str_5 = set(str_5) 

dif_str_4_to_5 = str_4.symmetric_difference(str_5)
dif_str_5_to_4 = str_5.symmetric_difference(str_4)

if len(str_4) != len(str_5):
    print("is Not Anagram ! ")
else:
    if len(dif_str_4_to_5) == 0 and len(dif_str_5_to_4) == 0:
        print("Is Anagram ! ")
    else:
        print("IS not Anagram ! ")


#Python Program to Check if the Substring is Present in the Given String. [The program takes a 
#string and checks if a substring is present in the given string.] 

original_string = str(input("Enter a String : "))
sub_string = str(input("Enter sub String : "))

if sub_string in original_string:
    print("Present !")
else:
    print("Absent ! ")

#Python Program to Print All Permutations of a String in Lexicographic Order without Recursion. 
#The problem is the display all permutations of a string in lexicographic or dictionary order. 


#Python Program to Calculate the Length of a String Without using Library Functions.[ The 
#program takes a string and calculates the length of the string without using library functions


i_string = str(input("Enter a String : "))

count = 0
for i in i_string:
    count+=1

print("Length of string is : " , count)

#Python Program to Create a New String Made up of First and Last 2 Characters. The program 
#takes a string and forms a new string made of the first 2 characters and last 2 characters from a 
#given string.

initial_string = str(input("Enter a String : "))
final_string = initial_string[0:2:] + initial_string[-2::]
print(final_string)

