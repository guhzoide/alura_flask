import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

senha = '12345'
nickname = 'guhzoide'

host = os.getenv('host')
user = os.getenv('user')
password = os.getenv('password')
database = os.getenv('database')
port = os.getenv('port')

con = psycopg2.connect(host="localhost", user="postgres", password="123456", database="postgres", port='5432')
cursor = con.cursor()
cursor.execute(f"SELECT senha FROM usuarios WHERE nickname='{nickname}';")
senha_banco = cursor.fetchall()
cursor.close()
con.close()


for teste in senha_banco:
    if senha in teste:
        print('eita')

nome = 'Cyberpunk 2077'
categoria = 'RPG'
console = 'PC'
con = psycopg2.connect(host=host, user=user, password=password, database=database, port=port)
cursor = con.cursor()
cursor.execute(f"INSERT INTO jogos (nome, categoria, console) VALUES ('{nome}', '{categoria}', '{console}');")
con.commit()
cursor.close()
con.close()
