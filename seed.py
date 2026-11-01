from app import app
from database import db
from models import Autor, Livro, Leitor

    db.create_all()

    autor1 = Autor(nome="Machado de Assis", nacionalidade="Estados Unidos")
    autor2 = Autor(nome="Clarice Lispector", nacionalidade="Brasil")
    autor3 = Autor(nome="George Orwell", nacionalidade="Itália")

    db.session.add_all([autor1, autor2, autor3])
    db.session.commit()

    livro1 = Livro(titulo="Dom Casmurro", ano=1800, autor_id=autor1.id)
    livro2 = Livro(titulo="Memórias Póstumas de Brás Cubas", ano=1801, autor_id=autor1.id)
    livro3 = Livro(titulo="A Hora da Estrela", ano=1802, autor_id=autor2.id)

    db.session.commit()

    leitor1 = Leitor(nome="Mariana", email="mari@email.com")
    leitor2 = Leitor(nome="Rhodrigo", email=rho@email.com")
    leitor3 = Leitor(nome="Felipe", email="felipe@email.com")

    db.session.commit()