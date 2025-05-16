#DATE- 26/2/2025

from Exercise_2 import population_details

def test_population_details():
    info = population_details("New York", "United States", "1Billion")
    assert info == "County => United States | City => New York | Population => 1Billion"