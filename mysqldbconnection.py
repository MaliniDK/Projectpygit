import mysql.connector# importing mysql

mydb=mysql.connector.connect(host="localhost",user="root",passwd="Malinidk@123",
auth_plugin='mysql_native_password',database="py") #conneting to the db

db1=mydb.cursor()# it will point to that perticular db
db1.execute("select * from student") #command to fetch the query

result1=db1.fetchall() #fething all ele
#result1=db1.fetchone() # Fetching one ele
print(result1)#Result will be in list
'''
with open("m1.txt","a") as f:
    f.write(result1[0][0]+' '+result1[0][1]+'\n') # Uused to write one values at a time
  
with open("m1.txt","a") as f:
    f.write(result1[1][0]+' '+result1[1][1]+'\n') '''

for i in result1:
    print(i)
    with open("m1.txt","a") as f:
        f.write(i[0]+' '+i[1]+'\n')#Result will print one line by line(tuple)

    
