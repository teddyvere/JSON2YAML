import json
import yaml
#json to yaml converter

donuts = '/Users/teddy/Documents/GitHub/Week4/JSON2YAML/donuts.json'
emojis = '/Users/teddy/Documents/GitHub/Week4/JSON2YAML/emojis.json'

def convert_json_to_yaml(json_file_path):
    with open(json_file_path, 'r') as json_file:
        json_data = json.load(json_file)

    yaml_data = yaml.dump(json_data)
    print(f'Converted {json_file_path} to YAML')
    with open(json_file_path.replace('.json', '.yaml'), 'w') as yaml_file:
        yaml_file.write(yaml_data)

    return yaml_data

donuts_yaml = convert_json_to_yaml(donuts)
emojis_yaml = convert_json_to_yaml(emojis)

