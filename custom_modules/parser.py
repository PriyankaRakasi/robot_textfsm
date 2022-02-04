import textfsm



def get_data_parsed(template_path, data_file_path):

    # Loading text from text_file
    with open(data_file_path,'r') as data:
        unstructured_data = data.read()

    print(unstructured_data)
    # Loading template from template path
    with open(template_path, 'r') as template_file:
        template = textfsm.TextFSM(template_file)
        
    template_match_data = template.ParseText(unstructured_data)

    # print(template_match_data)

    return template_match_data[0]