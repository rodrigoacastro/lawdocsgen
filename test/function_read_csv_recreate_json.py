import pandas as pd
import json

def read_template_json(template_path):
    """
    Read the template JSON file.

    Args:
    - template_path (str): Path to the template JSON file.

    Returns:
    - dict: Loaded template JSON.
    """
    with open(template_path, 'r', encoding='utf-8') as template_file:
        return json.load(template_file)

def process_csv_and_save_to_json(csv_path, template_json, output_json_path):
    """
    Read a CSV file, process each row, and save the result to a new JSON file.

    Args:
    - csv_path (str): Path to the CSV file.
    - template_json (dict): Template JSON to use as a base.
    - output_json_path (str): Path to save the resulting JSON file.

    Returns:
    - str: Message indicating success or failure.
    """
    try:
        # Read the CSV file using pandas
        df = pd.read_csv(csv_path)

        # Create a list to store the resulting JSON objects
        json_objects = []

        # Iterate through rows in the CSV file
        for index, row in df.iterrows():
            # Create a copy of the template JSON
            new_json = template_json.copy()

            # Replace values in the template JSON with values from the CSV row
            for key, value in row.items():
                if key in new_json:
                    new_json[key] = str(value)

            # Append the modified JSON to the list
            json_objects.append(new_json)

        # Save the list of JSON objects to a new JSON file
        with open(output_json_path, 'w', encoding='utf-8') as output_file:
            json.dump(json_objects, output_file, indent=2)

        return f'Data saved to {output_json_path}'

    except Exception as e:
        return f'An error occurred: {str(e)}'

# Replace 'your_template.json', 'your_csv_file.csv', and 'output.json' with your actual file paths
template_path = 'your_template.json'
csv_path = 'your_csv_file.csv'
output_json_path = 'output.json'

# Read the template JSON
template_json = read_template_json(template_path)

# Process the CSV and save to JSON
result_message = process_csv_and_save_to_json(csv_path, template_json, output_json_path)
print(result_message)
