from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

class Quiz(Base):
    __tablename__ = 'quizzes'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    questions = relationship("Question", back_populates="quiz")
