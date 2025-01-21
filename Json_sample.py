import json

# Sample data
data = {
    "name": "John Doe",
    "age": 30,
    "city": "New York",
    "is_student": False,
    "grades": [85, 90, 88]
}

# Define the file path where you want to write the JSON data
file_path = "C:\\Users\\KIIT\Desktop\\100Days_code_programming\\data.json"

# Write data to JSON file
with open(file_path, "w") as json_file:
    json.dump(data, json_file, indent=4)

print("Data has been written to", file_path)
