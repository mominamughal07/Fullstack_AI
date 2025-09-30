#variable declartion
print("         ______________________") 
print("        | VARIABLE DECLARATION |")
print("        ") 
h = 34 
f = 2.8
s = "Momina"
print("------------------------------------------")

#printing variables
print("          PRINTING VARIBAES")
print(f"Integer : {h}")
print(f"Float : {f}")
print(f"String : {s}")
print("------------------------------------------")
print("\n")

#types
print("          PRINTING TYPES")
print("Type of h : " ,type(h))
print("Type of f : " ,type(f))
print("Type of s : " ,type(s))
print("------------------------------------------")
print("\n")

#input 
print("          INPUT")
a = int(input("Enter a number : "))
print(f"The number you typed id : {a}. \nIts type is : {type(a)}.")
print("------------------------------------------")
print("\n")

#arithmatic functions 
print("          ARITHMATIC FUNTIONS ")

mul = h * f
div = h // f
mod = h % f 
sub = h - f
add = h + f 
print(f"Multiplication of {h} and {f} : {mul}.")
print(f"Division of {h} and {f} : {div}.")
print(f"Modulus of {h} and {f} : {mod}.")
print(f"Subtarction of {h} and {f} : {sub}.")
print(f"Addition of {h} and {f} : {add}.\n")

print(f"Type of multiplication : {type(mul)}.")
print(f"Type of division : {type(div)}.")
print(f"Type of Modulud  : {type(mod)}.")
print(f"Type of Subtraction : {type(sub)}.")
print(f"Type of Addition : {type(add)}.")
print("------------------------------------------")
print("\n")

#Conditional statment
print("         IF ELIF ELSE")
if h > f :
    print(f"{h} is greater then {f}.")
elif h < f :
    print(f"{h} is less then {f}.")
else :
    print(f"{h} is equal to {f}.")
print("------------------------------------------")
print("\n")

print("         OR CONDITION")
if h > f or h < f :
    print("less then both equal")
else:
    print("Equal")
print("------------------------------------------")
print("\n")

#string 
print("         String")
string = "My name is momina idrees . i am student of NEXTSKILL."
print(f"content : {string} \nType : {type(string)}")
print("------------------------------------------")
print("\n")

print(" ")
print("First name : " , string[11:17:])
print("Last name : " , string[18:24:])
print("Organization name : " , string[43:52:])
print("Length of string : " , len(string))
print("Reverse string " , string[::-1])
print("------------------------------------------")
print("\n")

print("\neach character using loop")
for a in string:
    print(a , end=" ")
print("\n------------------------------------------")
print("\n")

print("\nas soon as first a comes it stops :")
for a in string:
    if a == 'a':
        break
    print(a , end=" ")
print("\n------------------------------------------")
print("\n")

print("\nSkipping all the A's :")
for a in string:    
    if a == 'a':
        continue
    print(a , end=" ")
print("\n------------------------------------------")
print("\n")

my_int = 0 
while my_int <= 3:
    print(my_int, end=" ")
    my_int +=1 

