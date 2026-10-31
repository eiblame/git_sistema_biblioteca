from database import db
from models.emprestimo import emprestimos
class Leitor(db.Model):
    __tablename__ = "leitores"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120))
    livros = db.relationship("Livro", secondary=emprestimos, back_populates="leitores")
    def __repr__(self):
        return f"<Leitor {self.nome}>"