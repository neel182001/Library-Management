# PYTHON MODULE : BOOK

from mysql.connector import errorcode
from datetime import date, datetime, timedelta
import os
import platform
import mysql.connector as sqltor
from mysql.connector import errorcode

def clrscreen():
        if platform.system()=="Windows":
            os.system("cls")
            
class Book:

    def display(n):
        try:
            clrscreen()
            os.system('cls')
            cnx = sqltor.connect(user='root', password='root',host='localhost',database='Library')
            Cursor = cnx.cursor()
            query = ("SELECT * FROM BookRecord")
            Cursor.execute(query)
            for (Bno,Bname,Author,price,publ,qty,d_o_purchase) in Cursor:
                print("============================================")
                print("Book Code              : ",Bno)
                print("Book Name              : ",Bname)
                print("Author of Book         : ",Author)
                print("Price of Book          : ",price)
                print("Publisher              : ",publ)
                print("Total Quantity in Hand : ",qty)
                print("Purchased On           : ",d_o_purchase)
                print("============================================")
            Cursor.close()
            cnx.close()
            print("\nYou have done it!!!!!!")
        except sqltor.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist :! ")
            else:
                print(err)
                cnx.close()
                
    def insertData(n):
        try:
            clrscreen()
            cnx = sqltor.connect(user='root',password='root',host='localhost',database='Library')
            Cursor = cnx.cursor()
            Qry = ("INSERT INTO BookRecord VALUES (%s, %s, %s, %s, %s, %s, %s)")
            bno=int(input("Enter Book Code : "))
            search = "SELECT count(*) FROM bookrecord WHERE Bno=%s;"
            val = (bno,)
            Cursor.execute(search,val)
            for x in Cursor:
                cnt = x[0]
                if cnt == 0:
                    bname=str(input("Enter Book Name : "))
                    Auth=str(input("Enter Book Author's Name : "))
                    price=int(input("Enter Book Price : "))
                    publ=str(input("Enter Publisher of Book : "))
                    qty=int(input("Enter Quantity purchased : "))
                    print("Enter Date of Purchase (Date/Month and Year separately): ")
                    DD=int(input("Enter Date : "))
                    MM=int(input("Enter Month : "))
                    YY=int(input("Enter Year : "))
                    data = (bno,bname,Auth,price,publ,qty,date(YY,MM,DD))
                    Cursor.execute(Qry,data)
                    # Make sure data is committed to the database
                    cnx.commit()
                    Cursor.close()
                    cnx.close()
                    print("\nRecord Inserted.............")
                else:
                    print("\nRecord already exists..")
        except sqltor.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
                cnx.close()
                
    def deleteBook(n):
        try:
            clrscreen()
            cnx = sqltor.connect(user='root',password='root',host='localhost',database='Library')
            Cursor = cnx.cursor()
            bno=input("Enter Book Code of Book to be deleted from the Library : ")
            if bno > 0:
                Qry =("""DELETE FROM BookRecord WHERE BNO = %s""")
                del_rec=(bno,)
                Cursor.execute(Qry,del_rec)
                # Make sure data is committed to the database
                cnx.commit()
                Cursor.close()
                cnx.close()
                print(Cursor.rowcount,"Record(s) Deleted Successfully.....")
            else:
                print("\nInvalid Value..")
        except sqltor.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
                cnx.close()
                
    def SearchBookRec(n):
        try:
            clrscreen()
            cnx = sqltor.connect(user='root',password='root',host='localhost',database='Library')
            Cursor = cnx.cursor()
            bno=input("Enter Book No. to be Searched from the Library : ")
            query = ("SELECT * FROM BookRecord where BNo = %s ")
            rec_srch=(bno,)
            Cursor.execute(query,rec_srch)
            Rec_count=0
            for (Bno,Bname,Author,price,publ,qty,d_o_purchase) in Cursor:
                Rec_count+=1
                print("===============================")
                print("Book Code : ",Bno)
                print("Book Name : ",Bname)
                print("Author of Book : ",Author)
                print("Price of Book : ",price)
                print("Publisher : ",publ)
                print("Total Quantity in Hand : ",qty)
                print("Purchased On : ",d_o_purchase)
                print("===============================")
            if Rec_count%2==0:
                print()
                print(Rec_count, "Record(s) found")
                # Make sure data is committed to the database
                cnx.commit()
                Cursor.close()
                cnx.close()
            else:
                print(Rec_count, "Record(s) found")
        except sqltor.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
                cnx.close()
                
    def UpdateBook(n):
        try:
            clrscreen()
            cnx = sqltor.connect(user='root',password='root',host='localhost',database='Library')
            Cursor = cnx.cursor()
            bno=input("Enter Book Code of Book to be Updated from the Library : ")
            query = ("SELECT * FROM BookRecord where BNo = %s ")
            rec_srch=(bno,)
            print("Enter new data ")
            bname=input("Enter Book Name : ")
            Auth=input("Enter Book Author's Name : ")
            price=int(input("Enter Book Price : "))
            publ=input("Enter Publisher of Book : ")
            qty=int(input("Enter Quantity purchased : "))
            print("Enter Date of Purchase (Date/MOnth and Year seperately: ")
            DD=int(input("Enter Date : "))
            MM=int(input("Enter Month : "))
            YY=int(input("Enter Year : "))
            Qry = ("UPDATE BookRecord SET bname=%s,Author=%s,price=%s,publ=%s,qty=%s,d_o_purchase=%s WHERE Bno=%s")
            data = (bname,Auth,price,publ,qty,date(YY,MM,DD),bno)
            Cursor.execute(Qry,data)
            # Make sure data is committed to the database
            cnx.commit()
            Cursor.close()
            cnx.close()
            print(Cursor.rowcount,"Record(s) Updated Successfully........")
        except sqltor.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
                cnx.close()

b = Book()

