# import libraries
import os
import json
import pandas as pd

# store functions temporarily, before using a different file with functions 
# or with classes and methods

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
    os.makedirs(output_folder, exist_ok=True)

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

# Example usage
json_data = [
    {
        "[Nome]": "Fulano de Tal",
        "[RG]": "1234567",
        "[CPF]": "98765432100",
        "[NomeDocumento]": "Certidão de Nascimento",
        "[NomeCartorio]": "Cartório ABC",
        "[Cidade]": "City A",
        "[Data]": "20/10/2023"
    },
    {
        "Nome": "Ciclana Oliveira",
        "RG": "9876543",
        "CPF": "12345678901",
        "NomeDocumento": "Carteira de identidade",
        "NomeCartorio": "Cartório XYZ",
        "Cidade": "City B",
        "Data": "20/09/2023"
    }
]

template_path = 'templates/html/procuracao_mock1.html'
output_path = 'output/html/procuracao_completa_mock1.html'

# Clear the content of the output file
with open(output_path, 'w', encoding='utf-8'):
    pass

# Call the function to fill the HTML with data from the JSON
fill_html_with_json(template_path, json_data, output_path)


