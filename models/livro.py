from database import db
from models.emprestimo import emprestimos


class Livro(db.Model):
    __tablename__ = "livros"

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(150), nullable=False)
    ano = db.Column(db.Integer)
    autor_id = db.Column(db.Integer, db.ForeignKey("autores.id"), nullable=False)
    autor = db.relationship("Autor", back_populates="livros")
    leitores = db.relationship("Leitor", secondary=emprestimos, back_populates="livros")
    def __repr__(self):
        return f"<Livro {self.titulo}>"
