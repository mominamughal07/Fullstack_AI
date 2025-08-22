# Convert Minutes to Hours and Minutes 
# Input number of minutes and convert to hours and remaining minutes. 
# Example: 130 minutes → 2 hours 10 minutes

mints = int(input("Enter minutes :"))

hours = int(mints / 60)
min = mints % 60

print("Hours : {} & Mints : {}".format(hours , min))