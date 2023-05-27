from ecommerce import app
from flask import render_template
from ecommerce.models import Item 
from ecommerce.forms import CadastroForm


@app.route('/')
def page_home():
    return render_template("home.html")


@app.route('/produtos')
def page_produtos():

    itens = Item.query.all()
    return render_template("produtos.html", itens=itens)


@app.route('/cadastro')
def page_cadastro():
    form = CadastroForm()
    return render_template("cadastro.html", form=form)