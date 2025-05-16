#DATE - 28/3/2025

# here we are practicing class testing and for that we are creating demo class

class demo_survey:
    def __init__(self, questions):
        self.questions = questions
        self.responses = []
    def show_questions(self):
        return f"Questions => {self.questions} "

    def store_responses(self, new_responses):
        self.responses.append(new_responses)
        return self.responses

    def show_demo_survey(self):
        print("showing demo survey")
        for response in self.responses:
            return f"response => {response}"


