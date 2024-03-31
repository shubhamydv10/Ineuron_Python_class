import mysql.connector as conn

mydb = conn.connect(host="localhost" , user = "root" , passwd = "shubham1250")
print(mydb)
cursor = mydb.cursor()

#q1 = cursor.execute("create table shubham.ineuron(employee_id int(10) , emp_name varchar(80) , emp_mailid varchar(80) , emp_salary int(6) , emp_attendence int(3))")
q2 = cursor.execute("select * from shubham.ineuron")
print(q2)