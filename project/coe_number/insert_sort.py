def insertion_sort(data):
        
    limit_data(data)
    
    for i in range(0, len(data)):
        for j in range(0, len(data)):
            if data[j] > data[i]:
                temp = data[j]
                data[j] = data[i]
                data[i] = temp
    return data

def limit_data(num):
    
    for i in range(0, len(num)):
        if num[i] >= pow(10,3):
            num[i] = pow(10,3)
        elif num[i] <= pow(-10,3):
            num[i] = pow(-10,3)
    return num
