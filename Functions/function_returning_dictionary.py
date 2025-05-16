#DATE - 3/2/2025

#Topic => Returning a Dictionary

#=> Function can return any kind of value including more complex data structure like Lists and Dictionary

#Example

def generate_name(first_name, last_name):
    name={"first":first_name, "last":last_name}
    return  name


generate = generate_name(first_name="willie", last_name="man")
print(generate)

#or

def generate_name(first_name, last_name, middle_name=""):
    if middle_name:
        name = {"firstname":first_name, "middlename":middle_name, "lastname":last_name, }
    else:
        name = {"firstname":first_name, "lastname":last_name}
    return name


generate = generate_name(first_name="wille", last_name="van", middle_name="bruce")
print(generate)

# another example

def generate_user_info(first_name, last_name, age = None):
    user_info = {"firstname":first_name, "lastname":last_name, "Age":age}
    return user_info


generate = generate_user_info(first_name="willie", last_name="van")
print(generate)
generate = generate_user_info(first_name="willie", last_name="van", age=40)
print(generate)


#Or

def generate_user_info(first_name, last_name, age = None):
    user = {"firstname":first_name, "lastname":last_name}
    if age:
        user['Age']= age
    return user

generate = generate_user_info(first_name="willie", last_name="van")
print(generate)
generate = generate_user_info(first_name="willie", last_name="van", age=40)
print(generate)

