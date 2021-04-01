import MySQLdb

MySQLdb.apilevel = '1.0'
db = MySQLdb.connect(user="usuario",passwd="senha",db="nome_DB",host="localhost",port=3306,autocommit=True)
print("conectado")
db.close()
