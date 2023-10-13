import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
from pprint import pprint
from colorama import Fore, Back, Style

class env:
    def __init__(self,rectangle):
        self.length,self.height = np.shape(rectangle)
        self.rectangle = rectangle
    
    def print_env(self):
        for i in self.rectangle:
            for j in i:
                if j==1:
                    print(Fore.RED + 'X '+ Style.RESET_ALL,end="")
                else: 
                    print(Fore.BLUE + '. '+ Style.RESET_ALL,end="")
            print("")

def random_state_generator(length,height,num):
    arr = np.zeros((height,length))
    x_pts = random.sample(list(np.arange(2,length-1,2)),num)
    y_pts = [[0,0] for i in x_pts]
    for i,p in enumerate(x_pts):
        yp = random.sample(range(2,height-1),2)
        yp.sort()
        y_pts[i] = yp
    for i,xp in enumerate(x_pts):
        for j in range(y_pts[i][0],y_pts[i][1]+1):
            arr[j][xp] = 1
            
    return arr

p = pd.DataFrame([1,2])
rect = random_state_generator(30,30,5)
env1 = env(rect)
env1.print_env()