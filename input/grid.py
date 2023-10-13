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
    
    def print_grid(self):
        for i in self.rectangle:
            for j in i:
                if j==1:
                    print(Fore.BLACK + 'X '+ Style.RESET_ALL,end="")
                elif j==0: 
                    print(Fore.YELLOW + '. '+ Style.RESET_ALL,end="")
                elif j==2:
                    print(Fore.RED + 'S '+ Style.RESET_ALL,end="")
                elif j==3:
                    print(Fore.RED + 'D '+ Style.RESET_ALL,end="")
            print("")