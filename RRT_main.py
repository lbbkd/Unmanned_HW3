import numpy
import matplotlib.pyplot as plt
import RRT_functions
from Classes import Node

min_x = 0
max_x = 10
min_y = 0
max_y = 10
goal_x = 9
goal_y = 8
gs = 0.5
step = 0.5
domain_x = numpy.arange(min_x,max_x+gs,gs)
domain_y = numpy.arange(min_y,max_y + gs,gs)
domain_gs = numpy.arange(-gs,gs + gs,gs)
x_path = []
y_path = []
visited_nodes = dict()
path_nodes = dict()
visited_nodes[0] = Node(1,1,-1,0,0)
goal = Node(9,8,0,0,0)
RRT_functions.Obstacle_List(min_x,max_x,min_y,max_y,gs)
new_node = visited_nodes[0]
plt.axis([min_x, max_x + gs, min_y, max_y + gs])
obstacle_list = RRT_functions.Obstacle_List(min_x, max_x, min_y, max_y, gs)
for o in obstacle_list:
    plt.plot(obstacle_list[o].x, obstacle_list[o].y,'ks', markersize = 15)
    plt.show
i = 1
while RRT_functions.Cost(new_node, goal_x, goal_y, 0) > 2:
    new_node = RRT_functions.RRT_Brancher(step, visited_nodes, min_x, max_x, min_y, max_y, gs,i,obstacle_list)
    i = i + 1
    
goal.cost = RRT_functions.Cost(new_node,goal.x,goal.y,new_node.cost)
goal.parent_index = list(visited_nodes.keys())[list(visited_nodes.values()).index(new_node)]
path_nodes[0] = goal
trail_node = goal
x_path.append(goal.x)
y_path.append(goal.y)
k = 1
while trail_node.parent_index != -1:
    trail_node = visited_nodes[trail_node.parent_index]
    path_nodes[k] = trail_node
    x_path.append(trail_node.x)
    y_path.append(trail_node.y)
    k = k + 1
x = 1
for i in path_nodes:
    if x != len(path_nodes):
        plt.plot(x_path, y_path, 'ro-')
    x = x + 1
plt.show()