from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Criar um APi Flask
app = Flask(__name__)

# Configurar SQLAlchemy
app.config['SECRET_KEY'] = 'FSD2323f#$!SAH'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
db = SQLAlchemy(app)

# Definir a estrutura da tabela Autor
class Autor(db.Model):
    __tablename__ = 'autor'
    id_autor = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    senha = db.Column(db.String(100), nullable=False)
    admin = db.Column(db.Boolean, default=False)
    postagens = db.relationship('Postagem', backref='autor', lazy=True)

# Definir a estrutura da tabela Postagem
class Postagem(db.Model):
    __tablename__ = 'postagem'
    id_postagem = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    conteudo = db.Column(db.Text, nullable=False)
    id_autor = db.Column(db.Integer, db.ForeignKey('autor.id_autor'), nullable=False)


def inicializar_banco():
    # Executar o comando para criar o banco de dados dentro do contexto da aplicação Flask
    with app.app_context():
        # Criar o banco de dados
        db.create_all()

        # Criar usuários administradores
        autor = Autor(nome='Jhonatan', email='jhonatan@email.com', senha='123456', admin=True)
        db.session.add(autor)
        db.session.commit()

if __name__ == '__main__':
    inicializar_banco()
