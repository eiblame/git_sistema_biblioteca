from database import db
emprestimos = db.Table(
    "emprestimos",
    db.Column("leitor_id", db.Integer, db.ForeignKey("leitores.id"), primary_key=True),
    db.Column("livro_id", db.Integer, db.ForeignKey("livros.id"), primary_key=True),
)
