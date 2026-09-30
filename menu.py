menu=[] # The list
while True:
    try:
      choice=input("1.add items 2. View items  3.Exit:").lower()
      match choice:
         case "1":
            menu.append(input("Item:")) 
            print("Added")
         case "2":
            print(menu)
         case "3":
            break
         case _:  # works like the else statement incase a wrong option is chosen or none of the above is satistified
            print("Invalid")
    except KeyboardInterrupt:
       break       
        


