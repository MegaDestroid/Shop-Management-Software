# import mysql.connector
import sqlite3
con=sqlite3.connect("collegeproject.db")
c=con.cursor()
c.execute("Create table if not exists customer(name varchar(30)NOT NULL, phone int(11),email varchar(100), money int(11), points int(11),PRIMARY KEY (phone))")
c.execute("Create table if not exists items(itemName varchar(40), price int(11),sale int(11), PRIMARY KEY (itemName))")
c.execute("Create table if not exists sales(month varchar(11), customers int(11),sale int(11), PRIMARY KEY (month))")
con.commit()

from datetime import date
dToday=str(date.today().month)+"-"+str(date.today().year)
class Customer:
    def __init__(self,name,phone,email):
        self.name=name
        self.phone=phone
        self.email=email

    def newCustomer(self,cust):
        print("running insert customer")
        sql = "insert into customer values('{}','{}','{}',0,0)".format(cust.name, cust.phone, cust.email)
        # con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="collegeproject", port="3306")
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()

        sql="select month from sales where month='{}'".format(dToday)
        # con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="collegeproject",
        #                               port="3306")
        cursor = con.cursor()
        cursor.execute(sql)
        rows=[]
        rows=cursor.fetchone()
        
        if rows==None:
            print("running insert sales")
            sql = "insert into sales values('{}',1,0)".format(dToday)
            # con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="collegeproject",
            #                               port="3306")
            cursor = con.cursor()
            cursor.execute(sql)
            con.commit()
        else:
            print("running update sales")
            sql="select customers from sales where month='{}'".format(dToday)
            # con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="collegeproject",
            #                               port="3306")
            cursor = con.cursor()
            cursor.execute(sql)
            rrows = (cursor.fetchall())
            sql="update sales set customers= '{}' where month='{}'".format(rrows[0][0]+1,dToday)
            # con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="collegeproject",
            #                               port="3306")
            cursor = con.cursor()
            cursor.execute(sql)
            con.commit()

    def updCustomer(self,cust):
        print("running update customer")
        sql = "update customer set name ='{}', email='{}'where phone='{}'".format(cust.name, cust.email,
                                                                                          cust.phone)
        # con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="collegeproject", port="3306")
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()
        msg="Customer details updated!!"
        return msg

    def delCustomer(self,cust):
        print("running delete customer")
        sql = "delete from customer where phone={}".format(cust.phone)
        # con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="collegeproject", port="3306")
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()
        msg="Customer deleted!!"
        return msg

    def shwCustomer(self,cust):
        print("running show customer")
        sql = "select * from customer"
        # con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="collegeproject", port="3306")
        cursor = con.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        print(rows)
        return rows

# cs=Customer("zcxcx",992319,"iiii")
# cs.newCustomer(cs)
