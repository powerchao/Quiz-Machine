from question_model import Question
from quiz_brain import QuizBrain
from data import DataBase,Inputs
from random import choice
from os import system
from html import unescape

def begin_game():
    continuing = True
    while continuing:
        player_input = Inputs()
        question_set = DataBase(player_input)
        main_brain = QuizBrain(question_set.question_databank)
        system("cls")
        main_brain.take_quiz()
        another_quiz = input("Would you like to take another quiz? Y or N\n").lower()
        if another_quiz != "y":
            continuing = False
        

begin_game()


