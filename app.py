from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

#config banco de dados PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:4701@localhost/db_adega'

#config banco de dados MySQL - pip install pymysql
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://usuario:senha@localhost/db_adega'