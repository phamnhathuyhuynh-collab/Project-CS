def maxProfit(prices):
    if len(prices) == 1:
        return 0
    total = 0
    profit = 0

    i = 0
    j = 1
    while i < len(prices) and j < len(prices): 
        while j < len(prices) and prices[j] - prices[i] > profit:
            profit = (prices[j] - prices[i] )
            j += 1
        total += profit
        i = j 
        j += 1
        profit = 0
    return total

def maxProfit2(prices): 
    profit = 0 
    i = 0 
    j = 1
    while i < len(prices) and j < len(prices): 
        if prices[j] - prices[i] > 0: 
            profit += prices[j] - prices[i]
        i += 1
        j += 1

    return profit

print(maxProfit(prices = [7,1,5,3,6,4]))
print(maxProfit2(prices = [7,1,5,3,6,4]))