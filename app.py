from flask import Flask, render_template, request, redirect
#pip install Flask-SQLAlchemy
from flask_sqlalchemy import SQLAlchemy


class Bebidas:
    def __init__(self, tipo_bebidas, nome_bebidas, marca_bebidas, preco_bebidas):
        self.tipo = tipo_bebidas
        self.nome = nome_bebidas
        self.marca = marca_bebidas
        self.preco = preco_bebidas


app = Flask(__name__)

#config banco de dados PostgreSQL - Pablo
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:4701@localhost/db_adega'

#config - Joao
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:CASTELO2004@localhost/testedb'


#config banco de dados MySQL - pip install pymysql

# config - joao
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:castelo12@localhost/db_adega'

#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://usuario:senha@localhost/db_adega'

db =SQLAlchemy(app)

class Bebidas(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True )
    tipo_produto = db.Column(db.String(100), nullable = False)
    nome_produto = db.Column(db.String(200), nullable = False)
    marca_produto = db.Column(db.String(150), nullable = False)
    preco_produto = db.Column(db.Float, nullable = False)

@app.route("/cadastrar")
def cadastrar():
    return render_template("cadastrar.html")

 
    
@app.route("/")
def main():
    return "Rota principal do projeto"

@app.route("/catalogo")
def catalogo():
    lista_bebidas = Bebidas.query.order_by(Bebidas.id)

    return render_template("catalogo.html",
                           lista_bebidas = lista_bebidas)

app.run()
