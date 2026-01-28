def removeDigit(number, digit):
    len = len(number)
    max = ""
    for i in range(len): 
        if number[i] == digit:
            if i == 0:
                temp = number[1:]
                if temp > max :
                    max = temp 
            elif i == len -1:
                temp = number[:-1]
                if temp > max:
                    max = temp 
            else:
                temp = number[0:i] + number[i+ 1:]
                if temp > max:
                    max = temp 
    return max

print(removeDigit("551","5"))