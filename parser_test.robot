*** Settings ****
Documentation     How to use a custom Python library.
Library           custom_modules/parser.py


*** Variables ***
${show_clock_output}=    test_data\\cisco_show_clock.txt
${template}=             textfsm_templates\\cisco_show_clock.template



*** Test Cases ***

Getting Structured data from device output 
    ${structured_output}=  get_data_parsed  ${template}  ${show_clock_output}  
    
    Log to console   ${structured_output}[1]