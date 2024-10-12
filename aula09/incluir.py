import mysql.connector
# Informações de conexão
mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="ceub123456",
  database="bd_planejamento"
)

# entrada de dados
funcao = input('Qual a Função?')
diaria = float(input('Qual o valor da diária?'))

cmd = 'INSERT INTO tb_funcao VALUES(DEFAULT, %s, %s)'
mycursor = mydb.cursor()
mycursor.execute(cmd, (funcao, diaria))
mydb.commit()

print('Concluido com sucesso!')

mycursor.close()
mydb.close()
