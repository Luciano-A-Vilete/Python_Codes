import pytest
from address import *

def test_extract_city():
    # Test case 1: City is in the middle of the address
    address1 = "123 Main St, Springfield, IL 12345"
    assert extract_city(address1) == "Springfield"

    # Test case 2: City is at the end of the address
    address2 = "456 Oak St, Boston, MA 67890"
    assert extract_city(address2) == "Boston"

    # Test case 3: City has multiple words
    address3 = "789 Elm St, New York City, NY 54321"
    assert extract_city(address3) == "New York City"

def test_extract_state():
    # Test case 1: State abbreviation is used
    address1 = "123 Main St, Springfield, IL 12345"
    assert extract_state(address1) == "IL"

    # Test case 2: Full state name is used
    address2 = "456 Oak St, Boston, Massachusetts 67890"
    assert extract_state(address2) == "Massachusetts"

    # Test case 3: State abbreviation and full name are mixed
    address3 = "789 Elm St, Austin, TX 54321"
    assert extract_state(address3) == "TX"

def test_extract_zipcode():
    # Test case 1: Five-digit ZIP code
    address1 = "123 Main St, Springfield, IL 12345"
    assert extract_zipcode(address1) == "12345"

    # Test case 2: Nine-digit ZIP code
    address2 = "456 Oak St, Boston, MA 67890-1234"
    assert extract_zipcode(address2) == "67890-1234"

    # Test case 3: ZIP code without hyphen
    address3 = "789 Elm St, New York City, NY 54321"
    assert extract_zipcode(address3) == "54321"
    
# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])