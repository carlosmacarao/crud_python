import mysql.connector

conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'db_crud',
)

cursor = conexao.cursor()

#CRUD

nome_produto = 'iPhone'
valor = 3250

comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'
cursor.execute(comando)
conexao.commit() # Quando edita o DB

#resultado = cursor.fetchall() # Para ler o DB

cursor.close()
conexao.close()

#CREATE

#READ

#UPDATE

#DELETE