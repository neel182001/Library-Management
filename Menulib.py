#PYTHON MODULE: MENULIB

import mysql.connector as sqltor
from Book import *
from Member import *
from Issue import *

class MenuLib:
    
    def create_database(n):
        mydb = sqltor.connect(host='localhost',user='root',passwd='root')
        mycursor=mydb.cursor()
        print("Creating Library Database...")
        mycursor.execute("CREATE Database if not exists Library")
        print("Library Database created\n")
        mycursor.close()
        mydb.close()
        mydb = sqltor.connect(host='localhost',user='root',passwd='root',database='Library')
        mycursor=mydb.cursor()
        print("Creating BookRecord table...") 
        mycursor.execute("CREATE TABLE if not exists BookRecord (Bno int(8) PRIMARY KEY,Bname char(80) NOT NULL,Author varchar(80),Price float(8,2),Publ char(80),qty int(15),d_o_purchase DATE);")
        print("BookRecord Table created\n")
        print("Creating Member table...")
        mycursor.execute("CREATE TABLE if not exists Member (Mno int(8) PRIMARY KEY, Mname char(30), MOB int(20) NOT NULL ,DOP DATE, ADR varchar(80));")   
        print("Member table created\n")       
        print("Creating Issue table...")   
        mycursor.execute("CREATE TABLE if not exists Issue (Bno int(8) PRIMARY KEY, Mno int(8), d_o_Issue DATE, d_o_ret DATE);")  
        print("Issue table created\n")
        
    def MenuBook(n):
        while True:
            clrscreen()
            print("\n   Book Record Management")
            print("===============================")
            print("1. Add Book Record")
            print("2. Display all Book Records")
            print("3. Search Book Record")
            print("4. Delete Book Record")
            print("5. Update Book Record")
            print("6. Return to Main Menu")
            print("===============================")
            choice=int(input("Enter Choice between 1 to 5-------> : "))
            if choice==1:
                b.insertData()
            elif choice==2:
                b.display()
            elif choice==3:
                b.SearchBookRec()
            elif choice==4:
                b.deleteBook()
            elif choice==5:
                b.UpdateBook()
            elif choice==6:
                return
            else:
                print("Wrong Choice......Enter Your Choice again")
            x=input("Press Enter  key to continue...")
            
    def MenuMember(n):
        while True:
            clrscreen()
            print("\n    Member Record Management")
            print("===============================")
            print("1. Add Member Record")
            print("2. Display all Member Records")
            print("3. Search Member Record")
            print("4. Delete Member Record")
            print("5. Update Member Record")
            print("6. Return to Main Menu")
            print("===============================")
            choice=int(input("Enter Choice between 1 to 5--> : "))
            if choice == 1:
                mem.insertMember()
            elif choice == 2:
                mem.display()
            elif choice == 3:
                mem.SearchMember()
            elif choice == 4:
                mem.deleteMember()
            elif choice == 5:
                mem.UpdateMember()
            elif choice==6:
                return
            else:
                print("Wrong Choice......Enter Your Choice again")
            x=input("Press Enter key to continue...")
            
    def MenuIssueReturn(n):
        while True:
            clrscreen()
            print("\n    Member Record Management")
            print("=================================")
            print("1. Issue Book")
            print("2. Display all Issued Book Records")
            print("3. Return Issued Book")
            print("4. Return to Main Menu")
            print("=================================")
            choice=int(input("Enter Choice between 1 to 4--> : "))
            if choice==1:
                i.issueBook()
            elif choice==2:
                i.ShowIssuedBooks()
            elif choice==3:
                i.returnBook()
            elif choice==4:
                return
            else:
                print("Wrong Choice......Enter Your Choice again")
            x=input("Press Enter  key to continue...")


ml = MenuLib()

