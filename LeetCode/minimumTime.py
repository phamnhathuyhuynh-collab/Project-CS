def minimumTime(d, r):
    time_charge_d1 = [r[0]]
    time_charge_d2 = [r[1]]
    time_delivre_total = d[1] + d[0]
    hour_delivre_d1 = []
    hour_delivre_d2 = []
    for i in range(1, time_delivre_total):
        time_charge_d1.append(time_charge_d1[i -1] + r[0])
    for i in range(1, time_delivre_total):
        time_charge_d2.append(time_charge_d2[i -1] + r[1])

    for i in range(time_charge_d1[-1] + 1):
        hour_delivre_d1.append(1)
    
    for i in time_charge_d1: 
        hour_delivre_d1[i] = 0
    
    for i in range(time_charge_d2[-1] + 1):
        hour_delivre_d2.append(1)
    
    for i in time_charge_d2:
        hour_delivre_d2[i] = 0
    
    # return hour_delivre_d1, hour_delivre_d2
    idx = 1
    sum =0 
    # if hour_delivre_d1 == hour_delivre_d2:
    #     return time_charge_d1[-1] -1;
    if len(hour_delivre_d1) < len(hour_delivre_d2):
        for i in range(len(hour_delivre_d2) - len(hour_delivre_d1)):
            hour_delivre_d1.append(0)
    else:
        for i in range(len(hour_delivre_d1) - len(hour_delivre_d2)):
            hour_delivre_d2.append(0)
  
    reserved = []
    if time_charge_d1[-1] > time_charge_d2[-1]:
        for i in range(time_charge_d1[-1] +1):
            reserved.append(0)
    else: 
        for i in range(time_charge_d2[-1] +1):
            reserved.append(0)
    if d[0] > d[1]:
        for i in range(1, time_charge_d1[-1] + 1):

            if hour_delivre_d1[i] == 1:
                reserved[i] = 1
        count = d[1]
        for i in range(1, time_charge_d1[-1] + 1):
            if hour_delivre_d2[i] == 1 and reserved[i] == 0:
                reserved[i] = 1
                count -= 1
            if count == 0:
                break
        
       
    else:
        for i in range(1, time_charge_d2[-1] + 1):
            
            if hour_delivre_d2[i] == 1:
                reserved[i] = 1
        count = d[0]
        for i in range(1, time_charge_d2[-1] + 1):
            if hour_delivre_d1[i] == 1 and reserved[i] == 0:
                reserved[i] = 1
                count -= 1
            if count ==0: 
                break
    while sum < time_delivre_total:
            if reserved[idx] == 1:
                sum += 1
            idx += 1
    return reserved, idx - 1
    
    
    
    
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
r5 = [3, 3]

d6 =[906691060,413654000]
r6=[24838,29173]

print(minimumTime(d4, r4))