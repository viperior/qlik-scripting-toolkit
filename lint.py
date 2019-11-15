# Program Goal: Given the input of a text file containing a multi-line Qlik
#  script, produce an output file with the same script but with code style
#  and formatting improvements applied.

def add_trailing_comma_to_string(text):
    return text + ','

def count_lines_in_file(file_path):
    with open(file_path, 'r') as file:
        line_count = 1

        for line in file:
            line_count += 1

    return line_count

def enclose_string_in_brackets(text):
    return '[' + text + ']'

def process_line(line, current_line_number, file_line_count, field_prefix):
    new_line_content = str.strip(line)
    new_line_content = remove_trailing_comma_from_string(new_line_content)
    new_line_content = remove_double_quotes_from_string(new_line_content)

    if field_prefix:
        new_line_content = field_prefix + ' ' + new_line_content

    new_line_content = enclose_string_in_brackets(new_line_content)

    if current_line_number < file_line_count - 1:
        new_line_content = add_trailing_comma_to_string(new_line_content)

    return new_line_content

def process_qlik_field_list(field_prefix=''):
    input_file_directory = './input/'
    input_file_name = 'input.txt'
    output_file_directory = './output/'
    output_file_name = 'output.txt'
    input_file_path = input_file_directory + input_file_name
    ouput_file_path = output_file_directory + output_file_name

    with open(input_file_path, 'r') as input_file:
        current_line_number = 1
        file_line_count = count_lines_in_file(input_file_path)
        open(ouput_file_path, 'w').close()

        for line in input_file:
            processed_line_text = process_line(line, current_line_number, file_line_count, field_prefix)
            with open(ouput_file_path, 'a') as output_file:
                output_file.write(processed_line_text + '\n')
            current_line_number += 1

def remove_double_quotes_from_string(text):
    return text.replace('"', '')

def remove_trailing_comma_from_string(text):
    new_text = text

    if text[-1:] == ',':
        new_text = new_text[:-1]

    return new_text

process_qlik_field_list()
