from flask import Flask

from database import db

from models import Autor, Livro, Leitor, emprestimos

from controllers.principal import principal
from controllers.autores import autores
from controllers.livros import livros
from controllers.leitores import leitores
from controllers.emprestimos import emprestimos as emprestimos_bp

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///biblioteca.db"
app.config["SECRET_KEY"] = "biblioteca"

db.init_app(app)
app.register_blueprint(autores)
app.register_blueprint(livros)
app.register_blueprint(leitores)
app.register_blueprint(emprestimos_bp)

if __name__ == "__main__":
    app.run(debug=True)
