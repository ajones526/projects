import random

def get_questions():
    # Define a list of questions
    questions = [
        "What is the capital of France?",
        "How many continents are there?",
        "Who wrote 'Romeo and Juliet'?",
        "What is the largest planet in our solar system?",
        "What is the square root of 144?",
        # Add more questions as needed
    ]
    return questions

def play_game(questions):
    # Shuffle the questions randomly
    random.shuffle(questions)
    
    # Initialize the score
    score = 0
    
    print("Welcome to the Randomized 20 Questions Game!\n")
    
    # Iterate through the shuffled questions
    for i, question in enumerate(questions, start=1):
        print(f"Question {i}: {question}")
        user_answer = input("Your answer: ")
        
        # Check the answer (you can customize the correct answers)
        if is_correct_answer(question, user_answer):
            print("Correct!\n")
            score += 1
        else:
            print("Incorrect. The correct answer is:", get_correct_answer(question), "\n")
    
    print("Game Over! Your final score:", score)

def is_correct_answer(question, user_answer):
    # You can customize the logic for checking correct answers here
    # For simplicity, let's assume all answers are "correct"
    return True

def get_correct_answer(question):
    # You can customize the correct answers here
    # For simplicity, let's return a generic correct answer
    return "The correct answer is not specified for this question."

if __name__ == "__main__":
    questions_list = get_questions()
    play_game(questions_list)
