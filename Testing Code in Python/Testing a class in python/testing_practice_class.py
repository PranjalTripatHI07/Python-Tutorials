#DATE - 28/3/2025

# Here we are testing demo class using pytest

from testing_practice import demo_survey

def test_demo_survey():
    test1 = demo_survey("What is your name?")
    assert test1.show_questions() == "Questions => What is your name? "

def test_store_responses():
    test1 = demo_survey("What is your name?")
    test1.store_responses("Willie van")
    assert "Willie van" in test1.responses

