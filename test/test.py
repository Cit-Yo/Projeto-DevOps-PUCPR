from src.main import genderSelect
from unittest.mock import patch

def test_genderSelect():
    
    gender_test = "Male"
    assert gender_test == genderSelect("M")
    gender_test = "Female"
    assert gender_test == genderSelect("F")

test_genderSelect()