import os

class Usuario:
    def __init__(self, nome, nickname, senha):
        self.nome = nome
        self. nickname = nickname
        self.senha = senha

usuario1 = Usuario('Hugo', 'guhzoide', 'bumbum')
usuario2 = Usuario('Roberto', 'betinho', '1234')
usuario3 = Usuario('Jonas', 'toba', 'teste')

usuarios = {usuario1.nickname : usuario1,
            usuario2.nickname : usuario2,
            usuario3.nickname : usuario3}

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome=nome
        self.categoria=categoria 
        self.console=console
    
jogo1 = Jogo('Tetris', 'Puzzle', 'Atari')
jogo2 = Jogo('God of War', 'Rack n Slash', 'PS2')
jogo3 = Jogo('Mortal Kombta', 'Luta', 'PS2')

lista = [jogo1, jogo2, jogo3]
