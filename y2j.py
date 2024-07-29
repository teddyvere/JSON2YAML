import json
import yaml

#yaml to json converter

verify = '/Users/teddy/Documents/GitHub/Week4/JSON2YAML/verify.yaml'
xmas = '/Users/teddy/Documents/GitHub/Week4/JSON2YAML/xmas.yaml'

def convert_yaml_to_json(yaml_file_path):
    with open(yaml_file_path, 'r') as yaml_file:
        yaml_data = yaml.safe_load(yaml_file)

    json_data = json.dumps(yaml_data)
    print(f'Converted {yaml_file_path} to JSON')
    with open(yaml_file_path.replace('.yaml', '.json'), 'w') as json_file:
        json_file.write(json_data)

    return json_data

verify_json = convert_yaml_to_json(verify)
xmas_json = convert_yaml_to_json(xmas)
