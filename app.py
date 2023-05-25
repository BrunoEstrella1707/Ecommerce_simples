from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def page_home():
    return render_template("home.html")

@app.route('/produtos')
def page_produtos():

    itens = [
        {'id': 1, 'nome': 'Celular', 'cod': '23423424', 'preco': 1200},
        {'id': 2, 'nome': 'Notebook', 'cod': '12345678', 'preco': 3500},
        {'id': 3, 'nome': 'Teclado', 'cod': '54239918', 'preco': 120},
        {'id': 4, 'nome': 'Monitor', 'cod': '61129763', 'preco': 800}
    ]

    return render_template("produtos.html", itens=itens)

