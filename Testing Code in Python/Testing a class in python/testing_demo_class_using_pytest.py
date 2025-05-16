#DATE -  28/3/2025
# Here we are testing class using pytest

from demo_class_for_testing import Survey

def test_survey_class():
    questions = "What is your first language that you speak?"
    test1 = Survey(questions) #here we creat a object and pass attribute value
    test1.show_questions() # here we simply call the function of which we are going to test through object
    assert test1.show_questions() == "Questions => What is your first language that you speak? "  #here we make assertion / claim and pass that object with the function we are going to test and the value/output
# syntax => assert object_name.function_name() == "value"
def test_store_response():
   test1 = Survey("What is your first language that you speak?")  #here we creat a object and pass attribute value
   test1.store_response("English") # here we simply call the function of which we are going to test through object
   assert "English" in test1.responses  #here we make assertion / claim and pass that object with the function we are going to test and the value/output




