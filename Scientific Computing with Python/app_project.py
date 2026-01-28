class Category:
    def __init__(self, budget_category):
        self.ledger = []
        self.budget_category = budget_category
        
    def __repr__(self):
        result = ""
        title = ""
        self.ledger[0]['description'] = self.ledger[0]['description']
        
        for i in range(1, 31):
            if i <= ((30 - len(self.budget_category)) //2) or i > ((30 - len(self.budget_category)) //2) + len(self.budget_category) :
                title += '*'
            else:
                title += self.budget_category[i - ((30 - len(self.budget_category)) //2) - 1] 

        result += title 
        result += '\n'
        
        for sub_ledger in (self.ledger):
            if len(sub_ledger['description']) + 7 >= 30:
                result += (sub_ledger['description'][0: 23] + ' ' + f"{sub_ledger['amount']:4.2f}") 
                result += '\n'
            else:
                result += (sub_ledger['description'] + (30 - len(sub_ledger['description']) - len(f"{sub_ledger['amount']:4.2f}"))*' ' + f"{sub_ledger['amount']:4.2f}")
                result += '\n'
        
        result += f"Total: {float(self.get_balance()):4.2f}"
        return result     
        
    def deposit(self, amount, description = ""):
        self.ledger.append({'amount': amount, 'description' : description})
    
    def withdraw(self, amount, description = ""):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount,'description' : description})
            return True
        return False 

    def get_balance(self):
        current_balance = 0
        for amount in self.ledger:
            current_balance += float(amount['amount'])
        return current_balance

    def transfer(self, amount, category_object):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {category_object.budget_category}')
            category_object.deposit(amount, f'Transfer from {self.budget_category}')
            
            return True
        return False
    
    def check_funds(self, amount):
        if float(amount) > float(self.get_balance()):
            return False
        return True
    
food = Category('Food')
food.deposit(900, "deposit")
entertainment = Category('Entertainment')
entertainment.deposit(900, "deposit")
business = Category('Business')
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)

print(food)
print(entertainment)
print(business)


def create_spend_chart(categories):
    final_result = ""
    total = 0
    for withdrawal in categories:
        for i in range(len(withdrawal.ledger)):
            if float(withdrawal.ledger[i]['amount']) < 0:
                total += float(withdrawal.ledger[i]['amount'])
    total = abs(total)

    list_percentages = []
    for withdrawal in categories:
        total_widthdrawal = 0
        for i in range(len(withdrawal.ledger)):
            if float(withdrawal.ledger[i]['amount']) < 0:
                total_widthdrawal += float(withdrawal.ledger[i]['amount'])
        percentage_temporary = (abs(float(total_widthdrawal))*10//float(total)) *10
        list_percentages.append(percentage_temporary)

    for percentage in range(100, -10, -10):
        
        final_result += (f"{percentage:3.0f}" + '|')
        count = 0
        
        for j, per in enumerate(list_percentages):
            if percentage == per:
                if j == 0:
                    final_result += (' ' + 'o' )
                    list_percentages[j] -= 10
                else:
                    final_result += ('  ' + 'o' )
                    list_percentages[j] -= 10
            else:
                if j == 0:
                    final_result += 2*' '
                    count += 1
                else:
                    final_result += 3*' '
                    count +=1
            if count == len(list_percentages):
                break
        final_result += 2*' '
        final_result += '\n'

    final_result += 4*' ' + len(list_percentages)*2*'-' + len(list_percentages)*'-' + '-'
    final_result += '\n'
    min = float('inf')
    max = float('-inf')
    for i in categories: 
        if len(i.budget_category) < min:
            min  = len(i.budget_category)
    for i in categories: 
        if len(i.budget_category) > max:
            max  = len(i.budget_category)
        
 
    for i in range(min):
        final_result += 4 * ' '
        for j in categories:
            if j == categories[0]:
                if j.budget_category[i]:
                    final_result += (' '+ j.budget_category[i])
            else:
                if j.budget_category[i]:
                    final_result += ('  '+ j.budget_category[i])      
        final_result += (2*' ' + '\n')

    remain_max = max - min 

    for i in range(remain_max):
        final_result += 4 * ' '
        for j in categories:
            if len(j.budget_category) - min > 0:
                if j == categories[0]:
                    if j.budget_category[i]:
                        final_result += (' '+ j.budget_category[min])
                else:
                    if j.budget_category[i]:
                        final_result += ('  '+ j.budget_category[min])
            else:
                if j == categories[0]:
                    final_result += 2*' '
                else:
                    final_result += 3*' '
        min += 1
        if i != remain_max - 1:
            final_result += (2*' ' + '\n')
        else:
            final_result += 2*' '
    final_result = 'Percentage spent by category' + '\n' + final_result 
    return final_result
            
print(create_spend_chart([business, food, entertainment]))
