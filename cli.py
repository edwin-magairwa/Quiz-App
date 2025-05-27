import click
from base import Quiz, Question, Answer, Session

@click.group()
def cli():
    pass

@cli.command()
@click.argument('title')
def create_quiz(title):
    """Create a new quiz."""
    session = Session()
    quiz = Quiz(title=title)
    session.add(quiz)
    session.commit()
    click.echo(f"Quiz '{title}' created with id {quiz.id}.")

@cli.command()
@click.argument('quiz_id', type=int)
@click.argument('text')
def add_question(quiz_id, text):
    """Add a question to a quiz."""
    session = Session()
    question = Question(text=text, quiz_id=quiz_id)
    session.add(question)
    session.commit()
    click.echo(f"Question added to quiz {quiz_id} with id {question.id}.")

@cli.command()
@click.argument('question_id', type=int)
@click.argument('text')
@click.option('--correct', is_flag=True, help='Mark this answer as correct.')
def add_answer(question_id, text, correct):
    """Add an answer to a question."""
    session = Session()
    answer = Answer(text=text, is_correct=correct, question_id=question_id)
    session.add(answer)
    session.commit()
    click.echo(f"Answer added to question {question_id} with id {answer.id}.")

@cli.command()
@click.argument('quiz_id', type=int)
def take_quiz(quiz_id):
    """Take a quiz."""
    session = Session()
    quiz = session.query(Quiz).get(quiz_id)
    if not quiz:
        click.echo("Quiz not found.")
        return
    score = 0
    for q in quiz.questions:
        click.echo(f"Q: {q.text}")
        answers = q.answers
        for idx, a in enumerate(answers):
            click.echo(f"{idx+1}. {a.text}")
        choice = click.prompt("Your answer", type=int)
        if 0 < choice <= len(answers) and answers[choice-1].is_correct:
            score += 1
        else:
            click.echo("Incorrect or invalid choice.")
    click.echo(f"Your score: {score}/{len(quiz.questions)}")

if __name__ == "__main__":
    cli()
