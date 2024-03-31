import mysql.connector as conn

mydb = conn.connect(host="localhost" , user = "root" , passwd = "shubham1250")
cursor = mydb.cursor()
cursor.execute("select employee_id , emp_mailid from shubham.ineuron")
l=[]
for i in cursor.fetchall():
    l.append(i)

print(l)
print(type(l[0]))