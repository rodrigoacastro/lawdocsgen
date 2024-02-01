# import libraries
import os
import re
import json
import pandas as pd

from utils.functions import *

# store functions temporarily, before using a different file with functions 
# or with classes and methods

# Replace 'your_file_path.html' with the actual path to your HTML file

template_json_data = process_file_and_save_to_json(file_path = './templates/html/procuracao_mock1.html',
                                           output_json_file = './templates/json/html_fields.json')

# def process_file_and_save_to_json(data, template_content, output_folder):



# print(json_data)
'''
{"Nome": "Nome", "RG": "RG", "CPF": "CPF", "Nome do Documento": "Nome do Documento", 
"Nome do Cart\u00f3rio": "Nome do Cart\u00f3rio", "Cidade": "Cidade", "Data": "Data"}
'''

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



# Clear the content of the output file
# with open(output_path, 'w', encoding='utf-8'):
#     pass

# Call the function to fill the HTML with data from the JSON

# testing
json_data = {"Nome": "NomeB", "RG": "RG2", "CPF": "CPF2", "Nome do Documento": "Nome do Documento2", 
"Nome do Cart\u00f3rio": "Nome do Cart\u00f3rio2", "Cidade": "Cidade2", "Data": "DataB"}

json_data2 = read_json_and_extract_values("./templates/json/fields_to_fill2.json")

# print(json_data2[0].keys())
'''
[{'0': {'Nome': 'Fulano de Tal', 'RG': '1234567', 'CPF': '98765432100', 'Nome do Documento': 'Certidão de Nascimento', 
'Nome do Cartório': 'Cartório ABC', 'Cidade': 'Cidade A', 'Data': '2024-01-20'}}, 
{'1': {'Nome': 'Ciclana Oliveira', 'RG': '9876543', 'CPF': '12345678901', 'Nome do Documento': 'Carteira de Identidade', 
'Nome do Cartório': 'Cartório XYZ', 'Cidade': 'Cidade B', 'Data': '2024-01-21'}}]
data: {'Nome': 'NomeB', 'RG': 'RG2', 'CPF': 'CPF2', 'Nome do Documento': 'Nome do Documento2', 'Nome do Cartório': 'Nome do Cartório2', 'Cidade': 'Cidade2', 'Data': 'DataB'}
'''

# dict1 = return_dict_from_dictlist (json_data2)
# print(f'dict1: {dict1}')

# fills the html template with the json data
# result_message = fill_html_with_json2(json_data = json_data, 
#                                     template_path = './templates/html/procuracao_mock1.html', 
#                                     output_folder = './output/html/'
# )

output_all_final_docs(json_data_list = json_data2, 
                      template_path = './templates/html/procuracao_mock1.html', 
                      output_folder = './output/html/')
