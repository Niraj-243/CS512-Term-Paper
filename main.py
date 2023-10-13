from cluster.cluster import make_clusters
from input.grid import grid
from graph.make_graph import make_graph
from random_state_generator.random_state_generator import random_state_generator

length = 60
height = 40
num = 8
rectangle,source,dest = random_state_generator(length,height,num)

grid = grid(rectangle)

# This will print grid
# grid.print_grid()

clusters = make_clusters(rectangle)
graph = make_graph(clusters,source,dest)
print(graph)

