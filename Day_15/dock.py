import yaml
with open('dock.yaml') as file:
    data = yaml.safe_load(file)

service = data["services"]["oai-amf"]
list1 = service.get("environment",[])
dict1 = {}
for i in list1:
    if "=" in i:
        kay, value = i.split("=", 1)
        dict1[kay] = value
print("MCC =",dict1.get("MCC"))
print("MNC =",dict1.get("MNC"))



services = data.get("services",{})
# print(services)

for service_name, service_data in services.items():
    depends = service_data.get("depends_on")
    dep_list = []
    if not depends:
        print(f"{service_name} : None")
    else:
        if isinstance(depends, list):
            dep_list = depends
        else:
            dep_list = ["NA"]

    depends_str = ", ".join(dep_list)

    ipv4 = "None"
    networks = service_data.get("networks")
    if networks:
        for net_name,net_data in networks.items():
            ipv4 = net_data.get("ipv4_address","None")
            break

    print(f"{service_name} --> depends on: {depends_str} --> IP Address: {ipv4}")    
    


services = data.get("services",{})
# print(services)

for service_name, service_data in services.items():
    ports = []

    env = service_data.get("environment",[])
    for item in env:
        if "=" in item:
            key , val = item.split("=",1)
            if val.isdigit():
                if key not in ports:
                    ports.append(key)
    ports_str = ", ".join(ports) if ports else "None"  
    print(f"{service_name} --> Ports: {ports_str}")              
