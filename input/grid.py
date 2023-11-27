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
    
    def print_grid(self,type="rect"):
        count = 0
        rec = self.rectangle
        if type=="meta":
            rec = self.meta_rect
        for i in rec:
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

    def add_graph(self, graph,type = "rect"):

        if(type == "meta"):
            arr = self.meta_rect
        else:
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
        if(type == "meta"):
            self.meta_rect = arr
        else:
            self.rectangle = arr

    def add_opt_path(self, graph,type = "rect"):

        if(type == "meta"):
            arr = self.meta_rect.copy()
        else:
            arr = self.rectangle.copy()

        for u in range(arr.shape[0]):
            for v in range(arr[u].shape[0]):
                if arr[u][v]==4:
                    arr[u][v] = 0

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
        if(type == "meta"):
            self.meta_opt_rect = arr
        else:
            self.opt_rectangle = arr

    def print_opt_path(self,type="rect"):
        count = 0
        rec = self.opt_rectangle
        if type=="meta":
            rec = self.meta_opt_rect
        for i in rec:
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
    
    def plot_opt_path(self,type="rect"):
        x,y = self.opt_rectangle.shape
        if type == "meta":
            x,y = self.meta_opt_rect.shape
        col,char = None,None
        for i in range(x):
            for j in range(y):
                val = self.opt_rectangle[i][j]
                if type=="meta":
                    val = self.meta_opt_rect[i][j]
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
                ii = self.rectangle.shape[0]-i-1
                if type=="meta":
                    ii = self.meta_rect.shape[0]-i-1
                plt.plot(j,ii,char,color=col)
        plt.show()

    def plot_grid(self,type="rect"):
        x,y = self.rectangle.shape
        if type == "meta":
            x,y = self.meta_rect.shape
        col,char = None,None
        for i in range(x):
            for j in range(y):
                val = self.rectangle[i][j]
                if type=="meta":
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
                ii = self.rectangle.shape[0]-i-1
                if type=="meta":
                    ii = self.meta_rect.shape[0]-i-1
                plt.plot(j,ii,char,color=col)
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
        
        meta_arr[m_length-1][0] = 2
        meta_arr[0][m_height-1] = 3
        self.meta_rect = meta_arr


    def plot_meta_path(self,graph,k):
        
        count = 0
        rec = self.rectangle.copy()
        for x in range(rec.shape[0]):
            for y in range(rec[x].shape[0]):
                if rec[x][y] == 4:
                    rec[x][y] = 0

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
            if rec[vertex[0],vertex[1]] == 0:
                rec[vertex[0],vertex[1]] = 4
                
        x,y = rec.shape
        col,char = None,None
        
        for i in range(x):
            for j in range(y):
                val = rec[i][j]
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
                ii = rec.shape[0]-i-1
                plt.plot(j,ii,char,color=col)
        plt.show()
    
    def print_meta_path(self,graph,k):
        
        count = 0
        rec = self.rectangle.copy()
        for x in range(rec.shape[0]):
            for y in range(rec[x].shape[0]):
                if rec[x][y] == 4:
                    rec[x][y] = 0

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
            if rec[vertex[0],vertex[1]] == 0:
                rec[vertex[0],vertex[1]] = 4  
        for i in rec:
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
            
    def print_reverse_meta_grid(self,graph,k,print_grid=True):
        
        if print_grid:
            count = 0
            rec = self.rectangle.copy()
            for x in range(rec.shape[0]):
                for y in range(rec[x].shape[0]):
                    if rec[x][y] == 4:
                        rec[x][y] = 0

            total_paths = []
            path_dic = {}
            for v in graph.keys():
                for u in graph[v]:
                    #path = bres(v[1],v[0],u[1],u[0])
                    path = list(bresenham(k*v[0],k*v[1],k*u[0],k*u[1]))
                    total_paths += path
                    path_dic[(k*v,k*u)] = path
            #print(path_dic)
            for vertex in total_paths:
                if rec[vertex[0],vertex[1]] == 0:
                    rec[vertex[0],vertex[1]] = 4
            

            for i in rec:
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
            
        met_graph = {}
        for key in graph:
            met_graph[(k*key[0],k*key[1])] = []
            for a in graph[key]:
                met_graph[(k*key[0],k*key[1])].append((k*a[0],k*a[1]))
        return met_graph
    
    


    