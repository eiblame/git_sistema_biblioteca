from flask import Blueprint, flash, redirect, render_template, request, url_for

from database import db
from models.leitor import Leitor
from models.livro import Livro


emprestimos = Blueprint("emprestimos", __name__, url_prefix="/emprestimos")

@emprestimos.route("/")
def listar():
    registros = []
    for leitor in Leitor.query.all():
        for livro in leitor.livros:
            registros.append((leitor, livro))
    return render_template("emprestimos.html", registros=registros)

@emprestimos.route("/novo", methods=["GET", "POST"])
def novo():
    if request.method == "POST":
        leitor = db.session.get(Leitor, request.form.get("leitor_id", type=int))
        livro = db.session.get(Livro, request.form.get("livro_id", type=int))

        if leitor and livro and livro not in leitor.livros:
            leitor.livros.append(livro)
            db.session.commit()

    return render_template(
        "emprestimo_form.html",
        leitores=Leitor.query.all(),
        livros=Livro.query.all(),
    )

@emprestimos.route("/excluir/<int:leitor_id>/<int:livro_id>", methods=["POST"])
def excluir(leitor_id, livro_id):
    leitor = db.get_or_404(Leitor, leitor_id)
    livro = db.get_or_404(Livro, livro_id)

    if livro in leitor.livros:
        leitor.livros.remove(livro)
        db.session.commit()
        flash("Empréstimo removido.")
    return redirect(url_for("emprestimos.listar"))
