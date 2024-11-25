# Tu March 2 and We March 3, 2022
# Day 17. Quiz game

# This file was made in PyCharm.
# question_model.py, data.py and quiz_brain.py is written below main.py


# main.py

from question_model import Question
from data import question_data # import the list question_data
from quiz_brain import QuizBrain


# Create question_bank: it should contain a list of question objects each containing a question and an answer:
# Data comes from the data - so how to loop through the question data?

# ToDo 1. Write a for loop to iterate over the question_data

question_bank = [] # Created empty list to put questions in
for question in question_data:
    q_text = question["question"]
    q_answer = question["correct_answer"]
    new_question = Question(q_text, q_answer)
    question_bank.append(new_question)

quiz_brain = QuizBrain(question_bank)
while quiz_brain.still_has_questions():
    quiz_brain.next_question()

print("\nYou\'ve completed the quiz. ")
print(f"You\'re final score was: {quiz_brain.current_score}/{quiz_brain.question_number}! ")


# question_model.py

class Question:

    def __init__(self, text, answer):
        self.text = text
        self.answer = answer
 
 
# data.py

question_data = [
    {"category": "Science: Computers",
     "type": "boolean",
     "difficulty": "easy",
     "question": "Linus Torvalds created Linux and Git.",
     "correct_answer": "True",
     "incorrect_answers": ["False"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
     "question": "The programming language &quot;Python&quot; is based off a modified version of &quot;JavaScript&quot;.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
     "question": "The logo for Snapchat is a Bell.", "correct_answer": "False",
     "incorrect_answers": ["True"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
     "question": "RAM stands for Random Access Memory.", "correct_answer": "True",
     "incorrect_answers": ["False"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
     "question": "&quot;HTML&quot; stands for Hypertext Markup Language.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
     "question": "Time on Computers is measured via the EPOX System.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
     "question": "The Windows 7 operating system has six main editions.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
     "question": "The Windows ME operating system was released in the year 2000.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
     "question": "Linux was first created as an alternative to Windows XP.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
     "question": "The Python programming language gets its name from the British comedy group &quot;Monty Python.&quot;",
     "correct_answer": "True", "incorrect_answers": ["False"]}]
  
 
# quiz_brain.py

class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0  # All are quizzes start at first question. Keeps track on which quistion you are on
        self.question_list = question_list
        self.current_score = 0

    def next_question(self):
        """1. Retrieves the item at the current question_number from the question_list. """
        """2. Pull up the question from the question_list, depending on which question we are on"""
        new_question = self.question_list[self.question_number]
        self.question_number += 1  # Increase question_number by one here, so that on next line it already shows +1
        user_answer = input(f"\nQ.{self.question_number}: {new_question.text}. (True/False)?: ").lower()
        self.check_answer(user_answer, new_question.answer)


    def still_has_questions(self):
        """Returns True when there are still questions left, False when there are no more questions left. """
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, new_question):
        """Function that checks if answer_question is the same as the correct_answer"""
        if user_answer == new_question.lower():
            self.current_score += 1
            print("You got it right!")
            print(f"The correct answer was: {new_question}. ")
            print(f"You\'re currecnt score is: {self.current_score}/{self.question_number}" )

        elif user_answer != new_question.lower():
            print("That\'s wrong.")
            print(f"The correct answer was: {new_question}. ")
            print(f"You\'re current score is: {self.current_score}/{self.question_number}")