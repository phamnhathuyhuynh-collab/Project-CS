from typing import List
from collections import defaultdict, Counter
def maxCapacity(costs, capacity, budget):
    arr  = [] 
    longueur = len(costs)
    for i in range(longueur):
        if costs[i] < budget:
            arr.append(capacity[i])
    for i in range(longueur - 1): 
        for j in range(i + 1, longueur, 1):
            if costs[i] + costs[j] < budget: 
                arr.append(capacity[i] + capacity[j])
    return max(arr) if len(arr) != 0 else 0
     
print(maxCapacity(costs = [2,2,2], capacity = [3,5,4], budget = 5))