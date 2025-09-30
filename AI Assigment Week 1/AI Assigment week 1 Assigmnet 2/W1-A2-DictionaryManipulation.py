# Dictionary Manipulation 
# 1.  Check if a value exists in a dictionary 

student = {
    "name": "Amina",
    "age": 17,
    "grade": "11th",
    "passed": True
}

value = 17

for item in student.values():
    if item == value:
        print("{} exits !".format(item))

# 2.  Get the key of a minimum value from the following dictionary 

numbers = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6
}

min_key = min(numbers.values())
print(min_key)


key_found = None
for key, value in numbers.items():
    if value == min_key:
        key_found = key
        break

print(key_found)

# 3.  Delete a list of keys from a dictionary
numbers = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6
}

keys_to_delete = ["two", "four", "six"]

for key in keys_to_delete:
    if key in numbers:
        del numbers[key]

print(numbers)
