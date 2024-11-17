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

# === Maksym Hryhorenko: Converting JSON to CSV with added rows ===

# File names for Maksym Hryhorenko
json_filename = 'data.json'
updated_csv_filename = 'updated_data.csv'

# Additional data for the second CSV file
additional_data_2 = [
    {"id": 4, "name": "Diana", "age": 29},
    {"id": 5, "name": "Ethan", "age": 31}
]

# Function to read JSON and write to CSV with additional rows
def json_to_csv_with_addition(json_filename, csv_filename, additional_data):
    try:
        # Reading data from JSON file
        with open(json_filename, mode='r') as json_file:
            data = json.load(json_file)
        
        # Adding new rows to data
        data.extend(additional_data)
        
        # Writing data to new CSV file
        with open(csv_filename, mode='w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=["id", "name", "age"])
            writer.writeheader()
            writer.writerows(data)
        print(f"Data successfully written to {csv_filename} with additional rows")
    except FileNotFoundError as e:
        print(f"File not found: {e}")
    except IOError as e:
        print(f"Error during file operation: {e}")

# Execution for Maksym Hryhorenko
json_to_csv_with_addition(json_filename, updated_csv_filename, additional_data_2)

# === Mark Holovenko: Converting updated CSV to JSON with added rows ===

# File names for Mark Holovenko
updated_csv_filename = 'updated_data.csv'
final_json_filename = 'final_data.json'

# Additional data for the final JSON file
additional_data_3 = [
    {"id": 6, "name": "Frank", "age": 26},
    {"id": 7, "name": "Grace", "age": 28}
]

# Function to read CSV and write to JSON with additional rows
def csv_to_json_with_addition(csv_filename, json_filename, additional_data):
    try:
        # Reading data from CSV file
        with open(csv_filename, mode='r') as csv_file:
            reader = csv.DictReader(csv_file)
            data = [row for row in reader]
        
        # Adding new rows to data
        data.extend(additional_data)
        
        # Writing data to new JSON file
        with open(json_filename, mode='w') as json_file:
            json.dump(data, json_file, indent=4)
        print(f"Data successfully written to {json_filename} with additional rows")
    except FileNotFoundError as e:
        print(f"File not found: {e}")
    except IOError as e:
        print(f"Error during file operation: {e}")

# Execution for Mark Holovenko
csv_to_json_with_addition(updated_csv_filename, final_json_filename, additional_data_3)