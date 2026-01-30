from heapq import heapify, heappush, heappop, heapify_max, heappushpop_max, heappop_max, heappush_max

def fillCups(amount): 
    heapify_max(amount)
    count = 0
    while amount[0] != 0:
        num1 = heappop_max(amount)
        num2 = heappop_max(amount)
        if num1 > 0: 
            num1 -= 1
        if num2 > 0: 
            num2 -= 1
        heappush(amount, num1)
        heappush(amount, num2)
        heapify_max(amount)  
        count += 1
    return amount, count
print(fillCups(amount = [10, 1, 1]))