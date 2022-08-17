import sqlite3
connection = sqlite3.connect('./my-database.db')
cursor = connection.cursor()

sql = """
    UPDATE user SET name = "Ali" WHERE userId = 3
"""

cursor.execute(sql)
# cursor.executescript(sql)
connection.commit()
connection.close()