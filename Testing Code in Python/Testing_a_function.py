#DATE - 22/3/2025

# Topic -> Testing a Function

#For testing a function we first create a demo function which perform some task

def get_formatted_name(first_name, last_name):
    """Generating a full name."""
    full_name = f"\n {first_name} {last_name}"
    return full_name.title()




#Now here we are using pytest for testing above function
#Before testing we have to learn few concepts about testing

#1. Unit Test => A unit test verifies that a specific aspect of a function behaviour is correct

#2. Test Cases => A test cases is a collection of unit tests that together prove that a function behaves as it supposed to


# Passing test => With Pytest the test function call the function we are testing and will make an assertion(claim) about the value
# that is returned
# if our assertion is correct the test will pass,  if our assertion is incorrect the test will fail


