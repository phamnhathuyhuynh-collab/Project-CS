def maximizeSquareHoleArea(n, m, hBars, vBars):
    hBars.sort()
    vBars.sort()
    if len(hBars) <= 1 or len(vBars) <= 1: 
        return 4
    else: 
        i = 0 
        count_hBars = 1
        while i < len(hBars) - 1: 
            max = 1
            while i < len(hBars) - 1 and hBars[i + 1] - hBars[i] == 1: 
                max += 1
                i += 1
            if max > count_hBars: 
                count_hBars = max

            i += 1
        j = 0
        count_vBars = 1
        while j < len(vBars) - 1: 
            max = 1
            while j < len(vBars) -1 and vBars[j + 1] - vBars[j] == 1: 
                max += 1
                j += 1
            if max > count_vBars: 
                count_vBars = max
            j += 1
    return (min(count_hBars, count_vBars) + 1)**2

print(maximizeSquareHoleArea(3, 2, [3,2,4], [3, 2]))