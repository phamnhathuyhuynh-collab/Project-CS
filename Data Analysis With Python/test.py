import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 


a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6]])
print(np.concatenate((a, b), axis=0))