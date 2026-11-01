from flask import Blueprint, flash, redirect, render_template, request, url_for

from database import db
from models.autor import Autor
from models.livro import Livro

livros = Blueprint("livros", __name__, url_prefix="/livros")

@livros.route("/")
def listar():
    return render_template("livros.html", livros=Livro.query.all())

@livros.route("/novo", methods=["GET", "POST"])
def novo():
    if request.method == "POST":
        livro = Livro(
            titulo=request.form["titulo"],
            ano=request.form.get("ano", type=int),
            autor_id=request.form.get("autor_id", type=int),
        )
        db.session.add(livro)
        db.session.commit()
        flash("Livro cadastrado.")
        return redirect(url_for("livros.listar"))

    return render_template("livro_form.html", livro=None, autores=Autor.query.all())

@livros.route("/<int:id>")
def detalhar(id):
    livro = db.get_or_404(Livro, id)
    return render_template("livro_detalhe.html", livro=livro)

@livros.route("/<int:id>/editar", methods=["GET", "POST"])
def editar(id):
    livro = db.get_or_404(Livro, id)

    if request.method == "POST":
        livro.titulo = request.form["titulo"]
        livro.ano = request.form.get("ano", type=int)
        livro.autor_id = request.form.get("autor_id", type=int)
        db.session.commit()
        flash("Livro atualizado.")
        return redirect(url_for("livros.listar"))

    return render_template("livro_form.html", livro=livro, autores=Autor.query.all())

@livros.route("/<int:id>/excluir", methods=["POST"])
def excluir(id):
    livro = db.get_or_404(Livro, id)
    livro.leitores.clear()
    db.session.delete(livro)
    db.session.commit()
    flash("Livro excluído.")
    return redirect(url_for("livros.listar"))
