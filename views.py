from app import app, db
from models import Jogos, Usuarios
from flask import render_template, request, redirect, session, flash, url_for

@app.route('/')
def index():
    lista = Jogos.query.order_by(Jogos.id)
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

    jogo = Jogos.query.filter_by(nome=nome).first()

    if jogo:
        flash("Este jogo já consta no banco de dados")
        return redirect(url_for('index'))

    else:
        novo_jogo = Jogos(nome=nome, categoria=categoria, console=console)
        db.session.add(novo_jogo)
        db.session.commit()
        return redirect(url_for('index'))

@app.route('/editar')
def editar():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('editar')))
    return render_template('editar.html', titulo='Editando Jogo')

@app.route('/atualizar', methods=['POST', 'GET'])
def atualizar():
    pass

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)

@app.route('/autenticar', methods=['POST',])
def autenticar():
    nickname = request.form['usuario']
    senha = request.form['senha']
    proxima_pagina = request.form['proxima']
    usuario = Usuarios.query.filter_by(nickname=nickname).first()

    if usuario:
        session['usuario_logado'] = nickname
        return redirect(proxima_pagina)
        
    else:
        flash("Login inválido")
        return redirect(proxima_pagina)

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso!')
    return redirect(url_for('index'))

app.run(port=5025, host='localhost', debug=True)