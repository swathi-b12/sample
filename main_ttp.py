from ttp import ttp


with open('interface_ttp.txt', 'r') as file:
    # Read the entire contents of the file into a string
    template = file.read()

with open('interface.configs', 'r') as file1:
    # Read the entire contents of the file into a string
    configs = file1.read()

#parsing the config using ttp
parser = ttp(data=configs, template=template)
parser.parse()

#outputting the results in a separate text file 
result = parser.result(format='json')[0]
with open("interface.json", 'w') as file:
    for data in result:
        file.write(data)


#show results in terminal
# print((results))
# print(type(results))
