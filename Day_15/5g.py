import yaml, json

with open("5gy.yaml") as file:
    data = yaml.safe_load(file)

json_data = json.dumps(data, indent=2)
print(data)