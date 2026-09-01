# "And"is multiplication
# "or"is addition

# print(True or False)
# print(True and False)

# test1=int(input("Enter Score in Test 1:"))
# test2=int(input("Enter score in  test2:"))
# test3=int(input("Enter score in test 3:"))
# avg=(test1+test2+test3)/3
# print(f"Your avg score is {avg}")

# x=int(input('Enter a number:'))
# if x>0:
#     print("x is a positive number")
#     print("positive numbers are great!!!!!")
# else:
#     print("why is your number a negative broo!!!")
# print("Thanks for your time!!!")   # when the indentation is in the line of "if" it prints it regardless of the outcome 

x=int(input("Enter a number:"))
if x%2==0:
    print("Your number is an even number")
else:
    print("Your number is an odd number!")

subject1=int(input("Enter score for subject 1:"))
subject2=int(input("Enter score for subject 2:"))
subject3=int(input("Enter score for subject 3:"))
subject4=int(input("Enter score for subject 4:"))
subject5=int(input("Enter score for subject 5:"))
avg=(subject1+subject2+subject3+subject4+subject5)/5
print(f"Your avg score is {avg}")

if avg >=80:
    print("You are an outstanding student!!")
if avg >=70 and avg < 80:
    print("You are a good student")
if avg >=60 and avg <70:
    print('You are an average student')
if avg >=50 and avg< 60:
    print("You are a below average student")
if avg >=40 and avg < 50:
    print("You are a poor student")
if avg < 40:
    print("You need extra ordinary efforts.")        
    