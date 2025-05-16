#DATE - 22/3/2025

# Here we are testing get_formatted_name() function using pytest

from get_formatted_name import get_formatted_name

def test_get_formatted_name():
    """Generating a full name."""
    formatted_name = get_formatted_name("willie", "van")
    assert formatted_name == "\n Willie Van"

# here we use assert, assert => In pytest, the assert statement is used to validate that a condition is true
# If the condition is false, the test fails, indicating that something unexpected or incorrect has occurred
# Note => Any function name that starts with "test_" will be discovered by pytest and will run as a part of the testing process
# Note => We will never call the function yourself Pytest will find the function and run it for us


#Note assert => assert is assertion and assertion is basically a claim about a condition
# like in the above code we assert,or we claim that the value of formatted_name  should be "Willie Van"
#syntax => assert variable_name == "value"  Note-> if variable_name output is equal to value then test is passed if note then it fails

#Note we can run pytest directly in terminal by using this syntax command => python -m pytest



#Topic - Failing Test

#Pytest shares alot of information when the test fails

#First it show the status of the test fail/passed
#if the test fails => then wee see the name of a function which failed
# >(this angle bracket) indicates the line of code that cause the test fail

# E(this E word) shows us the actual error that caused the failure

#And at the end we see short test summery => which give us quick sense of which test failed and why