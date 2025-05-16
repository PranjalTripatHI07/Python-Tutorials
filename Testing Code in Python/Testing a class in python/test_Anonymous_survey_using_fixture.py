import pytest
from AnonynousSurvey_testing import Anonynous_Survey

@pytest.fixture
def language_survey():
    """A survey that will be available for all test functions"""
    question = "What is your favorite language?"
    language = Anonynous_Survey(question)
    return language

def test_Anonymous_Survey_store_answer_function(language_survey):
    language_survey.store_answer("English")
    assert "English" in language_survey.answers

def test_Anonymous_Survey_store_answer_function2(language_survey):
    answers = ["English", "Spanish", "French"]
    for answer in answers:
        language_survey.store_answer(answer)
    for answer in answers:
        assert answer in language_survey.answers