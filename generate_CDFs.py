import json
import random
import sys
import os

# Define the template JSON document
template = {
    "project_pseudo_id": {"1a":"9999"},
    "variant_id": {},

    "date": {"1a":"1990-1","1b":"1995-5","1c":"1997-5","2a":"2000-1","2b":"2001-1","3a":"2003-5","3b":"2005-5"},
    "age": { "1a": "40" },  
    "gender": {"1a":"FEMALE"},
    "date_of_death": {"global":""},
    "date_of_inclusion": {"global":"1991-2"},

    "albumin_result_all_m_1" :{ "1a": "34"},
    "creatinine_result_all_m_1":{ "1a": "79.2", "2a":"106.1"},
    "ethnicity_category_adu_q_1":{"1b":"1"},
    "hemoglobin_result_all_m_1" :{ "1a": "6", "2a":"12"},  
    "hba1cconc_result_all_m_1":{ "1a": "43", "2a":"44"},  

    "zip_code": {"1a":"11111"},

    "hypertension_startage_adu_q_1":{"1a":"","3a":"23","3b":"23"},
    "hypertension_presence_adu_q_1":{"1a":"2","3a":"1","3b":"1"},

    "stroke_startage_adu_q_1":{ "1a": "12" },
    "stroke_presence_adu_q_1": { "1a": "1" },
    "stroke_followup_adu_q_1":{"2a":"2","3a":"2","3b":"2"},


    "diabetes_presence_adu_q_1":    {"1a":"1"},
    "diabetes_startage_adu_q_1":    {"1a":"28"},
    "diabetes_followup_adu_q_1":        {"1b":"2","1c":"2","2a":"2","3a":"2","3b":"2"},
    "diabetes_type_adu_q_1":        {"1a":"2"},
    "diabetes_type_adu_q_1_a":      {"1a":""},
    "t1d_followup_adu_q_1":                 {"2a":"2","3a":"2","3b":"2"},
    "t2d_followup_adu_q_1":                 {"2a":"2","3a":"2","3b":"2"},

    "bp_entrytype_all_m_1":         {"1a":"2","2a":"2"},
    "bp_bandsize_all_m_1":          {"1a":"1","2a":"1","3a":"1"},
    "bp_arm_all_m_1":                           {"3a":"2"},
    "bpavg_systolic_all_m_1":       {"1a":"","2a":""},
    "bpavg_diastolic_all_m_1":      {"1a":"","2a":""},
    "bpavg_arterial_all_m_1":       {"1a":"","2a":"113"},

    "hdlchol_result_all_m_1":       {"1a":"","2a":"0.32"},
    "ldlchol_result_all_m_1":       {"1a":"0.41","2a":""},
    "cholesterol_result_all_m_1":   {"1a":"0.51","2a":"0.52"},
    
    "heartattack_startage_adu_q_1": {"1a":"33"},
    "angioplasty_bypass_adu_q_1_a":  {"1a":"1","3a":"1","3b":"1"},
    "heartattack_presence_adu_q_1": {"1a":"1"},
    "heartattack_followup_adu_q_1":     {"1b":"2","1c":"2","2a":"2","3a":"2","3b":"2"},
    "angioplasty_bypass_adu_q_1":   {"1a":"1","3a":"1","3b":"1"},
    "carotid_stenosis_adu_q_1":     {"1a":"1"},
    "claudication_followup_adu_q_1":            {"2a":"2","3a":"2","3b":"2"},
    "cvd_followup_adu_q_1":             {"1b":"2","1c":"2","2a":"2","3a":"2","3b":"2"},

    "current_smoker_adu_c_2": { "1a": "0", "1b": "0", "1c": "0", "2a": "0", "2b": "0", "3a": "0" },
    "smoking_startage_adu_c_2": { "1a": "5", "1b": "5", "1c": "5", "2a": "5", "2b": "5", "3a": "5" },
    "ex_smoker_adu_c_2": { "1a": "1", "1b": "1", "1c": "1", "2a": "1", "2b": "1", "3a": "1" },
    "smoking_endage_adu_c_2": { "1a": "8", "1b": "8", "1c": "8", "2a": "8", "2b": "8", "3a": "8"},
    "ever_smoker_adu_c_2": { "1a": "1", "1b": "1", "1c": "1", "2a": "1", "2b": "1", "3a": "1"},
    "total_frequency_adu_c_1": { "1a": "", "1b": "", "1c": "", "2a": "", "2b": "", "3a": ""},
    "packyears_cumulative_adu_c_2": { "1a": "", "1b": "", "1c": "", "2a": "", "2b": "", "3a": ""}
}

# Function to generate a random project pseudo ID
def generate_random_project_pseudo_id():
    return str(random.randint(1000, 9999))

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

# Generate N JSON files
for i in range(N):
    # Modify the template with a new random project pseudo ID
    template["project_pseudo_id"]["1a"] = generate_random_project_pseudo_id()
    
    # Convert the modified template to a JSON string
    json_str = json.dumps(template, indent=4)
    
    # Determine the filename and full path for the output file
    filename = f"{output_dir}/output_{i+1}.json"
    
    # Write the JSON string to a file
    with open(filename, 'w') as file:
        file.write(json_str)

    print(f"Generated file {filename}")