# QN. In last lab you did a task to take input three sides of a triangleand show the area of a triangle.
# We assumed that the user will always enter a valid triangle. As we know that a valid triangle the
# condition is that the sum of 2 sides should be greater than the 3rd one. Now update that program
# such that it takes 3 sides as input and will print the area only if a valid triangle otherwise it 
# should print that triangle is invalid.


side1=int(input("Enter length of side1:"))
side2=int(input("Enter length of side2:"))
side3=int(input("Enter length of side3:"))
sum_of_side1_and_side2=side1+side2


if sum_of_side1_and_side2 > side3:
    print("This is a valid triangle!!!")
    print(f"Therefore the area of this triangle is {side1*side2*side3}")
else:
    print("This triangle is invalid!!!!!")
print()   # The 2 empty print functions are for spacing the work in the command prompt  
print()   

# Write a program that will take 3 numbers as input and will print the maximum of the 3 numbers as output
#You have to use 3 if statements
num1=int(input("Enter number 1:"))
num2=int(input("Enter number 2:"))
num3=int(input("Enter number 3:"))
if num1 >num2 and num1>num3:
    print(f"{num1} which is number 1 is the maximum of the 3 numbers")
if num2>num1 and num2>num3:
    print(f"{num2} which is number 2 is the maximum of the 3 numbers") 
if num3>num2 and num3>num1:
    print(f"{num3} which is number 3 is the maximum of the 3 numbers") 
print()
print()  # The 2 empty print functions are for spacing the work in the command prompt

# A company insures its employees in the following cases;
#If the employee is unmarried,male and above 30 years of age
#If the employee is unmarried,Female and above 25 years of age
# Write a program which takes marital status, gender and age as an input from the user.
# After checking the given condition,the output of the program will write a message stating whether he/she
# is eligible for insurance or not.

maritalstatus=input("Enter marital status M/U:") # M-married, U-unmarried
gender=input("Enter your gender M/F:") # Ma-male, F-female
age=int(input("Enter your age:"))
if maritalstatus=="M":
    print("Congratulations")
    print("You are eligible for insurance")
else:
 print("Sorry you are not eligible for insurance")
if age>30 and  maritalstatus=="U" and gender=="Ma":
    print("Congratulations you are eligible for insurance")
if age>25 and gender=="F" and maritalstatus=="U":
    print("Congratulations you are eligible for insurance")   

