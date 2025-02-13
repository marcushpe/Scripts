import json

# Sample JSON data as a string
json_data = '''
{
    "name": "Jane Doe",
    "age": 25,
    "city": "New York"
}
'''

# Parse JSON data and assign it to a variable
data = json.loads(json_data)

# Print the data to verify
print(data)