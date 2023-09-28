import os

def txt_to_html(input_file, output_file):
    # Open the input file in read mode
    try:
        with open(input_file, 'r', encoding='utf-8') as txt_file:
            # Read the content of the text file
            txt_content = txt_file.read()
    except FileNotFoundError:
        print(f"File '{input_file}' not found.")
        return

    # Create an "html" directory if it doesn't exist already
    html_dir = 'html'
    if not os.path.exists(html_dir):
        os.makedirs(html_dir)

    # Create the full path for the output file within the "html" directory
    output_file = os.path.join(html_dir, output_file.replace('.txt', '_html.html'))

    # Open the output file in write mode
    with open(output_file, 'w', encoding='utf-8') as html_file:
        # Write the HTML header
        html_file.write("<!DOCTYPE html>\n<html>\n<head>\n<title>Conversion from TXT to HTML</title>\n</head>\n<body>\n")

        # Write the content of the text file inside a <pre> tag
        html_file.write("<pre>\n")
        html_file.write(txt_content)
        html_file.write("\n</pre>\n")

        # Close the <body> tag and the HTML
        html_file.write("</body>\n</html>\n")

    print(f"Conversion completed. The HTML file '{output_file}' has been created.")

# Get a list of files in the current directory
file_list = [f for f in os.listdir() if f.endswith('.txt')]

# Loop through each .txt file and convert them to HTML
for txt_file in file_list:
    txt_to_html(txt_file, txt_file)  # The HTML file will have the same name as the text file