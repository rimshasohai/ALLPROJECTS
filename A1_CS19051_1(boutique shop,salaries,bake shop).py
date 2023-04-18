while True:
    print('OBJECTS     \n1.BAKE SHOP      \n2.EMPLOYEE         \n3.BOUTIQUE            \nPRESS ANY OTHER KEY TO EXIT')
    choice3=input('ENTER THE OBJECT YOU WANT TO CALL:')
    if choice3=='1':
        from A1_CS19051_2 import food
        print()
        food()
    elif choice3=='2':
        from A1_CS19051_2 import employees
        print()
        employees()
    elif choice3=='3':
        from A1_CS19051_2  import boutique
        print()
        boutique()
    else:
        break
