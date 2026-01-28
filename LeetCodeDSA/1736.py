def maximumTime(time):
    arr = [" "]*5
    arr[2] == ":"
    for i in range(5): 
        arr[i] = time[i]
        if time[i] == '?':
            if i == 0:
                if time[i + 1] == "0" or time[i + 1] == "1" or time[i + 1] == "2" or time[i + 1] == "3": 
                    arr[i] = time[i].replace("?", "2")
                else: 
                    arr[i] = time[i].replace("?", "1")
            if i == 1: 
                if time[i - 1] == '1' or time[i - 1] == '0':
                    arr[i] = time[i].replace("?", "9")
                else:
                    arr[i] = time[i].replace("?", "3")
            if i == 3:
                arr[i] = time[i].replace("?", "5")
            if i == 4:
                arr[i] = time[i].replace("?", "9")
        print(arr)
    return "".join(arr)
print(maximumTime(time = "?0:15"))