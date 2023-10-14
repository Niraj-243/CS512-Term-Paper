import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
from pprint import pprint
from colorama import Fore, Back, Style
from copy import deepcopy
from bresenham import bresenham


class grid:
    def __init__(self,rectangle):
        self.length,self.height = np.shape(rectangle)
        self.rectangle = rectangle
    
    def print_grid(self):
        count = 0
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
                elif j==4:
                    print(Fore.BLACK + '* ' + Style.RESET_ALL,end="")
            print("")

    def add_graph(self, graph):
        arr = self.rectangle
        total_paths = []
        path_dic = {}
        for v in graph.keys():
            for u in graph[v]:
                #path = bres(v[1],v[0],u[1],u[0])
                path = list(bresenham(v[0],v[1],u[0],u[1]))
                total_paths += path
                path_dic[(v,u)] = path
        #print(path_dic)
        for vertex in total_paths:
            if arr[vertex[0],vertex[1]] == 0:
                arr[vertex[0],vertex[1]] = 4
        self.rectangle = arr