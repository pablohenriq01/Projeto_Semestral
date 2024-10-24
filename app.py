from flask import Flask
from flask_sqlalchemy import SQLAlchemy


class Bebidas:
    def __init__(self, tipo_bebidas, nome_bebidas, marca_bebidas, preco_bebidas):
        self.tipo = tipo_bebidas
        self.nome = nome_bebidas
        self.marca = marca_bebidas
        self.preco = preco_bebidas



app = Flask(__name__)

#config banco de dados PostgreSQL - Pablo
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:4701@localhost/db_adega'

#config banco de dados MySQL - pip install pymysql
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://usuario:senha@localhost/db_adega'

db =SQLAlchemy(app)



class Bebidas(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True )
    tipo_produto = db.Column(db.String(100), nullable = False)
    nome_produto = db.Column(db.String(200), nullable = False)
    marca_produto = db.Column(db.String(150), nullable = False)
    preco_produto = db.Column(db.Float, nullable = False)
    
