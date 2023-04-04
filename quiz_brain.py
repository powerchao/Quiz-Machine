from question_model import Question
from random import choice, shuffle

class QuizBrain():

    def __init__(self, databank):
        self.question_list = []
        for question in databank:
            self.question_list.append(
                Question(
                    qcategory=question["category"], 
                    qtype=question["type"],
                    qdifficulty=question["difficulty"],
                    qquestion=question["question"],
                    qcorans=question["correct_answer"],
                    qincans=question["incorrect_answers"],
                )
            )
        self.player_wrong = 0
        self.player_right = 0
    
    def ask_question(self, current_question):
        print(current_question.question)
        if current_question.is_boolean():
            player_response = input("\nTrue or False?\n").lower()
            if current_question.is_answer(player_response):
                return True
            else:
                return False
        else:
            possible_answers = []
            possible_answers.append(current_question.correct_answer)
            for answer in current_question.incorrect_answers:
                possible_answers.append(answer)
            shuffle(possible_answers)
            print(current_question.present_answers(shuffled_list=possible_answers))
            player_response = input("What is your answer?\n")
            if current_question.is_answer(player_response):
                return True
            else:
                return False
            
    def take_quiz(self):
        print("Welcome to the Quiz Game!")
        for question in self.question_list:
            if self.ask_question(question):
                self.player_right += 1
                print("Correct!\n")
            else:
                self.player_wrong += 1
                print("Incorrect. The correct answer was " + question.correct_answer + ".\n")
        accuracy = str(int(round(self.player_right/(self.player_right+self.player_wrong)*100,0)))
        total_qs = str(len(self.question_list))
        print(f"Your score is {accuracy}% out of {total_qs} questions.")
            


    

    
