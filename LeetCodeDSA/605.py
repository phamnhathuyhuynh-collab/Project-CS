# can place flowers 
def canPlaceFlowers(flowerbed, n):
    # truong hop do dai = 1
    if n == 0: 
        return True
    if len(flowerbed) == 1:
        if flowerbed[0] == 1:
            return False
        else: 
            if n > 1:
                return False
            else: 
                return True

    # truong hop do dai = 2
    if len(flowerbed) == 2:
        if flowerbed[0] == 0 and flowerbed[1] == 0 and n <= 1:
            return True
        else: 
            return False
    
    # truong hop do dai > 2
    count = 0
    for i in range(len(flowerbed)):
        if flowerbed[i] == 0:
            count += 1
            if (i == len(flowerbed) - 1 and count == 2) or (i == 0 and flowerbed[0] == 0 and flowerbed[1] == 0) or (count == 2 and flowerbed[i + 1] == 0):
                n -= 1
                flowerbed[i] = 1
                count = 0
            if n == 0:
                return True
        else: 
            count = 0
            
    return False
 
            
    
    
print(canPlaceFlowers([1,0,1,1,0], 1))