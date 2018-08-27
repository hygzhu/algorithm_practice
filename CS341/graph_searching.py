graph_1 = [
    (0,[]),
    (1,[2,5]),
    (2,[1,3,4]),
    (3,[2,10]),
    (4,[2]),
    (5,[1,6,7]),
    (6,[5,7,8]),
    (7,[5,6,8,9]),
    (8,[6,7]),
    (9,[7,10]),
    (10,[3,9]),
]

graph_2 = [
    (0,[1]),
    (1,[0,2,5]),
    (2,[4,5,6]),
    (3,[5]),
    (4,[2,7]),
    (5,[1,2,3,6]),
    (6,[2,5]),
    (7,[4])
]

"""
Breadth first search on a graph with adjacency list representation
Takes in a graph and a source vertex to start the search

Time complexity: O(m+n) since we go through all vertices and edges once
"""
def BFS(G, s):
    status = dict()
    for i in range(len(G)):
        #Set status to undiscovered
        status[G[i][0]]=False 
    status[s]=True
    queue = [s]
    tree = []
    while len(queue) > 0:
        v = queue.pop(0)
        #Add all undiscovered neighbours to the queue
        for w in G[v][1]:
            if not status[w]:
                status[w] = True
                queue.append(w)
        tree.append(v)
    return tree

#print(BFS(graph_1, 1))
#print(BFS(graph_1, 10))



"""
Depth first search with recursion

Time complexity: O(m+n) since we go through all vertices and edges once
Same as BFS
"""

def DFS(G, s):
    visited = dict()
    for i in range(len(G)):
        #Set status to undiscovered
        visited[G[i][0]]=False 
    pre = []
    post = []
    Explore(G, s, visited, pre, post)
    return (pre, post)

def Explore(G, s, visited, pre, post):
    visited[s] = True
    pre.append(s)
    #Explore each adjacent vertex
    for w in G[s][1]:
        if not visited[w]:
            Explore(G, w, visited, pre, post)
    post.append(s)


#print(DFS(graph_1, 1))
#print(DFS(graph_2, 6))