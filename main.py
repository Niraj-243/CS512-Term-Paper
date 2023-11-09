from cluster.cluster import make_clusters
from input.grid import grid
from graph.make_graph import make_graph
from random_state_generator.random_state_generator import random_state_generator

length = 60
height = 30
num = 4
k = 2 #how much we want to shorten the grid into; for example for k=2 100x100 turns into 50x50; for k=5 100x100 turns into 20x20
rectangle,source,dest = random_state_generator(length,height,num,gap=k+1)

grid = grid(rectangle)

#This will print grid
# grid.print_grid()

clusters = make_clusters(rectangle)
graph = make_graph(clusters,source,dest)
# print(graph)

grid.add_graph(graph)


grid.print_grid()
#grid.plot_grid()
grid.make_meta_grid(k=k)
grid.plot_meta_grid()

