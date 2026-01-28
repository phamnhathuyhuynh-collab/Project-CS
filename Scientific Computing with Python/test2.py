result = ""
pers = [10,20,30]
str = ['Clothing', 'Food', 'Autot']
for percentage in range(100, -10, -10):
    
    result += (f"{percentage:3.0f}" + '|')
    count = 0
    
    for j, per in enumerate(pers):
        if percentage == per:
            if j == 0:
                result += (' ' + 'o' )
                pers[j] -= 10
            else:
                result += ('  ' + 'o' )
                pers[j] -= 10
        else:
            if j == 0:
                result += 2*' '
                count += 1
            else:
                result += 3*' '
                count += 1
        if count == len(pers):
            break
    result += '\n'

result += 4*' '+ '-' + len(pers)*2*'-' + len(pers)*'-' 
result += '\n'
min = float('inf')
max = float('-inf')
for i in str: 
    if len(i) < min:
        min  = len(i)
for i in str: 
    if len(i) > max:
        max  = len(i)
       
print(min, max) 
for i in range(min):
    result += 4 * ' '
    for j in range(len(str)):
        if j == 0:
            if str[j][i]:
                result += (' '+ str[j][i])
        else:
            if str[j][i]:
                result += ('  '+ str[j][i])
    result += '\n'

remain_max = max - min 

for i in range(remain_max):
    result += 4 * ' '
    for j in range(len(str)):
        if len(str[j]) - min > 0:
            if j == 0:
                result += (' '+ str[j][min])
            else:
                result += ('  '+ str[j][min])
                
        else:
            result += 3*' '
    min += 1
    result += '\n'
print(result)
print('     B  F  E\n     u  o  n\n     s  o  t\n     i  d  t')
print('F  E\n     o  n\n     o  t\n     d  e\n      [87 chars]   t' != '     F  E  \n     o  n  \n     o  t  \n     d  e  [113 chars] t  ')