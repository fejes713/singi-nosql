import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

def getDatabases():
    mycursor = mydb.cursor()
    mycursor.execute("SHOW DATABASES")
    dbs = mycursor.fetchall()
    return dbs

def setActiveDatabase(databaseName):
    mycursor = mydb.cursor()
    mycursor.execute("USE " + databaseName)

def getTables():
    mycursor = mydb.cursor()
    mycursor.execute("SHOW TABLES")
    tables = mycursor.fetchall()
    return tables

def getTableData(tableName):
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM " + tableName)
    data =  mycursor.fetchall()
    return data