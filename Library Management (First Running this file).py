#Project on Library Management System
#--------------------------------------------------------------------

#MODULE : LIBRARY MANAGEMENT

from Menulib import *
from Book import *

#____Main____

while True:
    clrscreen()
    print("\n\tLibrary Management")
    print("================================")
    print("1. Library Setup")
    print("2. Book Management")
    print("3. Members Management")
    print("4. Issue/Return Book")
    print("5. Exit")
    print("================================")
    choice=int(input("Enter Choice between 1 to 5--> : "))
    if choice==1:
        ml.create_database()
    elif choice==2:
        ml.MenuBook()
    elif choice==3:
        ml.MenuMember()
    elif choice==4:
        ml.MenuIssueReturn()
    elif choice==5:
        for elements in dir():
            del(elements)
        break
    else:
        print("Wrong Choice...... Enter Your Choice again")
    x=input("\nPress Enter key to continue...")

