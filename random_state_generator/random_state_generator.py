import numpy as np
import random

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