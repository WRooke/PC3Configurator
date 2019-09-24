import pyodbc

conn = pyodbc.connect(
    r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\williamr\OneDrive - OEM TECHNOLOGY SOLUTIONS PTY LTD\Systems\PC3Configurator\PC3Config.accdb;')
cursor = conn.cursor()
cursor.execute('select PCA_Name from PC3_PCA where DO=8')

for row in cursor.fetchall():
    print(row)