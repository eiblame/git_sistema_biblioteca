from flask import Blueprint, flash, redirect, render_template, request, url_for

from database import db
from models.leitor import Leitor

leitores = Blueprint("leitores", __name__, url_prefix="/leitores")

@leitores.route("/")
def listar():
    return render_template("leitores.html", leitores=Leitor.query.all())

@leitores.route("/novo", methods=["GET", "POST"])
def novo():
    if request.method == "POST":
        leitor = Leitor(
            nome=request.form["nome"],
            email=request.form.get("email", ""),
        )
        db.session.add(leitor)
        db.session.commit()
        return redirect(url_for("leitores.listar"))

    return render_template("leitor_form.html", leitor=None)

@leitores.route("/<int:id>")
def detalhar(id):
    leitor = db.get_or_404(Leitor, id)
    return render_template("leitor_detalhe.html", leitor=leitor)

@leitores.route("/<int:id>/editar", methods=["GET", "POST"])
def editar(id):
    leitor = db.get_or_404(Leitor, id)

    if request.method == "POST":
        leitor.nome = request.form["nome"]
        leitor.email = request.form.get("email", "")
        db.session.commit()
        return redirect(url_for("leitores.listar"))

    return render_template("leitor_form.html", leitor=leitor)
