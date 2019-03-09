import mysql.connector

#connecting to a database
con = mysql.connector.connect(
    host = "husseinmac",
    user = "root",
    password = "password",
    database = "husseindb",
    port = 3306
)

print("Hey, I think I'm connected")

#cursor 
cur = con.cursor()
#insert a new row

for i in range(100):
    cur.execute("INSERT INTO employees (ID, NAME) VALUES (%s, %s)", (i+10, f'Mark{i}' ))

#execute the query
cur.execute("SELECT ID,NAME FROM employees")

#cur.execute("SELECT ID,NAME FROM employees where NAME = %s", ("Yara",))

rows = cur.fetchall()

for r in rows:
    print(f" ID = {r[0]} NAME = {r[1]}")

#commit the transaction
con.commit()

#close the cursor
cur.close()
#close the connection
con.close()
