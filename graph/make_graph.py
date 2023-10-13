def make_graph(clusters,source,dest,rect_shape):
    x0,y0 = source
    xn,yn = dest
    
    graph = {}
    q = []
    q.append((x0,y0))
    i=0
    while q:
        i+=1
        x0,y0 = q.pop(0)
        for i,j,k in clusters:
            if i <= y0 or i >= yn: continue
            print(i,j,k)
            m = (x0-xn)*(1.0)/(y0-yn)
            c1 = x0*(1.0) + m*(i-y0) - j
            c2 = x0*(1.0) + m*(i-y0) - k
            print(x0,m,i,y0,j,k,c1,c2)
            if c1*c2 <0 :
                dy = i-1
                if j-1>=0:
                    graph[(x0,y0)] = []
                    graph[(x0,y0)].append((j-1,i-1))
                    q.append((j-1,i+1))
                if k+1>=0:
                    graph[(x0,y0)].append((k+1,i-1))
                    q.append((k+1,i+1))
                break
    return graph