def menu():
    print("[1] Citi Burger R22.00")
    print("[2] Citi Pie R12.00")
    print("[3] Sausage/Russian roll    R13.00")
    print("[4] Russian roll and chips  R20.00")
    print("[5] Small chips   R10.00")
    print("[6] Big chips  R20.00")
    print("[7] Coke (350ml) R9.00")
    print("[0] invalid")
    print("\n")

menu()
option = int(input("What would you like to order? "))

while option != 0:
    if option == 1:
        print("Citi Burger R22.00")
        
    elif option == 2:
        print("Citi Pie R12.00")
        
    elif option == 3:
        print("Sausage/Russian roll    R13.00")
        
    elif option == 4:
        print("Russian roll and chips  R20.00")
        
        
    elif option == 5:
        print("Small chips   R10.00")
        
    elif option == 6:
        print("Big chips  R20.00")
        
    elif option == 7:
        print("Coke (350ml) R9.00")
        
        
    else:
        print("invalid option!")

    print(" ")
    menu()
    option = int(input("enter your option"))

print("THANK YOU")