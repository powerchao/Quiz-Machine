from requests import get
from os import system
from prettytable import PrettyTable

class Inputs():

    def list_categories(self, data):
        complete_columns = len(data)/6
        cat_table = PrettyTable()
        n = 0
        while n<complete_columns:
            r = n*6
            cat_table.add_column("ID #",[data[r]["id"],data[r+1]["id"],data[r+2]["id"],data[r+3]["id"],data[r+4]["id"],data[r+5]["id"]])
            cat_table.add_column("Category",[data[r]["name"],data[r+1]["name"],data[r+2]["name"],data[r+3]["name"],data[r+4]["name"],data[r+5]["name"]])
            n+=1
        print(cat_table)
        

    def __init__(self):
        system("cls")
        self.question_count = input("How many questions would you like on your quiz?\n")
        while not self.question_count.isdigit():
            print("Please enter a number with no symbols included.")
            self.question_count = input("How many questions would you like on your quiz?\n")
        self.question_count = "?amount="+self.question_count
        system("cls")
        category_data = get("https://opentdb.com/api_category.php").json()["trivia_categories"]
        self.list_categories(category_data)
        self.cat_id = input("Which category would you like? Please enter the corresponding ID #\nLeave blank for any category.\n")
        if self.cat_id == "":
            valid_ID = True
        else:
            valid_ID = False
            while not valid_ID:
                while not self.cat_id.isdigit():
                    print("Please enter the ID number to the left of your desired category.")
                    self.cat_id = input("Which category would you like? Please enter the corresponding ID #\n")
                for category in category_data:
                    if category["id"] == int(self.cat_id):
                        valid_ID = True
                if not valid_ID:
                    print("That category was not found.")
                    self.cat_id = input("Which category would you like? Please enter the corresponding ID #\n")
            self.cat_id = "&category="+self.cat_id

        





class DataBase():

    def __init__(self, inputs_object):
        self.question_website = "https://opentdb.com/api.php" + inputs_object.question_count + inputs_object.cat_id
        self.question_databank = get(self.question_website).json()["results"]
        


# {
#     "response_code": 0,
#     "results": [
#         {
#             "category": "Entertainment: Television",
#             "type": "multiple",
#             "difficulty": "hard",
#             "question": "The theme for the popular science fiction series &quot;Doctor Who&quot; was composed by who?",
#             "correct_answer": "Ron Grainer",
#             "incorrect_answers": ["Murray Gold", "Delia Derbyshire", "Peter Howell"]
#         },
#         {
#             "category": "General Knowledge", 
#             "type": "boolean", 
#             "difficulty": "medium", 
#             "question": "The bikini is named after the &quot;Bikini Atoll&quot;, an island where the United States conducted tests on atomic bombs.", 
#             "correct_answer": "True", 
#             "incorrect_answers": ["False"]
#         }, 
#         {"category": "Entertainment: Musicals & Theatres", "type": "multiple", "difficulty": "easy", "question": "Who wrote the award winning musical &quot;In The Heights&quot;?", "correct_answer": "Lin-Manuel Miranda", "incorrect_answers": ["Steven Sondheim", "Francis Scott Key", "John Phillips Sousa"]}, {"category": "Entertainment: Television", "type": "multiple", "difficulty": "medium", "question": "Dee from &quot;It&#039;s Always Sunny in Philadelphia&quot; has dated all of the following guys EXCEPT", "correct_answer": "Matthew &quot;Rickety Cricket&quot; Mara", "incorrect_answers": ["Colin the Thief", "Ben the Soldier", "Kevin Gallagher aka Lil&#039; Kevin"]}, {"category": "History", "type": "multiple", "difficulty": "easy", "question": "What was the first sport to have been played on the moon?", "correct_answer": "Golf", "incorrect_answers": ["Football", "Tennis", "Soccer"]}, {"category": "Animals", "type": "boolean", "difficulty": "easy",
#                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   "question": "A caterpillar has more muscles than humans do.", "correct_answer": "True", "incorrect_answers": ["False"]}, {"category": "Science: Mathematics", "type": "multiple", "difficulty": "easy", "question": "How many sides does a heptagon have?", "correct_answer": "7", "incorrect_answers": ["8", "6", "5"]}, {"category": "Vehicles", "type": "multiple", "difficulty": "hard", "question": "Which Audi does not use Haldex based all wheel drive system?", "correct_answer": "Audi A8", "incorrect_answers": ["Audi TT", "Audi S3", "Audi A3"]}, {"category": "Science: Computers", "type": "multiple", "difficulty": "hard", "question": "Dutch computer scientist Mark Overmars is known for creating which game development engine?", "correct_answer": "Game Maker", "incorrect_answers": ["Stencyl", "Construct", "Torque 2D"]}, {"category": "Entertainment: Video Games", "type": "multiple", "difficulty": "easy", "question": "In which mall does &quot;Dead Rising&quot; take place?", "correct_answer": "Willamette Parkview Mall", "incorrect_answers": ["Liberty Mall", "Twin Pines Mall", "Central Square Shopping Center"]}, {"category": "History", "type": "multiple", "difficulty": "medium", "question": "What year did the Vietnam War end?", "correct_answer": "1975", "incorrect_answers": ["1978", "1967", "1969"]}, {"category": "Entertainment: Film", "type": "boolean", "difficulty": "medium", "question": "The movie &quot;Tron&quot; received an Oscar nomination for Best Visual Effects.", "correct_answer": "False", "incorrect_answers": ["True"]}]}
