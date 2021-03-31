import MySQLdb

MySQLdb.apilevel = '1.0'
db = MySQLdb.connect(user="usuario",passwd="usuario",db="treinaweb_clientes",host="localhost",port=3306,autocommit=True)
print("conectado")
db.close()
