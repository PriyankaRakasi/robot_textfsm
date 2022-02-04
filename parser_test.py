import custom_modules.parser as parser

text_file_path = 'test_data\cisco_show_clock.txt'
template_file_path = 'textfsm_templates\cisco_show_clock.template'

output = parser.get_data_parsed(template_file_path, text_file_path,)

print(output[0])


