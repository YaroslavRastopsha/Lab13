import csv
import json
import os

# === Yaroslav Rastopsha: Creating CSV file and converting it to JSON ===

# File names for Yaroslav Rastopsha
csv_filename = 'data.csv'
json_filename = 'data.json'

# Data to be written to the CSV file
data = [
    {"id": 1, "name": "Alice", "age": 23},
    {"id": 2, "name": "Bob", "age": 27},
    {"id": 3, "name": "Charlie", "age": 22}
]

# Function to write data to CSV file
def write_csv(filename, data):
    try:
        with open(filename, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["id", "name", "age"])
            writer.writeheader()
            writer.writerows(data)
        print(f"Data successfully written to {filename}")
    except IOError as e:
        print(f"Error writing to CSV file: {e}")

# Function to convert CSV file to JSON
def csv_to_json(csv_filename, json_filename):
    try:
        with open(csv_filename, mode='r') as csv_file:
            reader = csv.DictReader(csv_file)
            data = [row for row in reader]

        with open(json_filename, mode='w') as json_file:
            json.dump(data, json_file, indent=4)
        print(f"Data successfully converted from {csv_filename} to {json_filename}")
    except FileNotFoundError as e:
        print(f"File not found: {e}")
    except IOError as e:
        print(f"Error during file operation: {e}")

# Execution for Yaroslav Rastopsha
write_csv(csv_filename, data)
csv_to_json(csv_filename, json_filename)

