from cluster.cluster import make_clusters
from input.grid import grid
from graph.make_graph import make_graph
from graph.find_path import find_optimal_path
from random_state_generator.random_state_generator import random_state_generator
import time

length = 60
height = 30
num = 5
k = 2 #how much we want to shorten the grid into; for example for k=2 100x100 turns into 50x50; for k=5 100x100 turns into 20x20
rectangle,source,dest = random_state_generator(length,height,num,gap=k+3)

grid = grid(rectangle)

#This will print grid
# grid.print_grid()

clusters = make_clusters(rectangle)
graph = make_graph(clusters,source,dest)
# print(graph)

grid.add_graph(graph)
print("\n")
grid.print_grid()
grid.plot_grid()

# optimal path
start = time.time()
opt_path,opt_path_len = find_optimal_path(graph,source,dest)
end = time.time()
time_taken = end-start
print(f'runtime : {time_taken}')
print('opt path\n',opt_path)
print(f'path len : {opt_path_len}')
grid.add_opt_path(opt_path)
print("\n")
grid.print_opt_path()
grid.plot_opt_path()


# meta
grid.make_meta_grid(k=k)
meta_clusters = make_clusters(grid.meta_rect)
meta_src = (grid.meta_rect.shape[0]-1,0)
meta_dest = (0,grid.meta_rect.shape[1]-1)
meta_graph = make_graph(meta_clusters,meta_src,meta_dest)

grid.add_graph(meta_graph,type="meta")
print("\n")
grid.print_grid(type="meta")
grid.plot_grid(type="meta")

# optimal path meta
opt_meta_path,opt_meta_path_len = find_optimal_path(meta_graph,meta_src,meta_dest)
grid.add_opt_path(opt_meta_path,"meta")
print("\n")
grid.print_opt_path(type="meta")
grid.plot_opt_path(type="meta")


# reverse mapping
print("\n")
met_path_graph = grid.print_reverse_meta_grid(meta_graph,k)
src = (meta_src[0]*k,meta_src[1]*k)
dst = (meta_dest[0]*k,meta_dest[1]*k)
meta_opt_path,meta_opt_path_len = find_optimal_path(met_path_graph,src,dst)
print("\n")
grid.print_meta_path(meta_opt_path,k)
grid.plot_meta_path(meta_opt_path,k)




