#Write a program that converts a temperature from Celsius to Fahrenheit. (Formula: Fahrenheit = 
#(Celsius * 9/5) + 32) 


celsius_temperature = float(input("Enter a temperature in celsius : "))

fahrenheit = (celsius_temperature * (9/5)) + 32

print(f"{celsius_temperature:.2f}° into Fahrenite : {fahrenheit:.2f}°")
              

