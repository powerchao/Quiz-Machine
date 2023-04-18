from html import unescape

class Question():

    def __init__(self, qcategory, qtype, qdifficulty, qquestion, qcorans, qincans) -> None:
        self.category = qcategory
        self.type = qtype
        self.difficulty = qdifficulty
        self.question = unescape(qquestion)
        self.correct_answer = unescape(qcorans)
        self.incorrect_answers = qincans
        for n in range(len(self.incorrect_answers)):
            self.incorrect_answers[n] = unescape(self.incorrect_answers[n])

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
        answer_dictionary = {}
        answer_dictionary["A"] = (shuffled_list[0])
        answer_dictionary["B"] = (shuffled_list[1])
        answer_dictionary["C"] = (shuffled_list[2])
        answer_dictionary["D"] = (shuffled_list[3])
        return answer_dictionary


    

    