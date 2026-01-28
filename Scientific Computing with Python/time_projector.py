def add_time(start, duration, days=''):
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thusrday', 'Friday', 'Saturday', 'Sunday']
    start_split = start.split(' ')
    start_split[0] = start_split[0].split(':')
    duration_split = duration.split(':')

    print(start_split, duration_split)
    
    result1 = int(start_split[0][0]) + int(duration_split[0])
    result2 = int(start_split[0][1]) + int(duration_split[1])

    while result2 >= 60:
        result2 -= 60
        result1 += 1 
        
    
    if start_split[1] == 'AM':
        days_later = (int(result1)) // 24
    else:
        days_later = (int(result1) + 12) // 24
        
    if  (int(result1) - int(duration_split[0])) + (int(duration_split[0]) % 12) >= 12:
        if start_split[1] == 'AM':
            start_split[1] = 'PM'
        else:
            start_split[1] = 'AM'
    day_of_week = ''
    if not days == '': 
        for day in days_of_week:
            if day.lower() == days.lower():
                day_of_week = days_of_week[(days_of_week.index(day)+days_later)%7]
    
    round_hour = -1
    if result1 >= 12:
        if result1 % 12 == 0:
            round_hour = 12
        else:
            round_hour = result1 % 12
    
    while round_hour > 12:
        round_hour = int(round_hour) - 12
    

                
    if result2 < 10:
        result2 = "0" + str(result2)
    
    if days_later == 0:
        if round_hour < 0:
            if days:
                final_result = f'{result1}:{result2} {start_split[1]}, {day_of_week}'
            else:
                final_result = f'{result1}:{result2} {start_split[1]}'
        else:
            if days:
                final_result = f'{round_hour}:{result2} {start_split[1]}, {day_of_week}'
            else:
                final_result = f'{round_hour}:{result2} {start_split[1]}'     
    elif days_later == 1:
        if round_hour < 0:
            if days:
                final_result = f'{result1}:{result2} {start_split[1]}, {day_of_week} (next day)'
            else:
                final_result = f'{result1}:{result2} {start_split[1]} (next day)'
        else:
            if days:
                final_result = f'{round_hour}:{result2} {start_split[1]}, {day_of_week} (next day)'
            else:
                final_result = f'{round_hour}:{result2} {start_split[1]} (next day)'
    elif days_later >=2 :
        if round_hour < 0:
            if days:
                final_result = f'{result1}:{result2} {start_split[1]}, {day_of_week} ({days_later} days later)'
            else:
                final_result = f'{result1}:{result2} {start_split[1]} ({days_later} days later)'
        else:
            if days:
                final_result = f'{round_hour}:{result2} {start_split[1]}, {day_of_week} ({days_later} days later)'
            else:
                final_result = f'{round_hour}:{result2} {start_split[1]} ({days_later} days later)'
       
    
    return final_result, result1
print(add_time('8:16 PM', '466:02'))
