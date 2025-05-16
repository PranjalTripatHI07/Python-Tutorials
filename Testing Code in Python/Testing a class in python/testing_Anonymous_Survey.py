#DATE - 28/3/2025

#Here we are testing the Anonymous Survey class

from AnonynousSurvey_testing import Anonynous_Survey


def test_Anonymous_Survey():

    question = "What is your favorite color?"
    survey_test1 = Anonynous_Survey(question)
    survey_test1.show_question()
    assert survey_test1.show_question() == "Question => What is your favorite color?"

def test_Anonymous_Survey_store_answer_function():
    question = "What is your favorite language?"
    survey_test1 = Anonynous_Survey(question)
    answers = ["English","Spanish", "German", "French"]
    for answer in answers:
        survey_test1.store_answer(answer)

    for answer in answers:
        assert answer in survey_test1.answers
