# Calculate Body Mass Index (BMI) 
# Input weight (kg) and height (m), then calculate: 
# BMI = weight / (height ** 2)

weight = float(input("Enter Weight : ")) 
height = float(input("Enter Height : "))

BMI = weight / (height ** 2)

print("BMI = {:.2f}".format(BMI))