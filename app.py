from models import *
from flask import Flask, render_template, request, redirect, session, flash, url_for


@app.route('/')
def index():
    lista = Jogos.busca_jogos()
    return render_template('lista.html', titulo='Jogos', jogos=lista)

@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('novo')))
    return render_template('novo.html', titulo='Novo Jogo')

@app.route('/criar', methods=['POST', 'GET'])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']

    result = Jogos.inserir_jogos(nome, categoria, console)
    flash(result)
    return redirect(url_for('index'))

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)

@app.route('/autenticar', methods=['POST',])
def autenticar():
    nickname = request.form['usuario']
    senha = request.form['senha']
    proxima_pagina = request.form['proxima']
    result = Usuarios.usuarios(nickname,senha)

    if result:
        session['usuario_logado'] = nickname
        flash(f"Bem vindo, {nickname}!")
        return redirect(proxima_pagina)

    flash("Login inválido")
    return redirect(proxima_pagina)

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso!')
    return redirect(url_for('index'))

app.run(port=5025, host='localhost', debug=True)