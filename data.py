from requests import get


class DataBase():

    def __init__(self):
        self.length = input("How many questions would you like? ")
        self.question_website = "https://opentdb.com/api.php?amount=" + self.length
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
