import json
import random
import argparse
import os
import glob
import string

def load_template(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def generate_alphanumeric(length):
    alphabet = string.ascii_letters + string.digits
    return ''.join(random.choice(alphabet) for _ in range(length))

# Set up argument parser
parser = argparse.ArgumentParser(description='Generate dummy JSON files based on templates.')
parser.add_argument('number_of_files', type=int, help='Number of files to generate')
parser.add_argument('output_directory', type=str, help='Output directory for generated files')
parser.add_argument('--initial_index', type=int, default=0, help='Initial index for naming files (default: 0)')
args = parser.parse_args()

# Ensure the output directory exists
os.makedirs(args.output_directory, exist_ok=True)

templates_folder = 'samples'
template_files = glob.glob(os.path.join(templates_folder, '*.json'))

for i in range(args.number_of_files):
    template_file = random.choice(template_files)
    template = load_template(template_file)

    template["project_pseudo_id"]["1a"] = generate_alphanumeric(45) + str(i+args.initial_index)

    json_str = json.dumps(template, indent=4)

    # Adjust filename to start counting from initial_index
    filename = f"{args.output_directory}/output_{i + args.initial_index}.json"

    with open(filename, 'w') as file:
        file.write(json_str)

    print(f"Generated file {filename} using template {template_file}")
