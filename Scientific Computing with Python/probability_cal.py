import copy
import random

class Hat:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
    
            

hat1 = Hat(yellow=3, blue=2, green=6)

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    pass