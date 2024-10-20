import re

# Define the pattern for a valid Indian number plate
number_plate_pattern = r'^[A-Z]{2} \d{2} [A-Z]{2} \d{4}$'

# Function to check if the number plate is valid
def is_valid_number_plate(plate):
    if re.match(number_plate_pattern, plate):
        return True
    return False

# Input from user
number_plate = input("Enter the number plate (format: XX NN YY NNNN): ")

# Validate the number plate
if is_valid_number_plate(number_plate):
    print(f"{number_plate} is a valid Indian number plate.")
else:
    print(f"{number_plate} is not a valid Indian number plate.")
