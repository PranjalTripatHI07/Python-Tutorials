#DATE - 28/3/2025

# Here we manually test the class

from demo_class_for_testing import Survey

question = "what language did you first learn to speak? "
language_survey = Survey(question)

language_survey.show_questions()
print("Enter 'end' to exit the survey.")
while True:
    response = input("Language: ")
    if response == "end":
        break
    language_survey.store_response(response)


print("Survey result")
language_survey.show_response()