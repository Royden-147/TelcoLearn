import subprocess
ipList = ["8.8.8.8","192.168.1.10","127.0.0.1"]

for ip in ipList:
    response = subprocess.run(["ping", "-n", "1", ip], capture_output=True, text=True)
    if "Reply from" in response.stdout:
        print(f"{ip} is reachable")
    else:
        print(f"{ip} is not reachable")