from base import Quiz, Question, Answer, Session, init_db

def print_menu():
    print("\nWelcome to the Quiz App!")
    print("1. Create a new quiz")
    print("2. Add a question to a quiz")
    print("3. Add an answer to a question")
    print("4. Take a quiz")
    print("5. Exit")

def create_quiz():
    title = input("Enter quiz title: ")
    session = Session()
    quiz = Quiz(title=title)
    session.add(quiz)
    session.commit()
    print(f"Quiz '{title}' created with id {quiz.id}.")

def add_question():
    quiz_id = input("Enter quiz id: ")
    text = input("Enter question text: ")
    session = Session()
    question = Question(text=text, quiz_id=int(quiz_id))
    session.add(question)
    session.commit()
    print(f"Question added to quiz {quiz_id} with id {question.id}.")

def add_answer():
    question_id = input("Enter question id: ")
    text = input("Enter answer text: ")
    correct = input("Is this answer correct? (y/n): ").strip().lower() == 'y'
    session = Session()
    answer = Answer(text=text, is_correct=correct, question_id=int(question_id))
    session.add(answer)
    session.commit()
    print(f"Answer added to question {question_id} with id {answer.id}.")

def take_quiz():
    quiz_id = input("Enter quiz id: ")
    session = Session()
    quiz = session.query(Quiz).get(int(quiz_id))
    if not quiz:
        print("Quiz not found.")
        return
    score = 0
    for q in quiz.questions:
        print(f"\nQ: {q.text}")
        answers = q.answers
        for idx, a in enumerate(answers):
            print(f"{idx+1}. {a.text}")
        try:
            choice = int(input("Your answer (number): "))
            if 0 < choice <= len(answers) and answers[choice-1].is_correct:
                score += 1
            else:
                print("Incorrect or invalid choice.")
        except Exception:
            print("Invalid input.")
    print(f"\nYour score: {score}/{len(quiz.questions)}")

def main():
    init_db()
    while True:
        print_menu()
        choice = input("Enter your choice: ").strip()
        if choice == '1':
            create_quiz()
        elif choice == '2':
            add_question()
        elif choice == '3':
            add_answer()
        elif choice == '4':
            take_quiz()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
