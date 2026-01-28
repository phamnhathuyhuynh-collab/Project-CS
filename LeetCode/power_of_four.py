import math
def power_of_four(n):
    if (n % math.sqrt(n) == 0) and (int(math.sqrt(n))&int((math.sqrt(n)-1)) == 0):
        return True  
    return False

def power_four(n):
    return (not (n&(n-1))) and n%3 == 1
        
print(power_four(8))
