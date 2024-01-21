# All functions


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
        return 'Data saved to JSON file successfully'

    except Exception as e:
        return f'An error occurred while saving to JSON file: {str(e)}'

def process_file_and_save_to_json(file_path, output_json_file):
    result_fields = extract_fields_from_file(file_path)

    if 'error' in result_fields:
        return result_fields['error']
    else:
        save_result = save_to_json(result_fields.get('success', {}), output_json_file)
        return save_result
