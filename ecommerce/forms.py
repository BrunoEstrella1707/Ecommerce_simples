from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from ecommerce.models import User


class CadastroForm(FlaskForm):
    def validate_usuario(self, check_user):
        user = User.query.filter_by(usuario=check_user.data).first()
        if user:
            raise ValidationError("Username alredy registered")

    def validate_email(self, check_email):
        email = User.query.filter_by(email=check_email.data).first()
        if email:
            raise ValidationError('Email alredy registered!')
        

    def validate_senha(self, check_senha):
        senha = User.query.filter_by(senha=check_senha.data).first()
        if senha:
            raise ValidationError('Password alredy registered!')



    usuario = StringField(label='Username: ', validators=[Length(min=4, max=30), DataRequired()])
    email = StringField(label='Email: ', validators=[Email(), DataRequired()])
    senha1 = PasswordField(label='Password: ',  validators=[Length(min=6, max=15), DataRequired()])
    senha2 = PasswordField(label='Confirm your Password: ',  validators=[EqualTo('senha1'), DataRequired()])
    submit = SubmitField(label='Register')
    


class LoginForm(FlaskForm):

    usuario = StringField(label='Username: ', validators=[DataRequired()])
    senha = PasswordField(label='Password: ',  validators=[DataRequired()])
    submit = SubmitField(label='Login')
