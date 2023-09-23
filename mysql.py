import pymysql

cnx=pymysql.connect(user='root',passwd='Aparticipant1224',\
        host='localhost',database='data_temp')

cursor=cnx.cursor()
query="select * from student"
cursor.execute(query)

for row in cursor:
    print(row)

cursor.close()
cnx.close()
