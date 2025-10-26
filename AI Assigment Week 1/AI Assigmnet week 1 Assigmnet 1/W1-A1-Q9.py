# Total Marks and Percentage 
# Input marks of 5 subjects. Print: 
#  Total marks 
#  Percentage 
#  Average 

print("Enter marks outof 100 : " )

Math = float(input("Math  : "))
English = float(input("English: "))
Urdu = float(input("Urdu: "))
Computer = float(input("Computer: "))
Science = float(input("Science: "))

TotalMarks = Math + English + Urdu + Computer + Science

print("Obtain marks : " , TotalMarks)
print("Percentage : {:.2f} ".format(((TotalMarks/500)*100)))
print("Average  : {:.2f} ".format(TotalMarks/5) )