""" YAWE JAYDEN JOHN
S26B38/009
This program basically allows several users to deposit money given they meet the required
criteria for the account type and then counts the total money deposited in all the accounts 
and the accounts successfully opened
"""
n=int(input("How many customers are u working on?:"))
count =0
total=0

for i in range(1,n+1): # To avoid repitition or in this case if u want something executed a certain no. of times.
    print(f"Client {i}:")
    name=input("Name:")
    age=int(input("Age:"))
    accounttype=input("Account type(S/C/T):") #S-Savings,C-Current,T-Student
    initial_deposit=int(input("Initial deposit:"))

    if accounttype=="S" and initial_deposit < 50000:
        print("Deposit too low.Minimum for Savings is 50,000 UGX")
    elif accounttype=="C" and initial_deposit<100000:
            print("Deposit too low.Minimum for Current is 100,000 UGX")
    elif  accounttype=="T" and initial_deposit< 20000:
            print("Deposit too low. Minimum for Student is 20,000 UGX")
    elif accounttype=="T" and age>25:
          print("This account is for Students sorry")        
    else:
        print(f"Account opened successfully for {name}.Balance is {initial_deposit}")
        count +=1
        total+=initial_deposit

print(f"The accounts opened successfully:{count}")     
print(f"Total amount deposited:{total} UGX")   







