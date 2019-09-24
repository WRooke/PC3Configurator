import pyodbc

conn = pyodbc.connect(
    r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\williamr\OneDrive - OEM TECHNOLOGY SOLUTIONS PTY LTD\Systems\Configurer\PC3Config.accdb;')
cursor = conn.cursor()
cursor.execute('select * from table name')

for row in cursor.fetchall():
    print(row)