#PYTHON MODULE MEMBER
from mysql.connector import errorcode
from datetime import date, datetime, timedelta
from mysql.connector import(connection)
import mysql.connector
import os
from Book import *


class Member:
    
    def display(n):
        try:
            clrscreen()
            os.system('cls')
            cnx = connection.MySQLConnection(user='root', password='root',host='localhost',database='Library')
            Cursor = cnx.cursor()
            query = ("SELECT * FROM Member")
            Cursor.execute(query)
            for (Mno,Mname,MOB,DOP,ADR) in Cursor:
                print("==================================================")
                print("Member Code          : ",Mno)
                print("Member Name          : ",Mname)
                print("Mobile No. of Member : ",MOB)
                print("Date of Membership   : ",DOP)
                print("Address              : ",ADR)
                print("==================================================")
            Cursor.close()
            cnx.close()
            print("You have done it!!!!!!")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
                cnx.close()
                
    def insertMember(n):
        try:
            clrscreen()
            cnx = connection.MySQLConnection(user='root',password='root',host='localhost',database='Library')
            Cursor = cnx.cursor()
            Qry = ("INSERT INTO Member VALUES(%s, %s, %s, %s, %s)")
            mno=int(input("Enter Member Code : "))
            search = "SELECT count(*) FROM member WHERE mno=%s;"
            val = (mno,)
            Cursor.execute(search,val)
            for x in Cursor:
                cnt = x[0]
                if cnt == 0:
                    mname=str(input("Enter Member Name : "))
                    mob=str(input("Enter Member Mobile No. : "))
                    if len(mob) == 10:
                        print("Enter Date of Membership (Date/Month and Year seperately): ")
                        DD=int(input("Enter Date : "))
                        MM=int(input("Enter Month : "))
                        YY=int(input("Enter Year : "))
                        addr=input("Enter Member Adress : ")
                        data = (mno,mname,mob,date(YY,MM,DD),addr)
                        Cursor.execute(Qry,data)
                        #  Make sure data is committed to the database
                        cnx.commit()
                        Cursor.close()
                        cnx.close()
                        print("\nRecord Inserted.............")
                    else:
                        print("\nPlease enter correct Mobile No. !!!")
                else:
                    print("\nRecord already exists..")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
                cnx.close()
                
    def deleteMember(n):
        try:
            clrscreen()
            cnx = connection.MySQLConnection(user='root',password='root',host='localhost',database='Library')
            Cursor = cnx.cursor()
            mno=input("Enter Member Code to be deleted from the Library : ")
            Qry =("""DELETE FROM Member WHERE MNO = %s""")
            del_rec=(mno,)
            Cursor.execute(Qry,del_rec)
            # Make sure data is committed to the database
            cnx.commit()
            Cursor.close()
            cnx.close()
            print(Cursor.rowcount,"Record(s) Deleted Successfully..........")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
                cnx.close()
                
    def SearchMember(n):
        try:
            clrscreen()
            cnx = connection.MySQLConnection(user='root',password='root',host='localhost',database='Library')
            Cursor = cnx.cursor()
            mnm=input("Enter Member Name : ")
            query = ("SELECT * FROM Member where MName = %s ")
            rec_srch=(mnm,)
            Cursor.execute(query,rec_srch)
            Rec_count=0
            for (Mno,Mname,MOB,DOP,ADR) in Cursor:
                Rec_count+=1
                print("==================================================")
                print("Member Code          : ",Mno)
                print("Member Name          : ",Mname)
                print("Mobile No. of Member : ",MOB)
                print("Date of Membership   : ",DOP)
                print("Address              : ",ADR)
                print("==================================================")
            if Rec_count%2==0:
                print()
                print(Rec_count, "Record(s) found")
                # Make sure data is committed to the database
                cnx.commit()
                Cursor.close()
                cnx.close()
            else:
                print(Rec_count, "Record(s) found")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
                cnx.close()
                
    def UpdateMember(n):
        try:
            clrscreen()
            cnx = sqltor.connect(user='root',password='root',host='localhost',database='Library')
            Cursor = cnx.cursor()
            mname=input("Enter Member Name : ")
            search = "SELECT count(*) FROM member WHERE Mname=%s;"
            val = (mname,)
            Cursor.execute(search,val)
            for x in Cursor:
                cnt = x[0]
                if cnt > 0:
                    query = ("SELECT * FROM Member where Mname = %s ")
                    rec_srch=(mname,)
                    print("\nEnter new data .. ")
                    Mname=input("Enter Member Name : ")
                    MOB = str(input("Enter new Mobile No. : "))
                    ADR = str(input("Enter new Address : "))
                    print("\nEnter new Date of Membership (Date/MOnth and Year seperately: ")
                    DD=int(input("Enter Date : "))
                    MM=int(input("Enter Month : "))
                    YY=int(input("Enter Year : "))
                    Qry = ("UPDATE Member SET mname=%s,MOB=%s,DOP=%s,ADR=%s WHERE mname=%s")
                    data = (Mname,MOB,date(YY,MM,DD),ADR,mname)
                    Cursor.execute(Qry,data)
                    # Make sure data is committed to the database
                    cnx.commit()
                    Cursor.close()
                    cnx.close()
                    print("\n 1 Record(s) Updated Successfully........")
                else:
                    print("\nRecord Doesn't exixts !!!")
        except sqltor.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
                cnx.close()
                

mem = Member()
