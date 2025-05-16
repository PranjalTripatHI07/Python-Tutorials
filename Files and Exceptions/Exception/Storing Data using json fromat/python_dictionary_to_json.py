import json

my_dictionary = {"name":"Willie van", "age":45, "country":"USA", "City":"New York"}
json_format = json.dumps(my_dictionary)
print(json_format)