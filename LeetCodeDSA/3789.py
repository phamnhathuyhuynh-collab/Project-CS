def minimumCost(cost1, cost2, costBoth, need1, need2):
    if min(cost1, cost2, costBoth) == costBoth: 
        return costBoth*max(need1, need2)
    else:
        if need1 > need2: 
            if need2*(cost1+cost2) > costBoth*need2 or need2 == 0:
                if costBoth*need1 < cost1*need1:
                    return costBoth*need1
                return need2*costBoth + (need1 - need2)*cost1
            else:
                return need1*cost1 + need2*cost2
        else:
            if need1*(cost1+cost2) > costBoth*need1 or need1 == 0:
                if costBoth*need2 < cost2*need2:
                    return costBoth*need2
                return need1*costBoth + (need2 - need1)*cost2
            else:
                return need1*cost1 + need2*cost2

def minimumCostHint(cost1, cost2, costBoth, need1, need2):
    result = min(costBoth, cost1+cost2)*min(need1, need2)
    if need1 > need2:
        result += min(costBoth, cost1)*(need1-need2)
    else:
        result += min(costBoth, cost2)*(need2-need1)
    return result
    
            

        
        
print(minimumCostHint(cost1 = 85, cost2 = 14, costBoth =31, need1 = 49, need2 = 0))
    
print(minimumCost(cost1 = 85, cost2 = 14, costBoth =31, need1 = 49, need2 = 0))