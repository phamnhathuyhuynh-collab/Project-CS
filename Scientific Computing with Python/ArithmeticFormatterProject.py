def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return ('Error: Too many problems.')

    for problem in problems:
        for char in problem:
            if char == '*' or char == '/':
                return ("Error: Operator must be '+' or '-'.")

    for problem in problems:
        for char in problem:
            if char.isalpha():
                return 'Error: Numbers must only contain digits.'

    for problem in problems:
        digit = 0
        for char in problem:
            if char == '+' or char == '-' or char == ' ':
                digit = 0
            else:
                digit += 1
            if(digit == 5):
                return 'Error: Numbers cannot be more than four digits.'

    for problem in problems:
        digit = 0
        for char in problem:
            if char == '+' or char == '-' or char == ' ':
                digit = 0
            else:
                digit += 1
            if(digit == 5):
                return 'Error: Numbers cannot be more than four digits.'

    first_digits = []
    last_digits = []
    for problem in problems:
        all_digits_in_one_operator = ""
        for digit in problem:
            if digit.isdigit():
                all_digits_in_one_operator += digit
            else :
                break
        first_digits.append(all_digits_in_one_operator)
        
    count = -1
    result_final = []
    for problem in problems:
        problem_reversed = problem[::-1]
        count += 1
        all_digits_in_one_operator = ""
        all_digits_in_one_operator_reversed = ""
        result_final_int = "" 
        for digit in problem_reversed:
            space = 0
            space_char = ""
            if digit.isdigit() and not(digit == '+' or digit == '-'):
                all_digits_in_one_operator_reversed += digit
                all_digits_in_one_operator = all_digits_in_one_operator_reversed[::-1]
                
                if(len(first_digits[count]) > len(all_digits_in_one_operator)):
                    space =  len(first_digits[count]) - len(all_digits_in_one_operator)
                    for _ in range(space):
                        space_char += ' '
                    all_digits_in_one_operator = space_char + all_digits_in_one_operator
                elif(len(first_digits[count]) < len(all_digits_in_one_operator)):
                    space =  len(all_digits_in_one_operator) - len(first_digits[count])                    
                    for _ in range(space):
                        space_char += ' '
                    first_digits[count] = space_char + first_digits[count]
            elif(digit == '+'):
                result_final_int += f'{int(first_digits[count]) + int(all_digits_in_one_operator)}'
                result_final.append(result_final_int)
                all_digits_in_one_operator = '+'+ ' ' + all_digits_in_one_operator
                break
            elif(digit == '-'):
                result_final_int += f'{int(first_digits[count]) - int(all_digits_in_one_operator)}'
                result_final.append(result_final_int)
                all_digits_in_one_operator = '-'+ ' ' + all_digits_in_one_operator
                break
        last_digits.append(all_digits_in_one_operator)   
    result_first_digits = ""
    result_last_digits = ""
    for i in range(len(problems)):
        if not i == 0:
            result_first_digits += '      ' + first_digits[i]
        else:
            result_first_digits += '  ' + first_digits[i]
    for i in range(len(problems)):
        if not i == 0:
            result_last_digits += '    ' + last_digits[i]
        else:
            result_last_digits += last_digits[i]
        
    divide_char = ""    
    space_result = ""
    
    for i in range(len(problems)):
        more_space = ""
        for _ in range(max(len(last_digits[i]), len(first_digits[i]))):
            divide_char += '-'
        if not (i == len(problems) - 1):
            divide_char += '    '
        for _ in range(len(last_digits[i]) - len(result_final[i])):
            more_space += ' '
        if not i == 0:
            space_result += '    '+more_space + result_final[i]
        else:
            space_result += more_space + result_final[i]
            
    result1  = result_first_digits + "\n" + result_last_digits + "\n" + divide_char+ "\n" + space_result 
    result2 = result_first_digits + "\n" + result_last_digits + "\n" + divide_char
    return result1 if show_answers == True else result2
    
    
actual = arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"])
expected = "    3      3801      45      123\n+ 855    -    2    + 43    +  49\n-----    ------    ----    -----"

print(expected == actual)
