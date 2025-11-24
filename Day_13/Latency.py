def avg(x):
    total = sum(x)
    avg = total / len(x) 
    return avg

def MinMaxAvg(x):
    minimum = min(x)
    maximum = max(x)
    average = avg(x)
    dict = {'minzx': minimum, 'maxzx': maximum, 'avg23': average}
    return dict 

data = [10, 20, 30, 40, 50]
print(MinMaxAvg(data))
