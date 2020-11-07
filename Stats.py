import matplotlib.pyplot as plt
# import mysql.connector
import sqlite3
con=sqlite3.connect("collegeproject.db")
c=con.cursor()
c.execute("Create table if not exists customer(name varchar(30)NOT NULL, phone int(11),email varchar(100), money int(11), points int(11),PRIMARY KEY (phone))")
c.execute("Create table if not exists items(itemName varchar(40), price int(11),sale int(11), PRIMARY KEY (itemName))")
c.execute("Create table if not exists sales(month varchar(11), customers int(11),sale int(11), PRIMARY KEY (month))")
con.commit()
from scipy import stats
import numpy as np
import csv
from matplotlib.widgets import Button
class Stats:
    def customerStats(self):
        sql = "SELECT `name`,`money` FROM `customer`"
        # con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="collegeproject",
        #                               port="3306")
        cursor = con.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        rName=[]
        rMoney=[]
        for x in rows:
            rName.insert(0,x[0])
            rMoney.insert(0,x[1])
        plt.scatter(rName,rMoney)
        plt.show()

    def itemsStats(self):
        sql = "SELECT `itemName`, `sale` FROM `items`"
        # con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="collegeproject",
        #                               port="3306")
        cursor = con.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        rIName = []
        rSales = []
        for x in rows:
            rIName.insert(0, x[0])
            rSales.insert(0, x[1])
        plt.scatter(rIName, rSales)
        plt.show()
        #csv pending

    def salesStats(self):
        sql = "SELECT `month`, `customers`, `sale` FROM `sales`"
        # con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="collegeproject",
        #                               port="3306")
        cursor = con.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        rMon = []
        rCust = []
        rSale = []
        for x in rows:
            rMon.insert(0, x[0])
            rCust.insert(0, x[1])
            rSale.insert(0,x[2])
        fig=plt.figure()
        aplt=fig.add_subplot(211)
        aplt.scatter(rMon,rCust)
        aplt.plot(rMon,rCust)
        bplt=fig.add_subplot(212)
        bplt.scatter(rMon,rSale)
        bplt.plot(rMon,rSale)
        plt.show()

    def salePredicition(self):
        sql="select customers from sales"
        # con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="collegeproject",
        #                               port="3306")
        cursor = con.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        cRows=[]
        for r in rows:
            cRows.extend(r)
        sql = "select sale from sales"
        # con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="collegeproject",
        #                               port="3306")
        cursor = con.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        sRows=[]
        for r in rows:
            sRows.extend(r)
        data = stats.linregress(cRows,sRows)
        maxX = np.max(cRows) + 10
        minX = np.min(sRows) - 10
        x = np.linspace(minX, maxX, 100)
        y = data[1] + data[0] * x
        plt.plot(x, y, color="r", label="Regression Line")
        plt.scatter(cRows, sRows, color="b", label="Data Points")
        plt.show()
        #prediction almost done

    def exportCSV(self):
        sql = "SELECT `month`, `customers`, `sale` FROM `sales`"
        # con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="collegeproject",
        #                               port="3306")
        cursor = con.cursor()
        cursor.execute(sql)
        with open("Sales-Stats.csv", "w", newline='') as csv_file:  # Python 3 version
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow([i[0] for i in cursor.description])  # write headers
            csv_writer.writerows(cursor)
        sql = "select * from customer"
        # con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="collegeproject",
        #                               port="3306")
        cursor = con.cursor()
        cursor.execute(sql)
        with open("Customer-Records.csv", "w", newline='') as csv_file:  # Python 3 version
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow([i[0] for i in cursor.description])  # write headers
            csv_writer.writerows(cursor)
        sql = "select * from items"
        # con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="collegeproject",
        #                               port="3306")
        cursor = con.cursor()
        cursor.execute(sql)
        with open("Items-Records.csv", "w", newline='') as csv_file:  # Python 3 version
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow([i[0] for i in cursor.description])  # write headers
            csv_writer.writerows(cursor)

# c=Stats()
# c.customerStats()
# c.exportCSV()
