import os
import psycopg2
from models import *
from flask import Flask
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")
host = os.getenv('host')
user = os.getenv('user')
password = os.getenv('password')
database = os.getenv('database')
port = os.getenv('port')

class Jogos():
    def busca_jogos():
        lista_jogos = []
        con = psycopg2.connect(host=host, user=user, password=password, database=database, port=port)
        cursor = con.cursor()
        cursor.execute(f"SELECT nome, categoria, console FROM jogos;")
        dados = cursor.fetchall()
        cursor.close()
        con.close()
        for line in dados:
            lista_jogos.append(line)

        return lista_jogos
    
    def inserir_jogos(nome, categoria, console):
        con = psycopg2.connect(host=host, user=user, password=password, database=database, port=port)
        cursor = con.cursor()
        cursor.execute(f"SELECT * FROM jogos WHERE nome='{nome}';")
        dados = cursor.fetchall()

        if dados:
            return 'Já existe um jogo com esse nome'
        try:
            cursor.execute(f"INSERT INTO jogos (nome, categoria, console) VALUES ('{nome}', '{categoria}', '{console}');")
            con.commit()
            cursor.close()
            con.close()
            return 'Jogo adcionado'
        except Exception as error:
            return error

    
class Usuarios():
    def usuarios(nickname,senha):
        con = psycopg2.connect(host=host, user=user, password=password, database=database, port=port)
        cursor = con.cursor()
        cursor.execute(f"SELECT senha FROM usuarios WHERE nickname='{nickname}';")
        senha_banco = cursor.fetchall()
        cursor.close()
        con.close()


        for teste in senha_banco:
            if senha in teste:
                return True