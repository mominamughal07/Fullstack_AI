#Salary Calculator 
#Input basic salary. Calculate: 
# HRA = 20% of basic 
# DA = 15% of basic 
# Total Salary = Basic + HRA + DA

BasicSalary = float(input("Enter Basic salary :"))

HRA = BasicSalary * (20/100)
DA = BasicSalary * (15/100)
TotalSalary = BasicSalary + HRA + DA

print("Total salary {:.2f}".format(TotalSalary))
