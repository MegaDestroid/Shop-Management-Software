# import mysql.connector
import sqlite3
con=sqlite3.connect("collegeproject.db")
c=con.cursor()
c.execute("Create table if not exists customer(name varchar(30)NOT NULL, phone int(11),email varchar(100), money int(11), points int(11),PRIMARY KEY (phone))")
c.execute("Create table if not exists items(itemName varchar(40), price int(11),sale int(11), PRIMARY KEY (itemName))")
c.execute("Create table if not exists sales(month varchar(11), customers int(11),sale int(11), PRIMARY KEY (month))")
con.commit()

from sklearn import tree
from sklearn.naive_bayes import GaussianNB
import numpy as np
from datetime import date
dToday=str(date.today().month)+"-"+str(date.today().year)

class Sales:
    def mnyPurchase(self,phone,money):
        sql = "select `money` from customer where phone ='{}'".format(phone)
        # con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="collegeproject", port="3306")
        cursor = con.cursor()
        cursor.execute(sql)
        rows = cursor.fetchone()
        sql = "update customer set money ='{}'where phone={}".format((rows[0]+money), phone)
        # con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="collegeproject",
        #                               port="3306")
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()

        sql = "select month from sales where month='{}'".format(dToday)
        # con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="collegeproject",
        #                               port="3306")
        cursor = con.cursor()
        cursor.execute(sql)
        rows = []
        rows = cursor.fetchone()

        if rows == None:
            print("running insert sales")
            sql = "insert into sales values('{}',0,'{}')".format(dToday,money)
            # con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="collegeproject",
            #                               port="3306")
            cursor = con.cursor()
            cursor.execute(sql)
            con.commit()
        else:
            print("running update sales")
            sql = "select sale from sales where month='{}'".format(dToday)
            # con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="collegeproject",
            #                               port="3306")
            cursor = con.cursor()
            cursor.execute(sql)
            rrows = (cursor.fetchall())
            sql = "update sales set sale= '{}' where month='{}'".format(rrows[0][0] + money, dToday)
            # con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="collegeproject",
            #                               port="3306")
            cursor = con.cursor()
            cursor.execute(sql)
            con.commit()

        msg="Purchase completed successfully!!"
        return msg
        #updating sales table testing almost done

    def pntPurchase(self,phone,money):
        sql = "select points from customer where phone ='{}'".format(phone)
        # con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="collegeproject", port="3306")
        cursor = con.cursor()
        cursor.execute(sql)
        rows = list(cursor.fetchone())
        if money > rows[0]:
            msg="You don't have enough points!!"
            return msg
        elif money > 500:
            msg = "You can't spend more than 500 points!!"
            return msg
        else:
            rows[0]=rows[0]-money
            sql = "update customer set points ='{}'where phone={}".format(rows[0], phone)
            # con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="collegeproject",
            #                               port="3306")
            cursor = con.cursor()
            cursor.execute(sql)
            con.commit()
            msg="Purchase completed successfully!!"
            return (msg,rows[0])
        
    def pntUpdate(self,cMoney,phone):
        sql="select money from customer where phone='{}'".format(phone)
        # con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="collegeproject",
        #                               port="3306")
        cursor = con.cursor()
        cursor.execute(sql)
        rows=cursor.fetchone()
        r=[]
        r.extend(rows)
        print(rows,r)
        data=[[1,10000],
              [100,100],
              [500,500],
              [1000,1000],
              [100,1000],
              [500,1000],
              [1000,2000],
              [2000,5000],
              [5000,10000],
              [5000,20000]]
        labels=[0,0,0,1,1,2,2,3,3,4]
        model = GaussianNB()
        model.fit(data, labels)
        input = [[cMoney,r[0]]]
        output = model.predict(input)
        print(output)
        if output[0]==0:
            points=np.random.randint(0,5)
            print(points)
        elif output[0]==1:
            points = np.random.randint(5, 10)
            print(points)
        elif output[0]==2:
            points = np.random.randint(10, 20)
            print(points)
        elif output[0]==3:
            points = np.random.randint(20, 40)
            print(points)
        elif output[0]==4:
            points = np.random.randint(40, 70)
            print(points)
        else:
            print("No points won!!")

        sql = "select points from customer where phone ='{}'".format(phone)
        # con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="collegeproject",
        #                               port="3306")
        cursor = con.cursor()
        cursor.execute(sql)
        rows = cursor.fetchone()


        sql = "update customer set points = {} where phone = {}".format(rows[0]+points,phone)
        # con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="collegeproject",
        #                               port="3306")
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()
        return points
        #increasing points after purchase testing almost done
    

    def delItem(self, itemName):
        sql = "delete from items where itemName ='{}'".format(itemName)
        # con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="collegeproject",
        #                               port="3306")
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()
        msg="Item has been deleted!!"
        return msg

    def addItem(self, itemName, price):
        sql = "insert into items values('{}','{}',0)".format(itemName, price)
        # con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="collegeproject",
        #                               port="3306")
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()
        msg = "Item has been added!!"
        return msg
    
    def updItem(self,itemName,price):
        sql = "update items set price ='{}'where itemName='{}'".format(price, itemName)
        # con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="collegeproject", port="3306")
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()
        msg="Item prices have been updated!!"
        return msg
    
    def allItem(self):
        sql = "select itemName, price from items"
        # con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="collegeproject", port="3306")
        cursor = con.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        return rows
    
    def getItemPrice(self,itemName):
        sql = "select price from items where itemName = '{}'".format(itemName)
        # con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="collegeproject",
        #                               port="3306")
        cursor = con.cursor()
        cursor.execute(sql)
        rows=cursor.fetchone();
        return int(rows[0])


# c=Sales()
# c.getItemPrice("Bhujia 200g")