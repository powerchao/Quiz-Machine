from question_model import Question
from quiz_brain import QuizBrain
from data import DataBase
from random import choice
from os import system
from html import unescape

def begin_game():
    question_set = DataBase()
    main_brain = QuizBrain(question_set.question_databank)
    main_brain.take_quiz()
    print("Goodbye.")

begin_game()


