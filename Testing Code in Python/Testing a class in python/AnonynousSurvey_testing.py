#DATE - 28/3/2025

#Here we create a demo class of anonymous survey

class Anonynous_Survey:
    def __init__(self, question):
        self.question = question
        self.answers = []

    def show_question(self):
        return f"Question => {self.question}"

    def store_answer(self, new_answers):
        self.answers.append(new_answers)

    def show_answer(self):
        print("These are the answers:")
        for answer in self.answers:
            return f"Answer => {answer}"