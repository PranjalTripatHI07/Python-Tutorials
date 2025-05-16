#DATE- 26/3/2025

#Testing location details function

from Exercise_1 import location_details

def test_location_details():
    info = location_details("santiago", "chile")
    assert info == "City name => santiago | Country name => chile"
    