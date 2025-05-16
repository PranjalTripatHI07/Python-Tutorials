#DATE -26/3/2025

#Topic - Testing a class in Python

#=> We can test class in python using pytest

#A verity of assertions
"""
Assertion                    claim
1. assert a == b      =>   Assert/claim two values are equal

2. assert a != b      =>   Assert/claim two values are not equal

3. assert  a           =>   assert a evaluates to True

4. assert element in list   => assert element is in list

5. assert element not in list   => assert element is not in list

"""

# Note => Testing a class is same as testing a function

# For testing a class first we create a demo class which perform certain tasks

# After that we create  a testing file and here we test the class

# So to test the demo class
#1. First we create a test function and inside that test function we create an object and pass the value in class
# like below syntax
#synatx => object_name = class_name("value")

#2. After that we call that object with the function of which we are going to test
#like below syntax
#synatx => object_name.function_name("value")

#3. after that we make assertion of the function we are going to test
#like below syntax
#synatx => assert object_name.function_name() or if we are dealing with list then => assert "value" in object_name.attribute_name



#Topic => Using fixtures

#Note => fixtures help us to set up a test environment means creating a resource that is used by more than one test

#syntax => @pytest.fixture

#Note => Decorators =>  Decorator is a function that modifies another function or method by adding or
# extending its behavior without changing its source code.

