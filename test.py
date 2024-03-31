import mysql.connector as conn

mydb = conn.connect(host="localhost" , user = "root" , passwd = "shubham1250")
print(mydb)
cursor = mydb.cursor()
#cursor.execute("create database shubham")
cursor.execute("show databases")

