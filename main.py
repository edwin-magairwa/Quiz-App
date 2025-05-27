from app.cli import menu
from app.db.session import engine
from app.models.base import Base
from app.models import user, quiz, question, answer

Base.metadata.create_all(engine)

if __name__ == "__main__":
    menu()
