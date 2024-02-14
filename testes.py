import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

senha = '12345'
nickname = 'guhzoide'

nome = 'Forza Horazon 5'
categoria = 'Corrida'
console = 'PC/Xbox series'

host = os.getenv('host')
user = os.getenv('user')
password = os.getenv('password')
database = os.getenv('database')
port = os.getenv('port')

con = psycopg2.connect(host=host, user=user, password=password, database=database, port=port)
cursor = con.cursor()
cursor.execute(f"SELECT * FROM jogos WHERE nome='{nome}' AND categoria='{categoria}' AND console='{console}';")
dados = cursor.fetchall()

if dados:
    print('Parece que deu boa')
else:
    try:
        cursor.execute(f"INSERT INTO jogos (nome, categoria, console) VALUES ('{nome}', '{categoria}', '{console}');")
        con.commit()
        cursor.close()
        con.close()
        print('Jogo adcionado')
    except Exception as error:
        print(error) 