flight=input("Is flight available? Yes/No:")
PIA=input("Is PIA available? Yes/No:")
Qatar=input("Is Qatar Airways available? Yes/No:")
Dubai=input("Is Dubai Air available? Yes/No:")
if flight=="Yes":
    if PIA =="Yes":
        print("PIA is available, you'll be able to board")
    else: 
        if Qatar=="Yes":
            print("Qatar Airways is available,you'll be able to board!!")
        else:
            if Dubai=="Yes":
                print("Dubai Airways is available,you'll be able to Board")
else:
    print("NO Airline is available, GO BY ROAD!!!!")
                
                        



