from ecommerce import app
from flask import render_template, redirect, url_for, flash
from ecommerce.models import Item, User
from ecommerce.forms import CadastroForm, LoginForm
from ecommerce import db
from flask_login import login_user, logout_user, login_required


@app.route('/')
def page_home():
    return render_template("home.html")


@app.route('/produtos')
@login_required
def page_produtos():

    itens = Item.query.all()
    return render_template("produtos.html", itens=itens)


@app.route('/cadastro', methods=['GET', 'POST'])
def page_cadastro():
    form = CadastroForm()
    if form.validate_on_submit():
        usuario = User(
            usuario = form.usuario.data,
            email = form.email.data,
            senhacrip = form.senha1.data
        )
        db.session.add(usuario)
        db.session.commit()
        return redirect(url_for('page_produtos'))
    if form.errors != {}:
        for error in form.errors.values():
            flash(f'Erro ao cadastrar {error}', category='danger')

    return render_template("cadastro.html", form=form)


@app.route('/login', methods=['GET', 'POST'])
def page_login():
    form = LoginForm()
    if form.validate_on_submit():
        usuario_logado = User.query.filter_by(usuario=form.usuario.data).first()
        if usuario_logado and usuario_logado.converte_senha(senha_texto_claro=form.senha.data):
            login_user(usuario_logado)
            flash(f'Success! Your login is: {usuario_logado.usuario}', category='success')
            return redirect(url_for('page_produtos'))
        else:
            flash(f'Incorrect username or password! Try again!', category='danger')
    return render_template('login.html', form=form)


@app.route('/logout')
def page_logout():
    logout_user()
    flash('Account disconected with success!', category='info')
    return redirect(url_for('page_home'))
