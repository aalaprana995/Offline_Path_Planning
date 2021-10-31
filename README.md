# Offline_Path_Planning
This project repository is for navigating a point robot and a rigid robot without collision in a configuration space using A* and dijkstra's algorithm.
## Algorithms
### A* Algorithm

The worse case time complexity is O(E), where E is the number of edges in the graph.
In the worse case we can have all the edges inside the open list, so required auxiliary space in worst case is O(V), where V is the total number of vertices.


### Dijkstra's Algorithm

Space complexity of Dijkstra's algorithm is O(V2) where V denotes the number of vertices (or nodes) in the graph.

### Experimental Details
This algorithms are used on the map displayed in the diagram below to find an shortest path form start point to end point.
There are four obstacles formed using algebraic expression and concepts of geometry.

The obstacle space is modified based on the robot size to avoid collision and investigate results for point size and rigid robots.
For our project purpose we are using circular robot.

![Screenshot from 2021-10-31 14-53-59](https://user-images.githubusercontent.com/93336207/139597574-8b115a41-36f7-4bdd-a208-082df8f8e3eb.png)

![Screenshot from 2021-10-31 14-50-28](https://user-images.githubusercontent.com/93336207/139597474-53dfdefb-6285-40e6-ab53-e2aa71f7d9ea.png)

# Visualization
## A* Exploration

## Dijkstra's Exploration
