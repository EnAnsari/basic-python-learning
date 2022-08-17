import sqlite3
connection = sqlite3.connect('./my-database.db')
cursor = connection.cursor()

sql = """
    DELETE FROM user WHERE userId = 1
"""

cursor.execute(sql)
# cursor.executescript(sql)
connection.commit()
connection.close()