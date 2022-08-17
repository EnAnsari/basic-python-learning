import sqlite3
connection = sqlite3.connect('./my-database.db')
cursor = connection.cursor()

sql = """
    SELECT * FROM user
"""

# sql = """
#     SELECT * FROM user WHERE userId = 2
# """

# sql = """
#     SELECT * FROM user WHERE email LIKE "%gmail%"
# """

cursor.execute(sql)
for product in cursor:
    print(product)