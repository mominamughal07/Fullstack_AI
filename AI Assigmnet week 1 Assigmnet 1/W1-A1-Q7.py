# Distribute Items Equally - You have n candies and k students. 
# Write a program to find: 
# how many candies each student gets 
# how many are left 

NoOfCandies = int(input("Enter number of candies :"))
NoOfStudents = int(input("Enter number of students :"))

EachStudentCandie = int(NoOfCandies/NoOfStudents)
Leftcandies = int(NoOfCandies%NoOfStudents)

print("No of candies each student gets : " , EachStudentCandie)
print("No of candies left : ", Leftcandies) 