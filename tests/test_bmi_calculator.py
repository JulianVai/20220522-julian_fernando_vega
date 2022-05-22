import pytest
import json
from bmi_calc.bmi_calculator import calculate_bmi, categorize_bmi 

test_data = [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 },
    { "Gender": "Male", "HeightCm": 161, "WeightKg": 85 },
    { "Gender": "Male", "HeightCm": 180, "WeightKg": 77 },
    { "Gender": "Female", "HeightCm": 166, "WeightKg": 62},
    {"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
    {"Gender": "Female", "HeightCm": 167, "WeightKg": 82}]

def test_calculate_bmi() -> None:    
    bmi_list = list(map(calculate_bmi, test_data))
    assert [32.8, 32.8, 23.8, 22.5, 31.1, 29.4] == bmi_list

def test_categorize_bmi() -> None:
    assert "Underweight" == categorize_bmi(18.2)
    assert "Normal weight" == categorize_bmi(22.1)
    assert "Overweight" == categorize_bmi(27.3)
    assert "Moderately obese" == categorize_bmi(32.3)
    assert "Severely obese" == categorize_bmi(38.5)
    assert "Very severely obese" == categorize_bmi(42.3)