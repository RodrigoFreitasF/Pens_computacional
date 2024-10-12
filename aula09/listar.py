import mysql.connector
# Informações de conexão
mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="ceub123456",
  database="bd_planejamento"
)
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM tb_funcao;")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
mydb.close()
