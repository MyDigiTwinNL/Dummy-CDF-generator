import json
import random
import sys
import os
import glob
import string

# Function to load a template from a JSON file
def load_template(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# Function to generate a random alphanumeric string of a specified length
def generate_alphanumeric(length):
    alphabet = string.ascii_letters + string.digits
    return ''.join(random.choice(alphabet) for _ in range(length))

# Check if arguments were provided
if len(sys.argv) < 3:
    print("Usage: python script.py <number_of_files> <output_directory>")
    sys.exit(1)

try:
    N = int(sys.argv[1])
    output_dir = sys.argv[2]
except ValueError:
    print("Error: Arguments must be integers.")
    sys.exit(1)

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# List all JSON files in the 'samples' folder
templates_folder = 'samples'
template_files = glob.glob(os.path.join(templates_folder, '*.json'))

# Generate N JSON files
for i in range(N):
    # Select a template randomly
    template_file = random.choice(template_files)
    template = load_template(template_file)
    
    # Modify the template with a new random alphanumeric pseudo ID
    template["project_pseudo_id"]["1a"] = generate_alphanumeric(45)
    
    # Convert the modified template to a JSON string
    json_str = json.dumps(template, indent=4)
    
    # Determine the filename and full path for the output file
    filename = f"{output_dir}/output_{i+1}.json"
    
    # Write the JSON string to a file
    with open(filename, 'w') as file:
        file.write(json_str)

    print(f"Generated file {filename} using template {template_file}")
