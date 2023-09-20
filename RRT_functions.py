from Classes import Node
from Classes import Obstacle

import matplotlib.pyplot as plt
import numpy 
import random
import math

def compute_index(min_x:int, max_x:int, min_y:int, max_y:int, 
                  gs, x_curr, y_curr):
    index = ((x_curr - min_x)/gs) + ((y_curr - min_y)/gs*(max_x+gs-min_x)/gs)

    return index
def Obstacle_List(min_x,max_x,min_y,max_y,gs):
    obstacle_list = dict()
    my_obstacles = [(2,2),(2,3),(2,4),(5,5),(5,6),(6,6),(7,6),(7,5),(7,4),(7,3),(8,6),(3,7)]
    for i in my_obstacles:
#   Storing the given obstacles into the Obstacle class with the given diameter.
        obstacle = Obstacle(i[0],i[1])
        obstacle_list[compute_index(min_x, max_x, min_y, max_y, gs, obstacle.x, obstacle.y)] = obstacle
    return obstacle_list

def inside(obstacle,node) -> bool:
        dist_from = numpy.sqrt((node.xx - obstacle.x)**2 + (node.yy - obstacle.y)**2)
        
        if dist_from > obstacle.radius:
            return False
        return True

def Cost(Node_1,Node_2_x, Node_2_y, Node_cost) -> float:
 euclidian = numpy.sqrt(((Node_2_x - Node_1.x)**2+(Node_2_y - Node_1.y)**2)) + Node_cost
 return euclidian

def RRT_Brancher(step,visited_nodes,min_x,max_x,min_y,max_y,gs,i,obstacle_list):
    global check
    check = True
    x = random.randint(min_x,max_x)
    y = random.randint(min_y,max_y)
    for n in visited_nodes:
     visited_nodes[n].Acost = Cost(visited_nodes[n],x,y,0)
    current_node = visited_nodes[min(visited_nodes, key=lambda x:visited_nodes[x].Acost)]
    xt = x -current_node.x
    yt = y - current_node.y
    theta = math.atan2(yt,xt)
    xs = numpy.sqrt((step**2)/(math.tan(theta)**2 + 1))
    ys = math.tan(theta) * xs
    cost = current_node.cost + 0.5
    parent =(compute_index(min_x, max_x, min_y, max_y, gs, current_node.x, current_node.y))
    new_node = Node(xs + current_node.x, ys + current_node.y, list(visited_nodes.keys())[list(visited_nodes.values()).index(current_node)], cost, 0)
    for l in obstacle_list:
     distance = numpy.sqrt(((new_node.x - obstacle_list[l].x)**2+(new_node.y - obstacle_list[l].y)**2))
     if (obstacle_list[l].radius) > distance:
        
         check = False;
    if not check:
        return current_node
    else:
        visited_nodes[i] = new_node
        plt.plot(new_node.x, new_node.y, 'bo')
        plt.pause(0.1)
        plt.show()
    
        return new_node
    