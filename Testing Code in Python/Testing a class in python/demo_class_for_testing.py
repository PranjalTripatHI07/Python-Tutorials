#DATE - 26/3/2025

# Here is a demo class for testing

class Survey:
    def __init__(self, questions):
        self.questions = questions  
        self.responses = []

    def show_questions(self):
        return f"Questions => {self.questions} "

    def store_response(self, new_response):
        self.responses.append(new_response)

    def show_results(self):
        print("Survey Results:")
        for response in self.responses:
            return f" - {response}"


