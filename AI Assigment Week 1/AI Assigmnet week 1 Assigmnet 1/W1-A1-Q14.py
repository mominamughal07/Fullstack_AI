# Percentage of Correct Answers 
# Input total questions and correct answers, and calculate the percentage score. 

totalquestions = int(input("Enter the total number of questions: "))
correctanswers = int(input("Enter the number of correct answers: "))


percentage = (correctanswers / totalquestions) * 100
print(f"You scored {percentage:.2f}%")
