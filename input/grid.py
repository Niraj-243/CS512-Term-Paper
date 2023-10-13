import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
from pprint import pprint
from colorama import Fore, Back, Style


class grid:
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