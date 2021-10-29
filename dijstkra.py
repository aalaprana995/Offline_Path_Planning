# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 12:05:44 2019

@author: Aalap
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 01:24:08 2019

@author: Aalap
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 18:47:25 2019

@author: Aalap
"""

import numpy as np
import matplotlib.pyplot as plt
import math

class Node:
    def __init__(self, nodex, nodey, cost, parentnode):
        self.nodex = nodex
        self.nodey = nodey
        self.cost = cost
        self.parentnode = parentnode
    def get_nodex(self):
        return self.nodex
    def get_nodey(self):
        return self.nodey

def shortest_path(goalnode, visited, reso):
    #shortest path found until parent id is -1
    path_x = []#stroes path x coordinates
    path_y = []#stroes path x coordinates
    path_x.append((goalnode.nodex))
    path_y.append((goalnode.nodey))
    p = goalnode.parentnode
    while (p != -1):
        tracknode = visited[p]
        path_x.append((tracknode.nodex))
        path_y.append((tracknode.nodey))
        p = tracknode.parentnode
    return path_x, path_y

def node_key(node):
    node_key = (node.nodex) * 250 + node.nodey#unique key generation by equation
    return node_key

def check_node(node,obsmap,obs_x,obs_y):
    #check of node correctness
    if (node.nodex < (min(obs_x)) or node.nodex > (max(obs_x)) or node.nodey < (min(obs_y)) or node.nodey > (max(obs_y))):
        return False
    if (obsmap[node.nodex][node.nodey]):
        return False
    if (node.nodex < 0):
        return False
    if (node.nodex > 250):
        return False
    if (node.nodey < 0):
        return False
    if (node.nodey > 150):
        return False
    return True

def check_goal_node(node,goalnode):
    if(node.nodex==goalnode.nodex and node.nodey==goalnode.nodey):
        return True

def obstacle_map(obs_x, obs_y):
    max_x = round(max(obs_x))
    max_y = round(max(obs_y))
    min_x = round(min(obs_x))
    min_y = round(min(obs_y))

    obsmap = np.zeros((251,151))#make a world space which is all false
    for i in range(min_x,max_x):
        for j in range(min_y,max_y):
            obsmap[i][j]=False#make a obstacle space that is all false
    for index,i in enumerate(obs_x):
        obsmap[obs_x[index]][obs_y[index]] = True#update the obstacle space at points where there is obstacle to true
    return obsmap

def obstacle_space(r,c):
    points=[]#stores points of obstacle space
    obs_x=[]#stores x coordinates of obstacle space
    obs_y=[]#stores y coordinates of obstacle space
    
    #parrallel shifts calculated 
    e=r+c
    l1=e*math.sqrt((-41/25)**2+1)
    p1=round(6525/25) -l1
    l2=e*math.sqrt((-2/19)**2+1)
    p2=l2+round(1314/19)
    l3=e*math.sqrt((38/7)**2+1)
    p3=l3-round(5830/7)
    l4=-e*math.sqrt((37/20)**2+1)
    p4=-(6101/20)+l4
    l5=(e*math.sqrt((-38/23)**2+1))
    p5= l5+ round((8530/23))
    l6=- e*math.sqrt((-37/10)**2+1)
    p6= (6551/10)+l6
    l7=e*math.sqrt((-37/10)**2+1)
    p7=  l7 +(6551/10)

   
     #circular obstacle space
    print("computing circle obstacle")
    k = 15 + (r) + c
    for i in range(e,251-e):
        for j in range(e,151-e):
            if (round((i - 190) ** 2 + (j - 130) ** 2 - (k ** 2)) <= 0):
                obs_x.append(i)
                obs_y.append(j)
                points.append([i,j])
    print("circle obstacle computed")
    #Ellipse obstacle space
    print("computing ellipse obstacle")
    p = 15 + (r) + c
    q =  6+ (r) + c
    for i in range(e,251-e):
        for j in range(e,151-e):
            if (round((((i - 140) ** 2) / (p ** 2)) + (((j - 120) ** 2) / (q ** 2)) - 1) <= 0):
                obs_x.append(i)
                obs_y.append(j)
    print("ellipse obstacle computed")
    #square obstacle space
    print("computing square obstacle")
    for i in range(e,251-e):
        for j in range(e,151-e):
            if ((i - 100-r-c <= 0) & (j - 67.5+r+c >= 0) & (j - 112.5-r-c <= 0) &(i - 50+r+c >= 0)):
                obs_x.append(i)
                obs_y.append(j)
                points.append([i, j])
    print("computed square obstacle")
    #Poly obstacle space
    print("computing poly obstacle")
    
    for i in range(e,251-e):
        for j in range(e,151-e):
             if ((2/19)*i + j - p2 <= 0) and (j+(41/25)*i -p1 >= 0) and (j - 15+e>= 0) and (j<=(-37/10)*i+p7) and((38/23)*i + j - p5 <= 0):
                obs_x.append(i)
                obs_y.append(j)
                points.append([i, j])
    for i in range(e,251-e):
        for j in range(e,151-e):
             if (((-38/7)*i +j - p3 <= 0) and ((38/23)*i + j -p5 <= 0) and ((-37/20)*i +j -p4 >= 0) and (j>=(-37/10)*i+p6)and round(15-r-c <= j)):
                obs_x.append(i)
                obs_y.append(j)
                points.append([i, j])
    print("computed poly obstacle")
#boundary obstacle space
    print("computing boundary obstacle")
    if(r==0 and c==0):
        for i in range(251):
            for j in range(151):
                if(i==0 or i==250 or j==150 or j==0):
                    obs_x.append(i)
                    obs_y.append(j)
                    points.append([i,j])
    else:
        
        e=r+c
        for i in range(e,251-e):
            for j in range(e,151-e):
                if(i==r+c or i==250-r-c or j==150-r-c or j==r+c):
                    obs_x.append(i)
                    obs_y.append(j)
                    points.append([i,j])
    print("computed boundary obstacle")                    
                    
    return obs_x,obs_y
    

def d_algo(startx,starty,goalx,goaly,reso,r,c):
    lx = []#used to store all explored node x
    ly = []#used to store all explored node y
    flag=0
    show=True
    unvisited=dict()#dictionary to storedunvisited node
    visited=dict()#dictionary to stored visited node for back tracking
    moves = [[1, 0, 1], [0, 1, 1], [-1, 0, 1], [0, -1, 1], [1, 1, math.sqrt(2)], [-1, -1, math.sqrt(2)],
             [-1, 1, math.sqrt(2)], [1, -1, math.sqrt(2)]]#all possible moves allowed

    startnode = Node(round(startx / reso), round(starty / reso), 0, -1)#start node formation
    goalnode = Node(round(goalx / reso), round(goaly / reso), 1000, -1)#goal node formation
    obs_x, obs_y = obstacle_space(r, c)#obstacle space fromed 
    #obstacle space in discretized formate
    obs_x = [round(x / reso) for x in obs_x]
    obs_y = [round(y / reso) for y in obs_y]
    #obstacle space converted to true false obstacle map
    obsmap= obstacle_map(obs_x,obs_y)
    #checking if the startnode or  goalnode  is not in obstacle or out of world space
    if not(startnode.nodex < min(obs_x) or startnode.nodex > max(obs_x) or startnode.nodey < min(obs_y) or startnode.nodey > max(obs_y)):
        if not(goalnode.nodex < min(obs_x) or goalnode.nodex > max(obs_x) or goalnode.nodey < min(obs_y) or goalnode.nodey > max(obs_y)):
            if not obsmap[startnode.nodex][startnode.nodey] and not obsmap[goalnode.nodex][goalnode.nodey]:
                flag = 1
            
    unvisited[node_key(startnode)] = startnode
    while (flag):
        current_node_id = min(unvisited, key=lambda o: unvisited[o].cost)#finding minimum cost node
        current_node = unvisited[current_node_id]#making it the current node
        
        visited[current_node_id] = current_node#putting current node to visited dictionary
        del unvisited[current_node_id]#removing current node from unvisited dictionary
        for i, _ in enumerate(moves):#node exploration
            node = Node(current_node.nodex + moves[i][0], current_node.nodey + moves[i][1],current_node.cost + moves[i][2], current_node_id)
            lx.append(Node.get_nodex(node))#used get node to store new nodex in lx
            ly.append(Node.get_nodey(node))#used get node to store new nodey in ly
            if (len(lx)%1000==0):
                if(show):
                    plt.plot(lx,ly,".r")
                    plt.plot(obs_x, obs_y,".k")#obstacle space
                    plt.show()
                    plt.grid()
    
            if (check_goal_node(node, goalnode)):
                goalnode.parentnode = node.parentnode
                goalnode.cost = node.cost
                flag=0
                break
            f = node_key(node)
            if not check_node(node, obsmap,obs_x,obs_y):#check the new node is not in obstacle
                continue
            if f in visited:#check new node in visited
                continue
            if f in unvisited:#check node in unvisited and update the parameters
                if (unvisited[f].cost > node.cost):
                    unvisited[f].cost = node.cost
                    unvisited[f].parentnode = node.parentnode
            else:
                unvisited[f] = node#add new node to unvisited dictionary
        
    a, b = shortest_path(goalnode, visited, reso)#return shortest path
    
    if(flag):
        print("shortest path aaya")
    else:
        print("end")        
    return a, b, obs_x, obs_y, lx,ly

            
                
                
            

    






def main():
    print( "dijstkra algorithm started!!")
    show=True#flag used to display the result
    
    startx = 10.0  # startx coordinate
    starty = 10.0  # starty coordinate
    goalx = 240.0  # goalx coordinate
    goaly = 140.0  # goaly coordinate
    reso = 1  # resolution
    r = 4  #robot radius
    c= 0# clearance
    
    if show:
        plt.plot(startx/reso, starty/reso, "xr")
        plt.plot(goalx/reso, goaly/reso, "xb")
    a,b, obs_x, obs_y, lx,ly =d_algo(startx,starty,goalx,goaly,reso,r,c)
    if show:
#displaying the result
#if input or output is incorrect then only obstacle and start and goal is displayed        
        plt.plot(lx,ly,".g")#node explored
        plt.plot(obs_x, obs_y,".k")#obstacle space
        plt.plot(a, b, "-r")#shortest path
        plt.grid()
        plt.show()
if __name__ == '__main__':
    main()