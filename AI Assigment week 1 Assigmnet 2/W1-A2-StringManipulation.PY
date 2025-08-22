#String Manipulation 

#1. Write a program to create a new string made of an input string’s first, 
#middle, and last character.


User_string = input("Enter a string : ") 
while True:
    try:
        if not User_string or User_string.isdigit():
            raise ValueError
        break
    except ValueError:
        print("Invalid input . please enter string !")
    User_string = input("Enter a string : ")


count = len(User_string)

first = User_string[0]
last = User_string[-1]

mid = None
mid_index = count // 2
if count % 2 == 0:
    mid = User_string[mid_index-1] + User_string[mid_index]
elif count % 2 != 0:
    mid = User_string[mid_index-1] 

new_string = first + mid + last
print("New string : " , new_string)

#2. Write a program to count occurrences of all characters within a string Given. 

string = input("Enter a string : ")


temp_list = list(string)
name_of_character = []
no_of_character = []
temp_index = 0

for i in temp_list:
    if i not in name_of_character:
        name_of_character.insert(temp_index , i)
        temp_index+=1

string_cout = len(name_of_character) 
print(string_cout)
        

index = 0 
while index < string_cout:
    temp1 = name_of_character[index]
    no_of_character.insert(index , string.count(temp1))
    index+=1


for i in range(0 , string_cout):
    print("{} : {} ".format(name_of_character[i] , no_of_character[i]))


#3. Reverse a given string 

my_string = input("Enter a string : ")
count = len(my_string)
index = -1

while index >= -count:
    print(my_string[index] , end=" ")
    index-=1

#4. Split a string on hyphens 

before_spil_string = input("Enter a string : ")

after_split_string = before_spil_string.split('-')

print(after_split_string)

#5. Remove special symbols / punctuation from a string 

punctuation = '!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
punc_string = "Wow! She said, \"That's #awesome :) @everyone!"
temp_string = []

a = 0

for i in punc_string:
    if i not in punctuation and i != '"':
        temp_string.insert(a, i)
        a += 1

new_string = "".join(temp_string)
print(new_string)


