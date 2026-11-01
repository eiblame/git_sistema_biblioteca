from flask import Blueprint, render_template

from database import db
from models.autor import Autor
from models.livro import Livro
from models.leitor import Leitor
from models.emprestimo import emprestimos

principal = Blueprint("principal", __name__)
