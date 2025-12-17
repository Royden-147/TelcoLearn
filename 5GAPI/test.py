# import yaml, json

# url = r"C:\Users\ROYDEN\OneDrive\Desktop\New folder\TelcoLearn\Day_15\ts24549.yaml"

# with open(url) as file:
#     data = yaml.safe_load(file)

# # Extract endpoint metadata (services)
# metadata = []

# paths = data.get("paths", {})
# for path, methods in paths.items():
#     for method, details in methods.items():
#         if method.lower() in ["get", "post", "put", "delete", "patch"]:
#             metadata.append({
#                 "path": path,
#                 "method": method.upper(),
#                 "summary": details.get("summary"),
#                 "description": details.get("description"),
#                 "operationId": details.get("operationId"),
#                 "tags": details.get("tags")
#             })

# print(json.dumps(metadata, indent=2))

# with open("out_file", "w") as f:
#     json.dump(metadata, f, indent=2)
    

# print("Services written to:", "out_file")

import yaml, json, os, logging

url = r"C:\Users\ROYDEN\OneDrive\Desktop\New folder\TelcoLearn\Day_15\ts24549.yaml"

log_file = r"C:\Users\ROYDEN\OneDrive\Desktop\New folder\TelcoLearn\5GAPI\log.txt"
# Configure logging (structured logs)
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format='%(asctime)s  |  %(levelname)s  |  %(message)s'
)

logging.info("Starting metadata extraction.")
logging.info(f"Reading YAML file: {url}")

with open(url) as file:
    data = yaml.safe_load(file)

logging.info("YAML file successfully loaded.")

# Extract services (endpoint metadata)
metadata = []
paths = data.get("paths", {})

for path, methods in paths.items():
    for method, details in methods.items():
        if method.lower() in ["get", "post", "put", "delete", "patch"]:
            meta_entry = {
                "path": path,
                "method": method.upper(),
                "summary": details.get("summary"),
                "description": details.get("description"),
                "operationId": details.get("operationId"),
                "tags": details.get("tags")
            }
            metadata.append(meta_entry)
            logging.info(f"Extracted endpoint: {method.upper()} {path}")

# Save services.json in same directory
out_file = os.path.join(os.path.dirname(url), "services.json")
with open(out_file, "w") as f:
    json.dump(metadata, f, indent=2)

logging.info(f"Metadata written to: {out_file}")
logging.info("Extraction completed successfully.")

print("Services written to:", out_file)
print("Logs saved to:", log_file)
