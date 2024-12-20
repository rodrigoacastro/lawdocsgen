# All functions

import os
import json
import re
import pandas as pd

def extract_fields_from_file(file_path):
    """
    Extract fields from an HTML file.

    Args:
    - file_path (str): Path to the HTML file to extract fields from.

    Returns:
    - dict: A dictionary containing the extracted fields. The keys are the extracted
            fields, and the values are set to the same value as the keys.

    Raises:
    - FileNotFoundError: If the specified HTML file is not found.
    - Exception: If an error occurs during the extraction process.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            html_content = file.read()

            # Define regex pattern for extracting fields in the format [value]
            field_pattern = re.compile(r'\[([^\]]*)\]')

            # Extract all fields in the format [value]
            matches = field_pattern.findall(html_content)
            print(f'matches: {matches}')
            
            # Creating a dictionary with the extracted values
            result = {'success': {match: match for match in matches}}

            return result

    except FileNotFoundError:
        return {'error': 'File not found'}
    except Exception as e:
        return {'error': f'An error occurred while extracting fields: {str(e)}'}

def save_to_json(data, output_file):
    """
    Save data to a JSON file.

    Args:
    - data (dict): Data to be saved to the JSON file.
    - output_file (str): Path to the JSON file where the data will be saved.

    Returns:
    - str: Message indicating success or failure. If successful, returns the message
           'Data saved to JSON file successfully: [output_file]'. If an error occurs,
           returns the error message.
    """
    try:
        with open(output_file, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=2) 
        print(f'Data saved to JSON file successfully: {output_file}')
        return ( json.dumps(data) ) # returns object
    except Exception as e:
        return f'An error occurred while saving to JSON file: {str(e)}'

def process_file_and_save_to_json(file_path, output_json_file):
    """
    Convert an HTML file to a DOCX file using htmldocx.

    Args:
    - input_html_file (str): Path to the input HTML file.
    - output_folder (str): Path to the folder where the DOCX file will be saved.

    Returns:
    - str: Message indicating success or failure.
    """
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


# def fill_html_with_json(template_path, json_data, output_folder):
#     """
#     Fill an HTML template with data from a JSON and save the result.

#     Args:
#         template_path (str): The path to the HTML template file.
#         json_data (list): A list of dictionaries containing the data to be inserted into the HTML.
#         output_folder (str): The path to the output folder where HTML files will be saved.

#     Returns:
#         None
#     """

#     # Ensure the output folder exists; create it if not
#     # os.makedirs(output_folder, exist_ok=True)

#     # Load the content of the HTML template file
#     with open(template_path, 'r', encoding='utf-8') as template_file:
#         template_content = template_file.read()

#     # Loop through the data sets in the JSON and substitute in the HTML
#     for data in json_data:
#         # Create a unique identifier for each field (using Nome and Data fields as an example)
#         unique_identifier = f"{data['Nome']}_{data['Data']}"
        
#         # Construct the output filename with the unique identifier
#         output_filename = os.path.join(output_folder, f"output_{unique_identifier}.html")

#         # Substitute data in the HTML template
#         html_filled = template_content.format_map(data)

#         # Save the filled HTML to the output file
#         with open(output_filename, 'w', encoding='utf-8') as output_file:
#             output_file.write(html_filled)



def fill_html_with_json(json_data, template_path, output_folder):
    """
    Fill an HTML template with data from a JSON and save the result.

    Args:
        template_path (str): The path to the HTML template file.
        json_data (list): A list of dictionaries containing the data to be inserted into the HTML.
        output_folder (str): The path to the output folder where HTML files will be saved.

    Returns:
        None
    """
    try:
        # Ensure the output folder exists; create it if not
        os.makedirs(output_folder, exist_ok=True)

        # Load the content of the HTML template file
        with open(template_path, 'r', encoding='utf-8') as template_file:
            template_content = template_file.read()

        # Loop through the data sets in the JSON and substitute in the HTML
        for data in json_data:
            # Create a unique identifier for each field (using Nome and Data fields as an example)
            unique_identifier = f"{data.get('Nome', '')}_{data.get('Data', '')}"
            
            # Construct the output filename with the unique identifier
            output_filename = os.path.join(output_folder, f"output_{unique_identifier}.html")

            try:
                # Substitute data in the HTML template
                html_filled = template_content.format_map(data)

                # Save the filled HTML to the output file
                with open(output_filename, 'w', encoding='utf-8') as output_file:
                    output_file.write(html_filled)
            except Exception as e:
                print(f'Error: Could not create output HTML file {output_filename}. {str(e)}')

    except FileNotFoundError:
        print(f'Error: Template file not found: {template_path}')
    except Exception as e:
        print(f'An error occurred: {str(e)}')

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


def fill_html_with_json2(json_data, template_path, output_folder):
    """
    Fill an HTML template with data from a JSON and save the result.

    Args:
        json_data (list or dict): If a list, it should contain dictionaries with the data to be inserted into the HTML.
                                  If a dict, it should be a single dictionary with the data for one person.
        template_path (str): The path to the HTML template file.
        output_folder (str): The path to the output folder where HTML files will be saved.

    Returns:
        None
    """
    try:
        # Ensure the output folder exists; create it if not
        os.makedirs(output_folder, exist_ok=True)

        # Load the content of the HTML template file
        with open(template_path, 'r', encoding='utf-8') as template_file:
            template_content = template_file.read()

        # print(template_content)
        # If json_data is a single dictionary, convert it to a list for uniform processing

        # print(f'json_data type: {type(json_data)}')

        if isinstance(json_data, str):
            # print(f'json_data is string')
            json_data = json.loads(json_data) # convert dict-like string into dictionary object
            # print(f'json_data type: {type(json_data)}')

        if isinstance(json_data, dict):
            json_data = [json_data]
            # print(f'json_data: {json_data}') # test
            '''
            json_data: [{'Nome': 'Nome', 'RG': 'RG', 'CPF': 'CPF', 
            'Nome do Documento': 'Nome do Documento', 'Nome do Cartório': 'Nome do Cartório', 
            'Cidade': 'Cidade', 'Data': 'Data'}]                                                               
            '''
            # print('essa parte rodou agora')

        # Loop through the data sets in the JSON and substitute in the HTML
        # print(f'json_data: {json_data}') # test
        for data in json_data:
            print(f'data: {data}') # test
            '''
            data: {'Nome': 'Nome', 'RG': 'RG', 'CPF': 'CPF', 'Nome do Documento': 'Nome do Documento', 
            'Nome do Cartório': 'Nome do Cartório', 'Cidade': 'Cidade', 'Data': 'Data'}
            '''
            # Create a unique identifier for each field (using Nome and Data fields as an example)
            unique_identifier = f"{data.get('Nome', '')}_{data.get('Data', '')}"
            # print(f'unique_identifier: {unique_identifier}')
            # Nome_Data

            # Construct the output filename with the unique identifier
            output_filename = os.path.join(output_folder, f"output_{unique_identifier}.html")
            print(f'output_filename: {output_filename}')
            # ./output/html/output_Nome_Data.html

            try:
                # Substitute data in the HTML template
                html_filled = template_content.format_map(data)
                # print(f'html_filled: {html_filled}')


                # Save the filled HTML to the output file
                with open(output_filename, 'w', encoding='utf-8') as output_file:
                    output_file.write(html_filled)
            except Exception as e:
                print(f'Error: Could not create output HTML file {output_filename}. {str(e)}')

    except FileNotFoundError:
        print(f'Error: Template file not found: {template_path}')
    except Exception as e:
        print(f'An error occurred: {str(e)}')


def read_json_and_extract_values(json_file_path):
    try:
        with open(json_file_path, 'r') as file:
            data = json.load(file)

            if isinstance(data, list):
                # If the JSON data is a list, create a list of dictionaries with index as key
                result_list = [{str(index): value} for index, value in enumerate(data)]
            elif isinstance(data, dict):
                # If the JSON data is a dictionary, create a list of dictionaries with keys as in the JSON
                result_list = [{key: value} for key, value in data.items()]
            else:
                print("Error: Unsupported JSON format. It should be either a list or a dictionary.")
                return None

            return result_list

    except FileNotFoundError:
        print(f"Error: File not found at path {json_file_path}")
        return None
    except json.JSONDecodeError:
        print(f"Error: Unable to decode JSON from {json_file_path}")
        return None

# Example usage:
# json_file_path = 'path/to/your/json/file.json'
# result = read_json_and_extract_values(json_file_path)
# print(result)


def iterate_through_data(json_data):
    for data_dict in json_data:
        for value in data_dict.values():
            yield value

def return_dict_from_dictlist(json_data_list):
    for result_values in iterate_through_data(json_data_list):
        return result_values
    
def output_all_final_docs(json_data_list, template_path:str = './templates/html/procuracao_mock1.html', output_folder:str = './output/html/'):
    for json_output in iterate_through_data(json_data_list):
        fill_html_with_json2(json_data = json_output, 
                             template_path = template_path,
                             output_folder = output_folder)
                                    
                                    # template_path = './templates/html/procuracao_mock1.html', 
                                    # output_folder = './output/html/'

