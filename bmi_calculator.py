import os
import json

def calculate_bmi(d_point) -> int:
    """given a d_point
    calculate the bmi"""
    mass = d_point["WeightKg"]
    height = d_point["HeightCm"]/100
    return round(mass / (height*height), 1)

def categorize_bmi(bmi) -> str:
    """match the bmi
    with a given category"""
    match bmi:
        case bmi if bmi <= 18.4:
            return  "Underweight"
        case bmi if (18.5 <= bmi <= 24.9):
            return "Normal weight"
        case bmi if (25 <= bmi <= 29.9):
            return "Overweight"
        case bmi if (30 <= bmi <= 34.9):
            return "Moderately obese"
        case bmi if (35 <= bmi <= 39.9):
            return "Severely obese"
        case bmi if bmi >= 40:
            return "Very severely obese"


if __name__ == "__main__":
    print("input data should be named: data.json")

    with open("data.json") as data_json:
        data = json.load(data_json)

    ### Create BMI list from data.
    bmi_list = list(map(calculate_bmi, data))

    ### Count how many are overweight.
    overweigth_count = len(list(filter(lambda x: (x=="Overweight"), list(map(categorize_bmi, bmi_list)))))

    print(f"the number of overweight persons is {overweigth_count}")
