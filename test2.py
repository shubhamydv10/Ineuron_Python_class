import mysql.connector as conn

mydb = conn.connect(host="localhost" , user = "root" , passwd = "shubham1250")
cursor = mydb.cursor()
s = "insert into shubham.ineuron values(101,'shudhanshu kumar' , 'shudhanshu@ineuron.ai' , 100 , 30)"
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)                     #multiple execution to insert same data multiple times
cursor.execute(s)
mydb.commit()
cursor.execute("select * from shubham.ineuron")
for i in cursor.fetchall():
    print(i)