import sqlite3
connection = sqlite3.connect('./my-database.db')
cursor = connection.cursor()

sql = """
    INSERT INTO user VALUES(1, "Rahmat", "Ansari", "En.Ansari@outlook.com");
    INSERT INTO user VALUES(2, "Davud", "Rajaee", "mdvr@gmail.com");
    INSERT INTO user VALUES(3, "Reza", "Mohammadi", "Reza@mohammadi.com");
"""

# cursor.execute(sql)
cursor.executescript(sql)
connection.commit()
connection.close()