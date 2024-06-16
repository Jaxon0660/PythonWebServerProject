import sqlite3

connect =  sqlite3.connect("database.db")

# Ctrl + / to comment out multiple lines               
# connect.execute(''' Create Table Customer
#                 (ID INT PRIMARY KEY NOT NULL,
#                 NAME TEXT NOT NULL, 
#                 AGE INT NOT NULL);''')

connect.execute("INSERT INTO CUSTOMER(ID, NAME,AGE)\
                VALUES(1,'TOMI',99)")
connect.execute("INSERT INTO CUSTOMER(ID, NAME,AGE)\
                VALUES(2,'TIM',29)")

all_data = connect.execute('''SELECT * FROM CUSTOMER''')

for row in all_data:
    print(row)


connect.close()