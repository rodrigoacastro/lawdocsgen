from htmldocx import HtmlToDocx

def convert_html_to_docx(input_html_file, output_folder):
    """
    Convert an HTML file to a DOCX file using htmldocx.

    Args:
    - input_html_file (str): Path to the input HTML file.
    - output_folder (str): Path to the folder where the DOCX file will be saved.

    Returns:
    - str: Message indicating success or failure.
    """
    try:
        parser = HtmlToDocx()
        output_docx_file = os.path.join(output_folder, 'output.docx')
        parser.parse_html_file(input_html_file, output_docx_file)
        return f'Document converted successfully. Output saved to {output_docx_file}'
    except Exception as e:
        return f'An error occurred: {str(e)}'

# Example usage:
# Replace 'path/to/your/input.html' with the actual path to your input HTML file
input_html_file = 'path/to/your/input.html'

# Replace 'path/to/your/output/folder' with the actual path to your output folder
output_folder = 'path/to/your/output/folder'

# Call the function
result_message = convert_html_to_docx(input_html_file, output_folder)
print(result_message)
