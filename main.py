import MySQLdb

MySQLdb.apilevel = '1.0'
db = MySQLdb.connect(user="usuario", passwd="senha", db="nome_DB", host="localhost", port=3306,
                     autocommit=True)
print("conectado")

cursor = db.cursor()
cursor.execute("SELECT * FROM cliente")
print(cursor.fetchall())   # todos as consultas
print(cursor.fetchone())   # apenas a primeira consulta
print(cursor.fetchmany())  # passar a quantidade de consultas
db.close()
