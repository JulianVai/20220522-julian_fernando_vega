# BMI CALCULATOR

A functional approach to calculate the `bmi` from a given batch of data of the form:

```json
[{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 },
    { "Gender": "Male", "HeightCm": 161, "WeightKg": 85 },
    { "Gender": "Male", "HeightCm": 180, "WeightKg": 77 },
    { "Gender": "Female", "HeightCm": 166, "WeightKg": 62},
    {"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
    {"Gender": "Female", "HeightCm": 167, "WeightKg": 82}]
```

## Installation
```
pip install -r requirements.txt
```

## Usage
```bash
# 1. Create an  environment on project's directory.
$ python -m venv venv

# 2. Activate environment
$ source venv/bin/activate

# 3. Create a random set of test data of [n_examples]; size by default a set of size 4 will be created
$ python create_data.py [n_examples]

# 4. execute the bmi_calculator.py file
$ python bmi_calculator.py
The number of overweight persons is [number_calculated]
```

## Tests
To run tests once the requirements has been instaled:
```bash
$ pytest
```

