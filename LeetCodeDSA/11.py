def maxArea(height):
    length = len(height)
    max = 0
    j = length - 1
    i = 0
    while i < j:
        # print(i, j)
        if (j - i)*(min(height[i], height[j])) > max:
           max = (j - i)*(min(height[i], height[j]))
        if height[i] < height[j]:
            i += 1
        else:
            j -= 1
    return max
                

    
print(maxArea([1,8,6,2,5,4,8,3,7]))