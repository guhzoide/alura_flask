class Usuario:
    def __init__(self, nome, nickname, senha):
        self.nome = nome
        self. nickname = nickname
        self.senha = senha

usuario1 = Usuario('Hugo', 'guhzoide', 'bumbum')
usuario2 = Usuario('Roberto', 'betinho', '1234')
usuario3 = Usuario('Jonas', 'toba', 'teste')

usuarios = {usuario1.nome : usuario1,
            usuario2.nickname : usuario2,
            usuario3.nickname : usuario3}


nome = input('Nome\n')
passs = 'bumbum'

if passs == usuarios[nome].senha:
    print('Mais facil')