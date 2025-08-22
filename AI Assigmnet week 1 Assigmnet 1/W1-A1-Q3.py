# Calculate Compound Interest 
# Use the formula: 
# CI = P * (1 + R/100)**T - P 
# Where P = principal, R = rate, T = time

P = float(input("Enter Principal : "))
T = float(input("Enter Time in years : "))
R = float(input("Enter Rate : "))

CI =  (P * (1 + R/100)**T) - P 

print("Compound Interest : " , CI)
