from app import app
from views_games import *
from models import Usuarios
from flask_bcrypt import check_password_hash
from helpers import FormularioUsuario
from flask import render_template, request, redirect, session, flash, url_for

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    form = FormularioUsuario()
    return render_template('login.html', proxima=proxima, form=form)

@app.route('/autenticar', methods=['POST',])
def autenticar():
    form = FormularioUsuario(request.form)

    nickname = form.nickname.data
    senha_formulario = form.senha.data
    proxima_pagina = request.form['proxima']
    usuario = Usuarios.query.filter_by(nickname=nickname).first()
    senha_banco = check_password_hash(usuario.senha, senha_formulario)

    if usuario and senha_banco:
        session['usuario_logado'] = nickname
        flash(f'Bem-vindo(a) {nickname}!')
        return redirect(proxima_pagina)
        
    else:
        flash("Login inválido")
        return redirect(proxima_pagina)

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso!')
    return redirect(url_for('index'))