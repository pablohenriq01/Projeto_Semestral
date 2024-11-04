from flask import Flask, render_template, request, redirect, jsonify
#pip install Flask-SQLAlchemy
from flask_sqlalchemy import SQLAlchemy


class Bebidas:
    def __init__(self, tipo_bebidas, nome_bebidas, marca_bebidas, preco_bebidas):
        self.tipo = tipo_bebidas
        self.nome = nome_bebidas
        self.marca = marca_bebidas
        self.preco = preco_bebidas

class Login:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.marca = senha



app = Flask(__name__)

#config banco de dados PostgreSQL - Pablo
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:4701@localhost/db_adega'

#config - Joao
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:CASTELO2004@localhost/testedb'


#config banco de dados MySQL - pip install pymysql

# config - joao
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:castelo12@localhost/db_adega'
# Config - Dennis
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:4668@localhost/db_adega'

db =SQLAlchemy(app)

class Bebidas(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True )
    tipo_produto = db.Column(db.String(100), nullable = False)
    nome_produto = db.Column(db.String(200), nullable = False)
    marca_produto = db.Column(db.String(150), nullable = False)
    preco_produto = db.Column(db.Float, nullable = False)

class Login(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True )
    nome = db.Column(db.String(250), nullable = False)
    email = db.Column(db.String(150), nullable = False)
    senha = db.Column(db.String(30), nullable = False)


#Rotas de telas
@app.route("/")
def tela_acesso():
    return render_template("tela_cadastro_login.html")

@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/cadastrar")
def cadastrar():
    return render_template("cadastrar_edit.html")


@app.route("/catalogo")
def catalogo():
    lista_bebidas = Bebidas.query.all()

    return render_template("catalogo_users.html",
                           catalogo_bebidas = lista_bebidas)



#Rotas para acesso com o banco de dados
@app.route("/cadastro", methods=['POST',])
def acesso_cadastro():
    nome = request.form['nome']
    email = request.form['email']
    senha = request.form['senha']
    confirmSenha = request.form['confirmar_senha']
    
    if senha == confirmSenha :
        novo_usuario = Login(nome = nome, email = email, senha = senha)
        db.session.add(novo_usuario)
        db.session.commit()

        return redirect("/catalogo")
    else:
        return redirect("/")
    

@app.route("/login" ,methods=['POST',])
def acesso_login():
    email = request.form.get('email')
    senha = request.form.get('senha')

    verifica_email = Login.query.filter_by(email = email).first()
    verifica_senha = Login.query.filter_by(senha = senha).first()

    if verifica_email and verifica_senha:
        return redirect('/catalogo')
    else:
        return redirect("/")
@app.route("/edicao/<int:id>", methods=['POST',])
def editar(id):
    bebidas = Bebidas.query.filter_by(id = id).first()

    return render_template("editar.html", lista_bebidas = bebidas)

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

@app.route("/editar/<int:id>", methods=['POST',])
def editar_bebidas(id):
   
    bebidas = Bebidas.query.filter_by(id = id).first()
    bebidas.tipo_produto = request.form['tipo_bebida']
    bebidas.nome_produto = request.form['nome_bebida']
    bebidas.marca_produto = request.form['marca']
    bebidas.preco_produto = float(request.form['valor'])
    db.session.commit()
    
    return redirect('/catalogo')

@app.route("/excluir/<int:id>", methods=['POST',])
def excluir_bebidaID(id):
    bebida = Bebidas.query.filter_by(id = id).first()
    db.session.delete(bebida)
    db.session.commit() 
    return redirect('/catalogo')

app.run()
