import os
from app import *
from flask_wtf import FlaskForm
from wtforms import StringField, validators, SubmitField, PasswordField

class FormularioJogo(FlaskForm):
    nome = StringField('Nome do jogo', [validators.data_required(), validators.length(min=3, max=50)])
    categoria = StringField('Categoria', [validators.data_required(), validators.length(min=2, max=40)])
    console = StringField('Console', [validators.data_required(), validators.length(min=2, max=20)])

    salvar = SubmitField('Salvar')

class FormularioUsuario(FlaskForm):
    nickname = StringField('Nickname', [validators.data_required(), validators.length(min=1, max=8)])
    senha = PasswordField('Senha', [validators.data_required(), validators.length(min=1, max=100)])

    login = SubmitField('Login')

class Help():
    def recupera_imagem(id):
        for nome_arquivo in os.listdir(app.config['UPLOAD_PATH']):
            if f'capa_{id}' in nome_arquivo:
                return nome_arquivo
            
        return 'capa_padrao.jpg'

    def deleta_arquivo(id):
        arquivo = Help.recupera_imagem(id)
        if arquivo != 'capa_padrao.jpg':
            os.remove(os.path.join(app.config['UPLOAD_PATH'], arquivo))