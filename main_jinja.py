import commentjson
import json
from jinja2 import Environment, Template, FileSystemLoader
import sys
from json import dumps

def generate_config():
    with open("interface.json", "r") as f1:
        template_list = json.load(f1)
        #print(template_lst)
        template_dict = {}
    
    for i in template_list:
        template_dict.update(i)  ## convert list of dict into dict
    #print(template_list)
    print("converted :",template_dict)


    # Creating Jinja2 Environment
    my_template = Environment(loader=FileSystemLoader(searchpath="."), trim_blocks=True) #define path

    template = my_template.get_template("interface_jinja.j2")

    # Rendering Variables to Jinja
    config_file = template.render(template_dict)
    with open("XR_interce.txt", "w") as f:
        f.write(config_file)

output = generate_config()
# print(template_dict)