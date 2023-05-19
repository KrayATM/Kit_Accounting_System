import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="kit-accounting-db"
)

mycursor = db.cursor()

# Uncomment the line below if the table doesn't exist yet and you want to create it
mycursor.execute("CREATE TABLE Person (name VARCHAR(50), age smallint UNSIGNED, personID int PRIMARY KEY AUTO_INCREMENT)")

# Use executemany() to insert multiple rows
values = [("Pearl", 23), ("Kgothatso", 24), ("Kenosi", 25), ("Zamo", 26)]
mycursor.executemany("INSERT INTO Person (name, age) VALUES (%s, %s)", values)

db.commit()

mycursor.execute("SELECT * FROM Person")

for x in mycursor:
    print(x)