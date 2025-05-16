from car_details import car_tech_details

def test_car_tech_details():
    car_details = car_tech_details("Audi","AU01", "2024", "B47")
    assert car_details == car_tech_details("Audi","AU01", "2024", "B47")