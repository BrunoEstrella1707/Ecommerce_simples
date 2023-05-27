from ecommerce import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(length=30), nullable=False, unique=True)
    email = db.Column(db.String(length=50), nullable=False, unique=True)
    senha = db.Column(db.String(length=15), nullable=False, unique=True)
    credito = db.Column(db.Integer, nullable=False, default=50000)
    itens = db.relationship('Item', backref='dono_user', lazy=True)


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(length=30), nullable=False, unique=True)
    cod = db.Column(db.String(length=8), nullable=False, unique=True)
    preco = db.Column(db.Integer, nullable=False)
    desc = db.Column(db.String(length=1024), nullable=False, unique=True)
    dono = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'{self.nome}'
    
