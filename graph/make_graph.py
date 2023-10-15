def make_graph(clusters,source,dest):
    x0,y0 = source
    xn,yn = dest
    xn_1,yn_1 = xn,yn
    graph = {}
    q = []
    q.append((x0,y0,xn_1,yn_1))
    inserted_tuples = set()
    inserted_tuples.add((x0,y0,xn_1,yn_1))
    while q:            
        x0,y0,xn_1,yn_1 = q.pop(0)
        if x0==xn and y0==yn: break
        cut = False
        if (x0,y0) not in graph:
            graph[(x0,y0)] = []
        brake = False
        for i,j,k in clusters:
            if brake == True:
                continue
            if i <= y0 or i >= yn_1: continue
            m = (x0-xn_1)*(1.0)/(y0-yn_1)
            c1 = x0*(1.0) + m*(i-y0) - j
            c2 = x0*(1.0) + m*(i-y0) - k
            if c1*c2 < 0 :
                if j-1>=0:
                    if (x0,y0,j-1,i-1) not in inserted_tuples: 
                        q.append((x0,y0,j-1,i-1))
                        inserted_tuples.add((x0,y0,j-1,i-1))
                    if (j-1,i+1,xn_1,yn_1) not in inserted_tuples: 
                        q.append((j-1,i+1,xn_1,yn_1))
                        inserted_tuples.add((j-1,i+1,xn_1,yn_1))
                    if (j-1,i-1) not in graph:
                        graph[(j-1,i-1)] = []
                    graph[(j-1,i-1)].append((j-1,i+1))

                if k+1>=0:
                    if (x0,y0,k+1,i-1) not in inserted_tuples:
                        q.append((x0,y0,k+1,i-1))
                        inserted_tuples.add((x0,y0,k+1,i-1))
                    if (k+1,i+1,xn_1,yn_1) not in inserted_tuples:
                        q.append((k+1,i+1,xn_1,yn_1))
                        inserted_tuples.add((k+1,i+1,xn_1,yn_1))
                    if (k+1,i-1) not in graph:
                        graph[(k+1,i-1)] = []
                    graph[(k+1,i-1)].append((k+1,i+1))
                cut = True
                brake = True
        if cut == False:
            graph[(x0,y0)].append((xn_1,yn_1))     
    return graph