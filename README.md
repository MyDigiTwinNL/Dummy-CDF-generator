# Dummy CDF (Cohort Data Format) data generator

This Python script is designed to streamline the creation of Cohort Data Format (CDF) JSON files for load-testing purposes, particularly aimed at evaluating queries and data 
transformations' performance. The script automates the generation of CDF files with unique identifiers, leveraging sample templates stored in a dedicated directory.

## Functionality

- **Unique Identifiers**: Each generated CDF file is assigned a unique identifier, ensuring distinctiveness among the test datasets.
- **Template-Based Generation**: The content of the generated CDF files is derived from sample templates located in the `./samples` directory. This approach allows users to tailor 
the characteristics of the dummy samples by modifying or adding new templates accordingly.

## Usage Instructions

To utilize this script effectively, follow these steps:

1. **Prepare Sample Templates**: Place your sample CDF templates in the `./samples` folder. Ensure these templates reflect the desired characteristics for your testing scenarios.
2. **Execute the Script**: Run the script from the command line, specifying the number of files to generate and the output directory. For example:
   ```bash
   python script.py 10 ./test_cdfs
   ```
   This command instructs the script to generate 10 CDF files in the `./test_cdfs` directory.

## Customization

To tailor the generated CDF files to specific testing requirements, modify the sample templates in the `./samples` folder. By adjusting these templates, you can control the 
structure and content of the generated files, thereby simulating various data scenarios for performance testing.
