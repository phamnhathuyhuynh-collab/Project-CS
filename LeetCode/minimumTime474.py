def minimumTime(d, r):
    rem1, rem2 = d[0], d[1]
    r1, r2 = r[0], r[1]
    
    t = 0
    while rem1 > 0 or rem2 > 0:
        t += 1
        can1 = (t % r1 != 0) and rem1 > 0
        can2 = (t % r2 != 0) and rem2 > 0
        
        if can1 and can2: 
            if rem1 >= rem2:
                rem1 -= 1
            else: 
                rem2 -= 1 
        elif can1:
            rem1 -= 1
        elif can2:
            rem2 -= 1
    return t
d1 = [3, 1]
#[1,3,5,7][2,4,6,8]
#[1,2,4,5,7,8, 10, 11][3,6,9,12]  
#[2,1,1,1,2]  
#3: 1,3,5 - 2,4 
#1: 2 - 3
r1 = [2 ,3]

d2 = [1, 3]
#[1,3,5,7][2,4,6,8]
#[1,3,5,7][2,4,6,8]
#[2,2,2,2]
#1: 3 - 4
#3: 1, 5, 7 - 2, 4, 6
r2 = [2, 2]

d3 = [2, 1]
#[1,2,4,5,7,8][3,6,9]
#[1,2,3,5,6,7,9,10,11][4,8,12]
#[2,2,1,1,2]
#1: 1, 2 - 3
#1: 3 - 4
r3 = [3, 4]

d4 = [1, 1]
#1,3 - 2, 4, 6
#1,2,3 - 4, 8
r4 = [2, 4]

d5 = [1, 1]
r5 = [3, 2]
print(minimumTime(d1, r1))
print(minimumTime(d2, r2))
print(minimumTime(d3, r3))
print(minimumTime(d4, r4))
print(minimumTime(d5, r5))

    