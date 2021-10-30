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



# Visualization
## A* Exploration

## Dijkstra's Exploration
