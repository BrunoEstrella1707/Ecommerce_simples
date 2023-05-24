from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("home.html")


@app.route('/sobre<usuario>')
def sobre(usuario):
    return f"<h3>Sobre mim: {usuario}</h3>"