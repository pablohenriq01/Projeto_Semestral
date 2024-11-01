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
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:4701@localhost/db_adega'

#config - Joao
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:CASTELO2004@localhost/testedb'


#config banco de dados MySQL - pip install pymysql

# config - joao
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:castelo12@localhost/db_adega'
# Config - Dennis
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:4668@localhost/db_adega'

db =SQLAlchemy(app)

class Bebidas(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True )
    tipo_produto = db.Column(db.String(100), nullable = False)
    nome_produto = db.Column(db.String(200), nullable = False)
    marca_produto = db.Column(db.String(150), nullable = False)
    preco_produto = db.Column(db.Float, nullable = False)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/cadastrar")
def cadastrar():
    return render_template("cadastrar_edit.html")


@app.route("/catalogo")
def catalogo():
    lista_bebidas = Bebidas.query.order_by(Bebidas.id)

    return render_template("catalogo_users.html",
                           catalogo_bebidas = lista_bebidas)

@app.route("/catalogoadmin")
def catalogo_editar():
    lista_bebidas = Bebidas.query.order_by(Bebidas.id)

    return render_template("catalogo_edit.html",
                           catalogo_bebidas = lista_bebidas)

@app.route("/inserir", methods=['POST',])
def adicionar_bebidas():
    tipo = request.form['tipo_bebida']
    nome = request.form['nome_bebida']
    marca = request.form['marca']
    valor = float(request.form['valor'])

    nova_bebida = Bebidas(tipo_produto = tipo, nome_produto = nome, marca_produto = marca, preco_produto = valor)
    db.session.add(nova_bebida)
    db.session.commit()
    return redirect('/catalogo')

app.run()
