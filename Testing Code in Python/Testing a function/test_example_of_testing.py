from example_of_testing import inventory_management

def test_inventory_management():
    inventory_info = inventory_management("willie van", 4)
    assert inventory_info == "\n Supplier Name: Willie Van, Inventory Number: 4"

