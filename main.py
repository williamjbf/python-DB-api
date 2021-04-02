import MySQLdb

MySQLdb.apilevel = '1.0'
db = MySQLdb.connect(user="root", passwd="will2410", db="treinaweb_clientes", host="localhost", port=3306,
                     autocommit=False)
print("conectado")

cursor = db.cursor()
try:
    db.begin()
    cursor.execute("INSERT INTO cliente (nome, idade) VALUES('José',25)")
    cursor.execute("INSERT INTO cliente (nome, idade) VALUES('Maria',25)")
    db.commit()
except:
    db.rollback()

cursor.execute("SELECT * FROM cliente")
print(cursor.fetchall())
print(cursor.lastrowid)

cursor.execute("UPDATE cliente SET nome='Ana' WHERE idcliente=2")
cursor.execute("SELECT * FROM cliente")
print(cursor.fetchmany(50))

cursor.execute("DELETE FROM cliente WHERE idcliente=2")
cursor.execute("SELECT * FROM cliente")
print(cursor.fetchall())
db.close()
