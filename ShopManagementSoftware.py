import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from CustomerManagement2 import *
from Sales import *
from Stats import *
class Ui_MainWindow1(object):
    def setupUi1(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(799,461)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.bgL = QtWidgets.QLabel(self.centralwidget)
        self.bgL.setGeometry(QtCore.QRect(0, 0, 799, 461))
        self.bgL.setText("")
        self.bgL.setPixmap(QtGui.QPixmap("C:/Users/vinay/Desktop/Xtras/cool-age/bg_wlpr.jpg"))
        self.bgL.setScaledContents(True)
        self.bgL.setObjectName("bgL")
        self.wlcmL = QtWidgets.QLabel(self.centralwidget)
        self.wlcmL.setGeometry(QtCore.QRect(50, 120, 461, 171))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.wlcmL.setFont(font)
        self.wlcmL.setObjectName("wlcmL")
        self.btn1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn1.setGeometry(QtCore.QRect(600, 150, 130, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.btn1.setFont(font)
        self.btn1.setIconSize(QtCore.QSize(16, 16))
        self.btn1.setObjectName("btn1")
        self.btn2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn2.setGeometry(QtCore.QRect(600, 190, 130, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.btn2.setFont(font)
        self.btn2.setIconSize(QtCore.QSize(16, 16))
        self.btn2.setObjectName("btn2")
        self.btn3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn3.setGeometry(QtCore.QRect(600, 230, 130, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.btn3.setFont(font)
        self.btn3.setIconSize(QtCore.QSize(16, 16))
        self.btn3.setObjectName("btn3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")

        self.retranslateUi1(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.btn1.clicked.connect(Ui_MainWindow1.open2)
        self.btn2.clicked.connect(Ui_MainWindow1.open3)
        self.btn3.clicked.connect(Ui_MainWindow1.open4)

    def open1(self):
        ui = Ui_MainWindow1()
        ui.setupUi1(w)
        w.show()

    def open2(self):
        ui = Ui_MainWindow2()
        ui.setupUi2(w)
        w.show()

    def open3(self):
        ui = Ui_MainWindow3()
        ui.setupUi3(w)
        w.show()

    def open4(self):
        ui = Ui_MainWindow4()
        ui.setupUi4(w)
        w.show()

    def pop(self,t):
        msg=QtWidgets.QMessageBox()
        msg.setText(t)
        msg.setWindowTitle("Message")
        msg.setStyleSheet("QLabel{min-width: 270px;min-height: 30px;}")
        msg.exec_()

    def retranslateUi1(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Shop Management Software"))
        self.wlcmL.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">Welcome to Shop</span></p><p align=\"center\"><span style=\" color:#ffffff;\">Management Software</span></p></body></html>"))
        self.btn1.setText(_translate("MainWindow", "Customer Management"))
        self.btn2.setText(_translate("MainWindow", "Item Management"))
        self.btn3.setText(_translate("MainWindow", "Sales"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))

class Ui_MainWindow2(object):
    def setupUi2(self, MainWindow):
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.bgL = QtWidgets.QLabel(self.centralwidget)
        self.bgL.setGeometry(QtCore.QRect(0, 0, 799, 461))
        self.bgL.setText("")
        self.bgL.setPixmap(QtGui.QPixmap("C:/Users/vinay/Desktop/Xtras/cool-age/bg_wlpr.jpg"))
        self.bgL.setScaledContents(True)
        self.bgL.setObjectName("bgL")
        self.nameL = QtWidgets.QLabel(self.centralwidget)
        self.nameL.setGeometry(QtCore.QRect(270, 160, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.nameL.setFont(font)
        self.nameL.setObjectName("nameL")
        self.phoneL = QtWidgets.QLabel(self.centralwidget)
        self.phoneL.setGeometry(QtCore.QRect(270, 120, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.phoneL.setFont(font)
        self.phoneL.setObjectName("phoneL")
        self.emailL = QtWidgets.QLabel(self.centralwidget)
        self.emailL.setGeometry(QtCore.QRect(270, 200, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.emailL.setFont(font)
        self.emailL.setObjectName("emailL")
        self.phoneI = QtWidgets.QLineEdit(self.centralwidget)
        self.phoneI.setGeometry(QtCore.QRect(340, 120, 221, 20))
        self.phoneI.setObjectName("phoneI")
        self.nameI = QtWidgets.QLineEdit(self.centralwidget)
        self.nameI.setGeometry(QtCore.QRect(340, 160, 221, 20))
        self.nameI.setObjectName("nameI")
        self.emailI = QtWidgets.QLineEdit(self.centralwidget)
        self.emailI.setGeometry(QtCore.QRect(340, 200, 221, 20))
        self.emailI.setObjectName("emailI")
        self.operationL = QtWidgets.QLabel(self.centralwidget)
        self.operationL.setGeometry(QtCore.QRect(140, 60, 181, 31))
        self.operationL.setObjectName("operationL")
        self.new_add = QtWidgets.QPushButton(self.centralwidget)
        self.new_add.setGeometry(QtCore.QRect(250, 270, 75, 23))
        self.new_add.setObjectName("new_add")
        self.upd_upd = QtWidgets.QPushButton(self.centralwidget)
        self.upd_upd.setGeometry(QtCore.QRect(380, 270, 75, 23))
        self.upd_upd.setObjectName("upd_upd")
        self.del_del = QtWidgets.QPushButton(self.centralwidget)
        self.del_del.setGeometry(QtCore.QRect(510, 270, 75, 23))
        self.del_del.setObjectName("del_del")
        # self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        # self.pushButton.setGeometry(QtCore.QRect(324, 330, 191, 23))
        # self.pushButton.setObjectName("pushButton")
        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(710, 370, 75, 23))
        self.back.setObjectName("back")
        MainWindow.setCentralWidget(self.centralwidget)

        def addCust():
            if (self.operationL.text()=="<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Add New Customer</span></p></body></html>"):
                if (self.phoneI.text() == "" or self.nameI.text() == ""):
                    Ui_MainWindow1.pop(Ui_MainWindow1, "Please enter values in Mobile and Name fields")
                else:
                    if (self.phoneI.text().isnumeric()==True):
                        phone=int(self.phoneI.text())
                        name=self.nameI.text()
                        email=self.emailI.text()
                        print(phone,name,email)
                        c=Customer(name,phone,email)
                        c.newCustomer(c)
                        self.phoneI.setText("")
                        self.nameI.setText("")
                        self.emailI.setText("")
                        Ui_MainWindow1.pop(Ui_MainWindow1, "Customer Added!!")
                    else:
                        Ui_MainWindow1.pop(Ui_MainWindow1,"Enter a valid Mobile number")
            else:
                self.operationL.setText("<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Add New Customer</span></p></body></html>")
                self.phoneI.setText("")
                self.nameI.setText("")
                self.emailI.setText("")
                self.nameI.setEnabled(True)
                self.emailI.setEnabled(True)

        def updCust():
            if (self.operationL.text()=="<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Update Customer</span></p></body></html>"):
                if (self.phoneI.text() == "" or self.nameI.text() == ""):
                    Ui_MainWindow1.pop(Ui_MainWindow1, "Please enter values in Mobile and Name fields")
                else:
                    if (self.phoneI.text().isnumeric() == True):
                        phone=int(self.phoneI.text())
                        name=self.nameI.text()
                        email=self.emailI.text()
                        print(phone,name,email)
                        c = Customer(name, phone, email)
                        c.updCustomer(c)
                        self.phoneI.setText("")
                        self.nameI.setText("")
                        self.emailI.setText("")
                        Ui_MainWindow1.pop(Ui_MainWindow1, "Customer Record Updated!!")
                    else:
                        Ui_MainWindow1.pop(Ui_MainWindow1,"Enter a valid Mobile number")
            else:
                self.operationL.setText("<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Update Customer</span></p></body></html>")
                self.phoneI.setText("")
                self.nameI.setText("")
                self.emailI.setText("")
                self.nameI.setEnabled(True)
                self.emailI.setEnabled(True)

        def delCust():
            if (self.operationL.text()=="<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Delete Customer</span></p></body></html>"):
                if (self.phoneI.text() == ""):
                    Ui_MainWindow1.pop(Ui_MainWindow1, "Please enter value in Mobile field")
                else:
                    phone=int(self.phoneI.text())
                    print(phone)             #linking files left
                    c = Customer(name, phone, email)
                    c.delCustomer(c)
                    self.phoneI.setText("")
                    Ui_MainWindow1.pop(Ui_MainWindow1, "Customer Deleted!!")

            else:
                self.operationL.setText("<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Delete Customer</span></p></body></html>")
                self.phoneI.setText("")
                self.nameI.setEnabled(False)
                self.emailI.setEnabled(False)
                self.nameI.setText("")
                self.emailI.setText("")

        self.retranslateUi2(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.back.clicked.connect(Ui_MainWindow1.open1)
        self.new_add.clicked.connect(addCust)
        self.upd_upd.clicked.connect(updCust)
        self.del_del.clicked.connect(delCust)

    def retranslateUi2(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Shop Management Software - Customer Management"))
        self.nameL.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#ffffff;\">Name</span></p></body></html>"))
        self.phoneL.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#ffffff;\">Mobile</span></p></body></html>"))
        self.emailL.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#ffffff;\">Email ID</span></p></body></html>"))
        self.operationL.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Add New Customer</span></p></body></html>"))
        self.new_add.setText(_translate("MainWindow", "Add"))
        self.upd_upd.setText(_translate("MainWindow", "Update"))
        self.del_del.setText(_translate("MainWindow", "Delete"))
        # self.pushButton.setText(_translate("MainWindow", "Update from Excel"))
        self.back.setText(_translate("MainWindow", "Back"))


class Ui_MainWindow3(object):
    def setupUi3(self, MainWindow):
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.bgL = QtWidgets.QLabel(self.centralwidget)
        self.bgL.setGeometry(QtCore.QRect(0, 0, 799, 461))
        self.bgL.setText("")
        self.bgL.setPixmap(QtGui.QPixmap("C:/Users/vinay/Desktop/Xtras/cool-age/bg_wlpr.jpg"))
        self.bgL.setScaledContents(True)
        self.bgL.setObjectName("bgL")
        self.priceL = QtWidgets.QLabel(self.centralwidget)
        self.priceL.setGeometry(QtCore.QRect(260, 170, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.priceL.setFont(font)
        self.priceL.setObjectName("priceL")
        self.itemNameL = QtWidgets.QLabel(self.centralwidget)
        self.itemNameL.setGeometry(QtCore.QRect(260, 120, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.itemNameL.setFont(font)
        self.itemNameL.setObjectName("itemNameL")
        self.itemNameI = QtWidgets.QLineEdit(self.centralwidget)
        self.itemNameI.setGeometry(QtCore.QRect(350, 120, 221, 20))
        self.itemNameI.setObjectName("itemNameI")
        self.priceI = QtWidgets.QLineEdit(self.centralwidget)
        self.priceI.setGeometry(QtCore.QRect(350, 170, 221, 20))
        self.priceI.setObjectName("priceI")
        self.operationL = QtWidgets.QLabel(self.centralwidget)
        self.operationL.setGeometry(QtCore.QRect(140, 60, 181, 31))
        self.operationL.setObjectName("operationL")
        self.new_add = QtWidgets.QPushButton(self.centralwidget)
        self.new_add.setGeometry(QtCore.QRect(250, 250, 75, 23))
        self.new_add.setObjectName("new_add")
        self.upd_upd = QtWidgets.QPushButton(self.centralwidget)
        self.upd_upd.setGeometry(QtCore.QRect(380, 250, 75, 23))
        self.upd_upd.setObjectName("upd_upd")
        self.del_del = QtWidgets.QPushButton(self.centralwidget)
        self.del_del.setGeometry(QtCore.QRect(510, 250, 75, 23))
        self.del_del.setObjectName("del_del")
        # self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        # self.pushButton.setGeometry(QtCore.QRect(324, 310, 191, 23))
        # self.pushButton.setObjectName("pushButton")
        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(710, 370, 75, 23))
        self.back.setObjectName("back")
        MainWindow.setCentralWidget(self.centralwidget)

        def addItem():
            if (self.operationL.text()=="<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Add New Item</span></p></body></html>"):
                if (self.itemNameI.text() == "" or self.priceI.text() == ""):
                    Ui_MainWindow1.pop(Ui_MainWindow1, "Please enter values in Item Name and Price fields")
                else:
                    if (self.priceI.text().isnumeric() == True):
                        itemname=self.itemNameI.text()
                        price=int(self.priceI.text())
                        print(itemname,price)
                        cs=Sales()
                        cs.addItem(itemname,price)
                        self.itemNameI.setText("")
                        self.priceI.setText("")
                        Ui_MainWindow1.pop(Ui_MainWindow1, "Item Added!!")
                    else:
                        Ui_MainWindow1.pop(Ui_MainWindow1,"Enter a valid Price value")

            else:
                self.operationL.setText("<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Add New Item</span></p></body></html>")
                self.itemNameI.setText("")
                self.priceI.setText("")
                self.priceI.setEnabled(True)

        def updItem():
            if (self.operationL.text()=="<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Update Item</span></p></body></html>"):
                if (self.itemNameI.text() == "" or self.priceI.text() == ""):
                    Ui_MainWindow1.pop(Ui_MainWindow1, "Please enter values in Item Name and Price fields")
                else:
                    if (self.priceI.text().isnumeric() == True):
                        itemname=self.itemNameI.text()
                        price=self.priceI.text()
                        print(itemname,price)
                        cs = Sales()
                        cs.updItem(itemname, price)
                        self.itemNameI.setText("")
                        self.priceI.setText("")
                        Ui_MainWindow1.pop(Ui_MainWindow1, "Item Updated!!")
                    else:
                        Ui_MainWindow1.pop(Ui_MainWindow1,"Enter a valid Price value")

            else:
                self.operationL.setText("<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Update Item</span></p></body></html>")
                self.itemNameI.setText("")
                self.priceI.setText("")
                self.priceI.setEnabled(True)

        def delItem():
            if (self.operationL.text()=="<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Delete Item</span></p></body></html>"):
                if (self.itemNameI.text() == ""):
                    Ui_MainWindow1.pop(Ui_MainWindow1, "Please enter value in Item Name field")
                else:
                    itemname=self.itemNameI.text()
                    print(itemname)
                    cs = Sales()
                    cs.delItem(itemname)
                    self.itemNameI.setText("")
                    self.priceI.setText("")
                    Ui_MainWindow1.pop(Ui_MainWindow1, "Item Deleted!!")

            else:
                self.operationL.setText("<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Delete Item</span></p></body></html>")
                self.itemNameI.setText("")
                self.priceI.setText("")
                self.priceI.setEnabled(False)
        self.retranslateUi3(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.back.clicked.connect(Ui_MainWindow1.open1)
        self.new_add.clicked.connect(addItem)
        self.upd_upd.clicked.connect(updItem)
        self.del_del.clicked.connect(delItem)


    def retranslateUi3(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Shop Management Software - Item Management"))
        self.priceL.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#ffffff;\">Price</span></p></body></html>"))
        self.itemNameL.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#ffffff;\">Item Name</span></p></body></html>"))
        self.operationL.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Add New Item</span></p></body></html>"))
        self.new_add.setText(_translate("MainWindow", "Add"))
        self.upd_upd.setText(_translate("MainWindow", "Update"))
        self.del_del.setText(_translate("MainWindow", "Delete"))
        # self.pushButton.setText(_translate("MainWindow", "Update from Excel"))
        self.back.setText(_translate("MainWindow", "Back"))

class Ui_MainWindow4(object):
    amount=0
    points=0
    def setupUi4(self, MainWindow):
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.bgL = QtWidgets.QLabel(self.centralwidget)
        self.bgL.setGeometry(QtCore.QRect(0, 0, 799, 461))
        self.bgL.setText("")
        self.bgL.setPixmap(QtGui.QPixmap("C:/Users/vinay/Desktop/Xtras/cool-age/bg_wlpr.jpg"))
        self.bgL.setScaledContents(True)
        self.bgL.setObjectName("bgL")
        self.pointsDispL = QtWidgets.QLabel(self.centralwidget)
        self.pointsDispL.setGeometry(QtCore.QRect(130, 400, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.pointsDispL.setFont(font)
        self.pointsDispL.setObjectName("pointsDispL")
        self.pointsL = QtWidgets.QLabel(self.centralwidget)
        self.pointsL.setGeometry(QtCore.QRect(50, 400, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.pointsL.setFont(font)
        self.pointsL.setObjectName("pointsL")
        self.operationL = QtWidgets.QLabel(self.centralwidget)
        self.operationL.setGeometry(QtCore.QRect(50, 70, 211, 31))
        self.operationL.setObjectName("operationL")
        self.moneyB = QtWidgets.QPushButton(self.centralwidget)
        self.moneyB.setGeometry(QtCore.QRect(40, 40, 111, 23))
        self.moneyB.setObjectName("moneyB")
        self.pointsB = QtWidgets.QPushButton(self.centralwidget)
        self.pointsB.setGeometry(QtCore.QRect(160, 40, 111, 23))
        self.pointsB.setObjectName("pointsB")
        self.addItemB = QtWidgets.QPushButton(self.centralwidget)
        self.addItemB.setGeometry(QtCore.QRect(50, 360, 75, 23))
        self.addItemB.setObjectName("addItemB")
        self.confirmPurchaseB = QtWidgets.QPushButton(self.centralwidget)
        self.confirmPurchaseB.setGeometry(QtCore.QRect(140, 360, 121, 23))
        self.confirmPurchaseB.setObjectName("confirmPurchaseB")
        self.itemDropDown = QtWidgets.QComboBox(self.centralwidget)
        self.itemDropDown.setGeometry(QtCore.QRect(50, 120, 211, 22))
        self.itemDropDown.setObjectName("itemDropDown")
        self.itemDropDown.addItem("")
        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(710, 370, 75, 23))
        self.back.setObjectName("back")
        self.selectTE = QtWidgets.QTextEdit(self.centralwidget)
        self.selectTE.setEnabled(False)
        self.selectTE.setGeometry(QtCore.QRect(270, 120, 201, 231))
        self.selectTE.setObjectName("selectTE")
        self.selectL = QtWidgets.QLabel(self.centralwidget)
        self.selectL.setGeometry(QtCore.QRect(270, 90, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.selectL.setFont(font)
        self.selectL.setObjectName("selectL")
        self.pointsL_2 = QtWidgets.QLabel(self.centralwidget)
        self.pointsL_2.setGeometry(QtCore.QRect(50, 330, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.pointsL_2.setFont(font)
        self.pointsL_2.setObjectName("pointsL_2")
        self.pointsDispL_2 = QtWidgets.QLabel(self.centralwidget)
        self.pointsDispL_2.setGeometry(QtCore.QRect(130, 330, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.pointsDispL_2.setFont(font)
        self.pointsDispL_2.setObjectName("pointsDispL_2")
        self.custNoL = QtWidgets.QLabel(self.centralwidget)
        self.custNoL.setGeometry(QtCore.QRect(50, 300, 81, 21))
        self.custNoL.setFont(font)
        self.custNoL.setObjectName("custNoL")
        self.custNoI = QtWidgets.QLineEdit(self.centralwidget)
        self.custNoI.setGeometry(QtCore.QRect(130, 300, 131, 21))
        self.custNoI.setObjectName("custNoI")
        self.custStatsB = QtWidgets.QPushButton(self.centralwidget)
        self.custStatsB.setGeometry(QtCore.QRect(580, 120, 161, 23))
        self.custStatsB.setObjectName("custStatsB")
        self.statsL = QtWidgets.QLabel(self.centralwidget)
        self.statsL.setGeometry(QtCore.QRect(580, 90, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.statsL.setFont(font)
        self.statsL.setObjectName("statsL")
        self.salesStatsB = QtWidgets.QPushButton(self.centralwidget)
        self.salesStatsB.setGeometry(QtCore.QRect(580, 150, 161, 23))
        self.salesStatsB.setObjectName("salesStatsB")
        self.statsL_2 = QtWidgets.QLabel(self.centralwidget)
        self.statsL_2.setGeometry(QtCore.QRect(580, 200, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.statsL_2.setFont(font)
        self.statsL_2.setObjectName("statsL_2")
        self.salesPredB = QtWidgets.QPushButton(self.centralwidget)
        self.salesPredB.setGeometry(QtCore.QRect(580, 230, 161, 23))
        self.salesPredB.setObjectName("salesPredB")
        self.excelB = QtWidgets.QPushButton(self.centralwidget)
        self.excelB.setGeometry(QtCore.QRect(580, 310, 161, 23))
        self.excelB.setObjectName("excelB")
        self.statsL_3 = QtWidgets.QLabel(self.centralwidget)
        self.statsL_3.setGeometry(QtCore.QRect(580, 280, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.statsL_3.setFont(font)
        self.statsL_3.setObjectName("statsL_3")
        MainWindow.setCentralWidget(self.centralwidget)

        def moneyP():
            self.amount=0
            self.points=0
            self.operationL.setText("<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Money Purchase</span></p></body></html>")
            self.selectTE.setText("")
            self.pointsDispL_2.setText("<html><head/><body><p><span style=\" font-weight:600; color:#ffffff;\">0</span></p></body></html>")
            self.pointsDispL.setText("<html><head/><body><p><span style=\" font-weight:600; color:#ffffff;\">0</span></p></body></html>")
            self.amount=0
            self.points=0
        def pointP():
            self.amount=0
            self.points=0
            self.operationL.setText("<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Points Purchase</span></p></body></html>")
            self.selectTE.setText("")
            self.pointsDispL_2.setText("<html><head/><body><p><span style=\" font-weight:600; color:#ffffff;\">0</span></p></body></html>")
            self.pointsDispL.setText("<html><head/><body><p><span style=\" font-weight:600; color:#ffffff;\">0</span></p></body></html>")
            self.amount = 0
            self.points = 0
        def addfromCombo():
            cs=Sales()
            price=cs.getItemPrice(str(self.itemDropDown.currentText()))
            self.selectTE.setText(self.selectTE.toPlainText() + str(self.itemDropDown.currentText()) + "\t"+str(price)+"\n")
            self.amount=self.amount+price
            self.pointsDispL_2.setText("<html><head/><body><p><span style=\" font-weight:600; color:#ffffff;\">{}</span></p></body></html>".format(self.amount))

        def confirmPurchase():
            final_amount=self.amount
            if(self.operationL.text()=="<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Money Purchase</span></p></body></html>"):
                if (self.custNoI.text() == "" or self.custNoI.text().isnumeric()== False):
                    Ui_MainWindow1.pop(Ui_MainWindow1, "Please enter valid value in Mobile field")
                else:
                    phone = int(self.custNoI.text())
                    s=Sales()
                    Ui_MainWindow1.pop(Ui_MainWindow1, s.mnyPurchase(phone,final_amount))
                    self.points=s.pntUpdate(final_amount,phone)
                    self.pointsDispL.setText("<html><head/><body><p><span style=\" font-weight:600; color:#ffffff;\">{}</span></p></body></html>".format(self.points))
            else:
                if (self.custNoI.text() == "" or self.custNoI.text().isnumeric()== False):
                    Ui_MainWindow1.pop(Ui_MainWindow1, "Please enter valid value in Mobile field")
                else:
                    phone = int(self.custNoI.text())
                    s = Sales()
                    aa=s.pntPurchase(phone, final_amount)
                    Ui_MainWindow1.pop(Ui_MainWindow1,aa[0])
                    self.pointsDispL.setText(
                        "<html><head/><body><p><span style=\" font-weight:600; color:#ffffff;\">{}</span></p></body></html>".format(
                            aa[1]))

        def csvfunction():
            Stats.exportCSV(Stats)
            Ui_MainWindow1.pop(Ui_MainWindow1, "Files have been imported to your system!!")



        cs = Sales()
        items = cs.allItem()
        items1=[]
        i=0
        while(i<len(items)):
            items1.insert(0,items[i][0])
            i=i+1
        print(items1)
        self.itemDropDown.clear()
        self.itemDropDown.addItems(items1)
        self.retranslateUi4(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.back.clicked.connect(Ui_MainWindow1.open1)
        self.moneyB.clicked.connect(moneyP)
        self.pointsB.clicked.connect(pointP)
        self.addItemB.clicked.connect(addfromCombo)
        self.confirmPurchaseB.clicked.connect(confirmPurchase)
        self.custStatsB.clicked.connect(Stats.customerStats)
        self.salesStatsB.clicked.connect(Stats.salesStats)
        self.salesPredB.clicked.connect(Stats.salePredicition)
        self.excelB.clicked.connect(csvfunction)

    def retranslateUi4(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Shop Management Software - Sales"))
        self.pointsDispL.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#ffffff;\">0</span></p></body></html>"))
        self.pointsL.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#ffffff;\">Points Left</span></p></body></html>"))
        self.operationL.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Money Purchase</span></p></body></html>"))
        self.moneyB.setText(_translate("MainWindow", "Money Purchase"))
        self.pointsB.setText(_translate("MainWindow", "Points Purchase"))
        self.addItemB.setText(_translate("MainWindow", "Add"))
        self.confirmPurchaseB.setText(_translate("MainWindow", "Confirm Purchase"))
        self.back.setText(_translate("MainWindow", "Back"))
        self.selectL.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#ffffff;\">Items Selected</span></p></body></html>"))
        self.pointsL_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#ffffff;\">Amount</span></p></body></html>"))
        self.custNoL.setText(_translate("MainWindow","<html><head/><body><p><span style=\" font-weight:600; color:#ffffff;\">Mobile</span></p></body></html>"))
        self.pointsDispL_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#ffffff;\">0</span></p></body></html>"))
        self.custStatsB.setText(_translate("MainWindow", "Customer Stats"))
        self.statsL.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#ffffff;\">Stats</span></p></body></html>"))
        self.salesStatsB.setText(_translate("MainWindow", "Sales Stats"))
        self.statsL_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#ffffff;\">Predictions</span></p></body></html>"))
        self.salesPredB.setText(_translate("MainWindow", "Sales Prediciton"))
        self.excelB.setText(_translate("MainWindow", "Get Excel Files"))
        self.statsL_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#ffffff;\">Excel Files</span></p></body></html>"))

app=QApplication(sys.argv)
w=QMainWindow()
ui=Ui_MainWindow1()
ui.setupUi1(w)
w.show()
sys.exit(app.exec_())