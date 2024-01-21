# All functions

import os
import json
import re
import pandas as pd


def fill_html_with_json(template_path, json_data, output_folder):
    """
    Fill an HTML template with data from a JSON and save the result.

    Args:
        template_path (str): The path to the HTML template file.
        json_data (list): A list of dictionaries containing the data to be inserted into the HTML.
        output_folder (str): The path to the output folder where HTML files will be saved.

    Returns:
        None
    """

    # Ensure the output folder exists; create it if not
    # os.makedirs(output_folder, exist_ok=True)

    # Load the content of the HTML template file
    with open(template_path, 'r', encoding='utf-8') as template_file:
        template_content = template_file.read()

    # Loop through the data sets in the JSON and substitute in the HTML
    for data in json_data:
        # Create a unique identifier for each field (using Nome and Data fields as an example)
        unique_identifier = f"{data['Nome']}_{data['Data']}"
        
        # Construct the output filename with the unique identifier
        output_filename = os.path.join(output_folder, f"output_{unique_identifier}.html")

        # Substitute data in the HTML template
        html_filled = template_content.format_map(data)

        # Save the filled HTML to the output file
        with open(output_filename, 'w', encoding='utf-8') as output_file:
            output_file.write(html_filled)


def extract_fields_from_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            html_content = file.read()

            # Define regex pattern for extracting fields in the format [value]
            field_pattern = re.compile(r'\[([^\]]*)\]')

            # Extract all fields in the format [value]
            matches = field_pattern.findall(html_content)

            # Creating a dictionary with the extracted values
            result = {'success': {match: match for match in matches}}

            return result

    except FileNotFoundError:
        return {'error': 'File not found'}
    except Exception as e:
        return {'error': f'An error occurred while extracting fields: {str(e)}'}

def save_to_json(data, output_file):
    try:
        with open(output_file, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=2)
        return f'Data saved to JSON file successfully: {output_file}'

    except Exception as e:
        return f'An error occurred while saving to JSON file: {str(e)}'

def process_file_and_save_to_json(file_path, output_json_file):
    result_fields = extract_fields_from_file(file_path)

    if 'error' in result_fields:
        return result_fields['error']
    else:
        save_result = save_to_json(result_fields.get('success', {}), output_json_file)
        return save_result


def fill_and_save_html(data, template_file_path, output_folder):
    """
    Substitute data into an HTML template and save the filled HTML to a file.

    Args:
    - data (dict): Dictionary containing data to substitute into the template.
    - template_file_path (str): Path to the HTML template file.
    - output_folder (str): Path to the folder where the filled HTML will be saved.

    Returns:
    - str: Message indicating success or failure.
    """
    try:
        # Read the HTML template from the file
        with open(template_file_path, 'r', encoding='utf-8') as template_file:
            template_content = template_file.read()

        # Create a unique identifier for each field (using Nome and Data fields as an example)
        unique_identifier = f"{data.get('Nome', '')}_{data.get('Data', '')}"

        # Construct the output filename with the unique identifier
        output_filename = os.path.join(output_folder, f"output_{unique_identifier}.html")

        # Substitute data in the HTML template
        html_filled = template_content.format_map(data)

        # Save the filled HTML to the output file
        with open(output_filename, 'w', encoding='utf-8') as output_file:
            output_file.write(html_filled)

        return f'Data saved to {output_filename}'

    except Exception as e:
        return f'An error occurred: {str(e)}'


# Example usage:
# template_content = """
# <html>
# <head>
#     <title>{Nome}'s Document - {Data}</title>
# </head>
# <body>
#     <h1>{Nome}'s Document</h1>
#     <p>City: {Cidade}</p>
#     <p>Document Type: {Nome do Documento}</p>
#     <!-- Add more placeholders as needed -->
# </body>
# </html>
# """

# # Replace 'your_output_folder' with the actual path to your output folder
# output_folder = 'your_output_folder'

# # Replace 'your_json_data.json' with the actual path to your JSON data file
# json_data_path = 'your_json_data.json'

# # Read the JSON data
# with open(json_data_path, 'r', encoding='utf-8') as json_file:
#     json_data = json.load(json_file)

# # Call the function
# result_message = fill_and_save_html(json_data, template_content, output_folder)
# print(result_message)
