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
        self.meta_rect = None
    
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

    def plot_grid(self):
        x,y = np.meshgrid(range(self.height),range(self.length))
        col,char = None,None
        for i in range(self.rectangle.shape[0]):
            for j in range(self.rectangle.shape[1]):
                val = self.rectangle[i][j]
                if val==0: 
                    col = 'yellow'
                    char = '.'
                if val==1: 
                    col = 'black'
                    char = '.'
                if val==2: 
                    col = 'blue'
                    char = '.'
                if val==3: 
                    col = 'blue'
                    char = '.'
                if val==4: 
                    col = 'red'
                    char = '.'
                plt.plot(j,self.rectangle.shape[0]-i-1,char,color=col)
        plt.show()
    
    def make_meta_grid(self,k):
        arr = self.rectangle
        length, height = arr.shape
        m_length = int(length/k)
        m_height = int(height/k)
        meta_arr = np.zeros((m_length,m_height))
        for i in range(m_length):
            for j in range(m_height):
                if 1 in arr[k*i:k*(i+1),k*j:k*(j+1)]:
                    meta_arr[i][j] = 1
        self.meta_rect = meta_arr

    def plot_meta_grid(self):
        h,l = self.meta_rect.shape
        x,y = np.meshgrid(range(h),range(l))
        col,char = None,None
        for i in range(h):
            for j in range(l):
                val = self.meta_rect[i][j]
                if val==0: 
                    col = 'yellow'
                    char = '.'
                if val==1: 
                    col = 'black'
                    char = '.'
                if val==2: 
                    col = 'blue'
                    char = '.'
                if val==3: 
                    col = 'blue'
                    char = '.'
                if val==4: 
                    col = 'red'
                    char = '.'
                plt.plot(j,h-i-1,char,color=col)
        plt.show()