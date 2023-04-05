from html import unescape

class Question():

    def __init__(self, qcategory, qtype, qdifficulty, qquestion, qcorans, qincans) -> None:
        self.category = qcategory
        self.type = qtype
        self.difficulty = qdifficulty
        self.question = unescape(qquestion)
        self.correct_answer = unescape(qcorans)
        self.incorrect_answers = unescape(qincans)

    def is_boolean(self):
        if self.type == 'boolean':
            return True
        else:
            return False
    
    def is_answer(self, ans_string):
        """String to boolean. Compares argument with object's correct
        answer attribute."""
        if ans_string.lower() == self.correct_answer.lower():
            return True
        else:
            return False
        
    def present_answers(self, shuffled_list):
        presentable_string = "Your options are: "
        presentable_string += shuffled_list[0] + ", "
        presentable_string += shuffled_list[1] + ", "
        presentable_string += shuffled_list[2] + ", or "
        presentable_string += shuffled_list[3] + "."
        return presentable_string


    

    