# import libraries
import os
import re
import json
import pandas as pd

from utils.functions import *

# store functions temporarily, before using a different file with functions 
# or with classes and methods

# Replace 'your_file_path.html' with the actual path to your HTML file
file_path = './templates/html/procuracao_mock1.html'
output_json_file = './templates/json/html_fields.json'

json_data = process_file_and_save_to_json(file_path, output_json_file)

# def process_file_and_save_to_json(data, template_content, output_folder):


print(json_data)

# # Example usage
# json_data = [
#     {
#         "[Nome]": "Fulano de Tal",
#         "[RG]": "1234567",
#         "[CPF]": "98765432100",
#         "[NomeDocumento]": "Certidão de Nascimento",
#         "[NomeCartorio]": "Cartório ABC",
#         "[Cidade]": "City A",
#         "[Data]": "20/10/2023"
#     },
#     {
#         "[Nome]": "Ciclana Oliveira",
#         "[RG]": "9876543",
#         "[CPF]": "12345678901",
#         "[NomeDocumento]": "Carteira de identidade",
#         "[NomeCartorio]": "Cartório XYZ",
#         "[Cidade]": "City B",
#         "[Data]": "20/09/2023"
#     }
# ]

template_path = './templates/html/procuracao_mock1.html'
output_path = './output/html/'

print('rodou até aqui')

# Clear the content of the output file
# with open(output_path, 'w', encoding='utf-8'):
#     pass

# # Call the function to fill the HTML with data from the JSON
# fill_html_with_json(template_path, json_data, output_path)

# result_message = fill_html_with_json(json_data, template_content, output_folder)

result_message = fill_and_save_html(json_data, template_path, output_path)

