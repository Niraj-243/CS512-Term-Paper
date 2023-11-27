import numpy as np
def find_optimal_path(graph,source,destination):

    def manhattan_distance(p1,p2):
        return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])
    def eucledian_distance(p1,p2):
        return np.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)
    opt_path = {}
    n = len(graph)
    dis = {}
    dis[source] = 0
    for i in range(n):
        for cur_node in graph:
            if cur_node not in dis:
                continue
            for child in graph[cur_node]:
                if child not in dis:
                    dis[child] = dis[cur_node] + manhattan_distance(cur_node,child)
                    cur_list = []
                    cur_list.append(cur_node)
                    opt_path[child] = cur_list
                elif dis[cur_node] + manhattan_distance(cur_node,child) < dis[child]:
                    dis[child] = dis[cur_node] + manhattan_distance(cur_node,child)
                    cur_list = []
                    cur_list.append(cur_node)
                    opt_path[child] = cur_list

    # return opt_path
    opt_path_dest_to_src = {}
    cur_node = destination
    while cur_node != source:
        next_node = opt_path[cur_node][0]
        cur_list = []
        cur_list.append(next_node)
        opt_path_dest_to_src[cur_node] = cur_list
        cur_node = next_node
    def path_len(path):
        len = 0
        for k in path:
            for l in path[k]:
                len += eucledian_distance(k,l)
        return len
    return opt_path_dest_to_src,path_len(opt_path_dest_to_src)

                