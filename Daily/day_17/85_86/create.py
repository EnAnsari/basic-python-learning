import sqlite3
connection = sqlite3.connect('./my-database.db')
cursor = connection.cursor()

sql = """
    CREATE TABLE IF NOT EXISTS user(
        userId INTERGER,
        name VARCHAR(60),
        family VARCHAR(60),
        email VARCHAR(60)
    );
"""

cursor.execute(sql)
connection.commit()
connection.close()