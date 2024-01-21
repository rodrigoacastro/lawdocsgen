import re
import json

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

# Replace 'your_file_path.html' with the actual path to your HTML file
file_path = './templates/html/procuracao_mock1.html'
output_json_file = './templates/json/html_fields.json'

result = process_file_and_save_to_json(file_path, output_json_file)
print(result)

