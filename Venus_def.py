def get_num_customers(): # ask the user how many customers are ordering,validating the input
 while True:
   try:
      n=int(input("How many customers are ordering?:"))
      break
   except ValueError:
     print("Enter Valid input please specifically a number!!")
 return n #This is to return the number of customers!!,The return must be in line with the while loop

def get_customer_order(customer_number):
  #Collects 1 customer's name,meal choice, and student status.
    print(f'CUSTOMER{customer_number}')
    name=input("Name:")
    mealchoice=input("MealChoice(St/V/S):")# St-Standard,V-Vegetarian,S-Special
    student=input("Are u a student(Yes/No):")
    return name,mealchoice,student
def get_meal_price(mealchoice):#returns the base price for a given meal choice.
  if mealchoice=="St":
    return 8000
  elif mealchoice=="V":
    return 7000
  elif mealchoice=="S":
    return 12000
  else:
    print("Invalid meal choice")
    return 0
def apply_student_discount(price,student):
  # Applys a 10% discount if the customer is a student
  if student=="Yes":
    price=price*0.9 # 0.9 because we removed the 10%
  return  price

def process_customer(customer_number):# Handle 1 custome's full order and return the price they pay
  name,mealchoice,student=get_customer_order(customer_number)
  price=get_meal_price(mealchoice)
  price=apply_student_discount(price,student)
  print(f'This meal is {price} UGX')
  return price

def main():
   n=get_num_customers()
   total=0
   count=0

   for i in range(1,n+1):
      price=process_customer(i)
      count+=1
      total+=price
   print(f'The number of customer orders is {count}')
   print(f"The total money collected is {total} UGX") \

if __name__=="__main__":
  main() 



