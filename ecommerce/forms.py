from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField


class CadastroForm(FlaskForm):
    usuario = StringField(label='Username: ')
    email = StringField(label='Email: ')
    senha1 = PasswordField(label='Senha: ')
    senha2 = PasswordField(label='Confirme a senha: ')
    submit = SubmitField(label='Cadastrar')