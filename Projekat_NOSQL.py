# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Projekat_NOSQL.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from functions import getDatabases, getTables, setActiveDatabase, getTableData

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1440, 900)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(10, 20, 741, 521))
        self.widget.setObjectName("widget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.widget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 721, 501))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.verticalLayoutWidget)
        self.tabWidget.setObjectName("tabWidget")
        self.Connection = QtWidgets.QWidget()
        self.Connection.setObjectName("Connection")
        self.pushButton = QtWidgets.QPushButton(self.Connection)
        self.pushButton.setGeometry(QtCore.QRect(0, 100, 711, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_8 = QtWidgets.QPushButton(self.Connection)
        self.pushButton_8.setGeometry(QtCore.QRect(0, 200, 711, 32))
        self.pushButton_8.setObjectName("pushButton_8")
        self.tabWidget.addTab(self.Connection, "")
        self.Databases = QtWidgets.QWidget()
        self.Databases.setObjectName("Databases")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.Databases)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 711, 71))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.pushButton_7 = QtWidgets.QPushButton(self.Databases)
        self.pushButton_7.setGeometry(QtCore.QRect(0, 80, 711, 31))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_9 = QtWidgets.QPushButton(self.Databases)
        self.pushButton_9.setGeometry(QtCore.QRect(0, 120, 711, 31))
        self.pushButton_9.setObjectName("pushButton_9")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.Databases)
        self.tableWidget_2.setGeometry(QtCore.QRect(0, 160, 711, 311))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.tabWidget.addTab(self.Databases, "")
        self.Data = QtWidgets.QWidget()
        self.Data.setObjectName("Data")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.Data)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(0, 20, 711, 61))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget_3)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_3.addWidget(self.comboBox)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.comboBox_2 = QtWidgets.QComboBox(self.horizontalLayoutWidget_3)
        self.comboBox_2.setObjectName("comboBox_2")
        self.horizontalLayout_3.addWidget(self.comboBox_2)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.Data)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(0, 80, 711, 71))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_6 = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_4.addWidget(self.pushButton_6)
        self.pushButton_5 = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_4.addWidget(self.pushButton_5)
        self.pushButton_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_4.addWidget(self.pushButton_4)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_4.addWidget(self.pushButton_2)
        self.tableWidget = QtWidgets.QTableWidget(self.Data)
        self.tableWidget.setGeometry(QtCore.QRect(10, 160, 691, 301))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tabWidget.addTab(self.Data, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(360, 540, 47, 13))
        self.label_4.setObjectName("label_4")
        self.comboBox_3 = QtWidgets.QComboBox(Dialog)
        self.comboBox_3.setGeometry(QtCore.QRect(40, 10, 681, 16))
        self.comboBox_3.setObjectName("comboBox_3")

        ### Punimo baze u Combobox 1
        databases = getDatabases()
        for database in databases:
            self.comboBox.addItem(database[0])
    
        ### Biramo bazu 
        def getSelectedDatabase():
            selectedDatabase = self.comboBox.currentText()
            onSelectedDatabase(selectedDatabase)

        self.comboBox.activated.connect(getSelectedDatabase)

        def onSelectedDatabase(imeBaze):
            ## ocisti listu
            self.comboBox_2.clear()

            ## dodaj trenutnu
            setActiveDatabase(imeBaze)
            tables = getTables()
            for table in tables:
                self.comboBox_2.addItem(table[0])


        ### Biramo tabelu
        def getSelectedTable():
            selectedTable = self.comboBox_2.currentText()
            onSelectedTable(selectedTable)

        self.comboBox_2.activated.connect(getSelectedTable)

        def onSelectedTable(imeTabele):
            ### povucemo data za trazeni table
            data = getTableData(imeTabele)
            print(data)
            

            num_rows = len(data)
            # num_cols = len(columns) -- replace with column length
            num_cols = 2

            self.tableWidget.setRowCount(num_rows)
            self.tableWidget.setColumnCount(num_cols)

            
            # self.tableWidget.setHorizontalHeaderLabels(columns)
            print('--------------')
            self.tableWidget.setHorizontalHeaderLabels(['id', 'ime', 'prezime'])            
            for row in range(num_rows):
                for column in range(num_cols):
                    print(row, column)
                    print(str(data[row][column]))
                    self.tableWidget.setItem(row, column, QtWidgets.QTableWidget(str(data[row][column)))

    
        # self.pushButton_8.clicked.connect(load)
        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Load config"))
        self.pushButton_8.setText(_translate("Dialog", "Connect"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Connection), _translate("Dialog", "Connection"))
        self.label.setText(_translate("Dialog", "Enter Database Name"))
        self.pushButton_7.setText(_translate("Dialog", "Create Database"))
        self.pushButton_9.setText(_translate("Dialog", "Delete Database"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Databases), _translate("Dialog", "Databases"))
        self.label_2.setText(_translate("Dialog", "Database:"))
        self.label_3.setText(_translate("Dialog", "Collection:"))
        self.pushButton_6.setText(_translate("Dialog", "Insert"))
        self.pushButton_5.setText(_translate("Dialog", "Update Selected"))
        self.pushButton_4.setText(_translate("Dialog", "Delete Selected"))
        self.pushButton_2.setText(_translate("Dialog", "Get All"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Data), _translate("Dialog", "Data"))
        self.label_4.setText(_translate("Dialog", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

