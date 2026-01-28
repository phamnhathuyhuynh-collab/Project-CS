from collections import Counter, defaultdict
def lemonadeChange(bills):
    cnt = defaultdict()
    cnt[5] = 0 
    cnt[10] = 0
    cnt[20] = 0
    for i in bills:
        if i == 5: 
            cnt[5] += 1
        else: 
            if i == 10: 
                cnt[5] -= 1
                cnt[10] += 1
                if cnt[5] < 0: 
                    return False
            if i == 20: 
                if cnt[10] > 0 and cnt[5] > 0: 
                    cnt[10] -=1
                    cnt[5] -= 1
                else: 
                    cnt[5] -= 3
                    if cnt[5] < 0 : 
                        return False
    return True
    
    
print(lemonadeChange(bills = [5,5,10,10,20]))