# CSS file beautifier operation

# Add some parent selector for all the css rules in the css file
import re

try:
    input_file = open('input.css', 'r')
    output_file = open('output.css', 'w')
    print('>>> Input file is accessible')
    if input_file.mode == 'r':
        print('----------------------------')
        current_line_number = 0
        flag = False
        for line_data in input_file:
            current_line_number += 1
            if output_file.mode == 'w':
                if flag:
                    end_tag_match_data = re.search('(^\s*}$)|(^}$)', line_data)
                    output_file.write(line_data)
                    if end_tag_match_data:
                        flag = False
                else:
                    prefix_text = '.formio-form '
                    match_data = re.search('(^(?!@).*{$)|(.*,$)', line_data)
                    if match_data:
                        new_write_line = prefix_text + line_data
                        output_file.write(new_write_line)
                    else:
                        fontface_match_data = re.search('^(@font-face).*$', line_data)
                        output_file.write(line_data)
                        if fontface_match_data:
                            flag = True
        print('----------------------------')
    input_file.close()
    output_file.close()
    print('File operation successful !!!')
except IOError:
    print('>>> Input file is not accessible')
