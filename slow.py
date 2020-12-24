def slowestKey(keyTimes):
    keyTimes = [[chr(k[0] + 97), k[1]] for k in keyTimes]                    
    bigger = None
    bigger_time = None    
    for i in range(len(keyTimes)-1):
        if i == 0:
            start = 0
        else:
            start = keyTimes[i-1][1]
        end = keyTimes[i][1]
        char = keyTimes[i][0]
        interval = end - start
        if not bigger_time or interval > bigger_time:
            bigger_time = interval
            bigger = char
    return bigger
print(slowestKey([[0, 2], [1, 5], [0, 9], [2, 15]]))

print(slowestKey([[0, 2], [1, 5], [0, 9], [2, 15]]))
