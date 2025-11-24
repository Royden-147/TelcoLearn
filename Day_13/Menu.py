import os

def ip_reach_test():
    ip = input("Enter an IP address to test reachability: ")
    command = f"ping -n 1 {ip}" if os.name == 'nt' else f"ping -c 1 {ip}"
    response = os.system(command)
    if response == 0:
        print(f"{ip} is reachable")
    else:
        print(f"{ip} is not reachable")

def avg(x):
    total = sum(x)
    avg = total / len(x) 
    return avg

def summary(x):
    minimum = min(x)
    maximum = max(x)
    average = avg(x)
    dict = {'min': minimum, 'max': maximum, 'avg': average}
    return dict

while True:
    choice = input("Choose an option:\n1. Test IP Reachability\n2. Calculate Min, Max, Avg of Numbers\n3. Exit\n>> ")
    if choice == '1':
        ip_reach_test()
    elif choice == '2':
        num = input("How many numbers will you enter? ")
        numList = list(map(float, num.split(",")))
        print(summary(numList))
    elif choice == '3':
        break
    else:
        print("Invalid choice. Please try again.")