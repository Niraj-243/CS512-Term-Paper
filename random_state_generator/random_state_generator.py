import numpy as np
import random

def random_state_generator(length,height,num):
    arr = np.zeros((height,length))
    x_pts = random.sample(list(np.arange(2,length-1,5)),num)
    y_pts = [[0,0] for i in x_pts]
    for i,p in enumerate(x_pts):
        yp = random.sample(range(2,height-1),2)
        yp.sort()
        y_pts[i] = yp
    for i,xp in enumerate(x_pts):
        for j in range(y_pts[i][0],y_pts[i][1]+1):
            arr[j][xp] = 1
    x_source = 0
    y_source = height - 1
    x_dest = length - 1
    y_dest = 0        
    '''
    x_source,x_dest = None,None
    while 1:
        x_source = random.choice(range(0,length))
        if x_source not in x_pts:
            break
    while 1:
        x_dest = random.choice(range(0,length))
        if x_dest not in x_pts and x_dest > x_source:
            break
    y_source,y_dest = random.choice((range(0,height))),random.choice((range(0,height)))
    '''
    arr[y_source][x_source] = 2 
    arr[y_dest][x_dest] = 3
    return arr,(y_source,x_source),(y_dest,x_dest)