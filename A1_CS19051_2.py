def food():
    while True:
        print('MENU             \n1.SHOW TOTAL ITEMS IN STOCK  \n2.TAKE ORDER,ADJUST BILL    \n3.ADD  NEW ITEMS IN STOCK      \n PRESS ANY OTHER KEY TO EXIT')
        print()
        choice=input('ENTER CHOICE NUMBER:')
        print()
        if choice=='1':
            with open('A1_CS19051_4.py','r') as f:
                from A1_CS19051_4 import stock
                stock()
        elif choice=='2':
            with open('A1_CS19051_4.py','r') as c:
                from A1_CS19051_4 import order
                order()
        elif choice=='3':
            with open('A1_CS19051_4.py','r') as u:
                from A1_CS19051_4 import new_items
                new_items()
        else:
            break


def employees():
    while True:
        print('MENU         \n1.ENTER EMPLOYEES INFORMATION  \n2.TO KNOW ABOUT EMPLOYEES WORKED HOURS IN A MONTH  \n3.TO KNOW EMPLOYEES BONUS  \n4.TO  KNOW EMPLOYEES PAYMENT \n PRESS ANY KEY TO EXIT')
        print()
        choice1=input('ENTER CHOICE NUMBER:')
        print()
        if choice1=='1':
            from A1_CS19051_4 import employee_info
            employee_info()
        elif choice1=='2':
            from A1_CS19051_4  import employee_hours
            employee_hours()
        elif choice1=='3':
            from A1_CS19051_4 import employee_bonus
            employee_bonus()
        elif  choice1=='4':
            from A1_CS19051_4 import employees_payment
            employees_payment()
        else:
            break

def boutique():
    while True:
        print('MENU       \n1.SHOW TOTAL ITEMS IN STOCK     \n2.TAKE ORDER,ADJUST BILL      \n3ADD  NEW ITEMS IN STOCK  \nPRESS ANY OTHER KEY TO EXIT')
        print()
        choice2=input('ENTER CHOICE NUMBER:')
        print()
        if choice2=='1':
              from  A1_CS19051_3   import  boutique_stock
              boutique_stock()
        elif choice2=='2':
            from  A1_CS19051_3  import order_customer
            order_customer()
        elif choice2=='3':
            from  A1_CS19051_3  import add_items
            add_items()
        else:
            break

              
        
