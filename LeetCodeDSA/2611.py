def miceAndCheese(reward1, reward2, k):
    length = len(reward1)
    if k == length: 
        return sum(reward1)
    sum_mouse2 = sum(reward2)
    gain = [0] * length
    for i in range(length):
        gain[i] = reward1[i] - reward2[i]
    gain = sorted(gain, reverse=True)
    for i in range(k):
        sum_mouse2 += gain[i]
    return sum_mouse2, gain
    
    
        
print(miceAndCheese(reward1 = [1,1,3,4], reward2 = [4,4,1,1], k = 2))