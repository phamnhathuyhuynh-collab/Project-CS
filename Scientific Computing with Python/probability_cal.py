import copy 
import random

from unittest import main
class Hat:
    def __init__(self, **kwargs):
        self.contents = [];
        for key, value in kwargs.items():
            while int(value) > 0:
                self.contents.append(key)
                value -= 1
        for key, value in kwargs.items():
            setattr(self, key, value)
        
            
    def draw(self, ball):
        list_of_ball_drawed = []
        if ball > len(self.contents):
            
            list_of_ball_drawed = copy.deepcopy(self.contents)
            self.contents = []
            return list_of_ball_drawed, self.contents
        
        while ball > 0:
            random_ball = round(random.random() * len(self.contents)) -1
            list_of_ball_drawed_copy = copy.deepcopy(self.contents[random_ball])
            list_of_ball_drawed.append(list_of_ball_drawed_copy)
            self.contents.pop(random_ball)
            ball -= 1
        
        return list_of_ball_drawed
    


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    list_compared = []
    
            
    for color, number in expected_balls.items():
        for _ in range(number): 
            list_compared.append(color)
            
    
    count1 = 0
    for _ in range(num_experiments):
        count = 0
        hat_copy = copy.deepcopy(hat)
        num_balls_drawn_copy = copy.deepcopy(num_balls_drawn)
        temp = hat_copy.draw(num_balls_drawn_copy)
    
            
        for i in list_compared:    
            for j in temp:
                if i == j:
                    count += 1
                    temp.remove(j)
                    break
                        
        if count == len(list_compared):
            count1 += 1
    
        
    return count1/num_experiments


                    
                    
        
        #hat.draw(num_balls_drawn_copy)
            #count += 1
        #else:
         #   count1 += 1
   # return count/num_experiments
            
    
hat = Hat(black=6, red=4, green=1)

probability = experiment(hat=hat,
                  expected_balls={'black':2, 'green': 1},
                  num_balls_drawn=6,
                  num_experiments=2000)



# Run unit tests automatically
main(module='test_module', exit=False)

print(hat.draw(5))
print(probability)


#source from freeCodeCamp, i'm just a learner



