"""

This program basically allows several users to place orders at a campus canteen
displays meal prices and offers a 10% discount to students only
"""
while True:
    try:
        n=int(input("How many customers are ordering?:"))
        break
    except ValueError:
        print("Enter Valid Input Please")
count=0
total=0        
for i in range(1,n+1):
    print(f"CUSTOMER {i}")
    name=input("Name:")
    meal_choice=input("Meal Choice(St/V/S):") # St-Standard, V-Vegetarian,S-Special
    student=input("Are u a student(Yes/No):")

    if meal_choice=="St":
        price=8000
    elif meal_choice=="V":
        price=7000 
    elif meal_choice=="S":
        price=12000
    else:
        price=0
        print("Invalid meal Choice")
    if student=="Yes":
        price=price*0.9  # 0.9 because we removed the 10%
    print(f"This meal is {price} UGX")   
    count+=1
    total+=price
print(f"The number of customer orders is {count}")  
print(f"The total money collected is {total} UGX")  
