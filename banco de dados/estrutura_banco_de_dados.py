from flask import Flask
from  flask_sqlalchemy import SQLAlchemy

#Criar um APi flask
app = Flask(__name__)
#criar um isntancia de sqlalchemy
app.config['SECRET_KEY'] = 'FSD2323f#$!SAH'
app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///blog.db'
db = SQLAlchemy(app)
db:SQLAlchemy
#Definir a estrtura da tabela Postagem


#Definir a estrutura da tabela Autor
