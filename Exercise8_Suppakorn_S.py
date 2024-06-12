username = input("Username : ")
password = input("Password : ")

if username == 'peem' and password == '1234':
    print("    Welcome to Peem's Shop")
    print("------------------------------")
    print("You can select the product to purchase.")
    print("1. Pencil        10 THB")
    print("2. Pen           20 THB")
    print("3. Pencil case   100 THB")
    print("4. Ruler         20 THB")
    print("5. Scissors      40 THB")
    print("------------------------------")
    choose = int(input("Choose : "))
    if choose == 1:
        x = input("Fill number of product : ")
        print("Total : 10 x", x, '=', 10 * int(x), "THB")
        print("------------------------------")
    elif choose == 2:
        x = input("Fill number of product : ")
        print("Total : 20 x", x, '=', 20 * int(x), "THB")
        print("------------------------------")
    elif choose == 3:
        x = input("Fill number of product : ")
        print("Total : 100 x", x, '=', 100 * int(x), "THB")
        print("------------------------------")
    elif choose == 4:
        x = input("Fill number of product : ")
        print("Total : 20 x", x, '=', 20 * int(x), "THB")
        print("------------------------------")
    elif choose == 5:
        x = input("Fill number of product : ")
        print("Total : 40 x", x, '=', 40 * int(x), "THB")
        print("------------------------------")
else:
    print("Incorrect")
