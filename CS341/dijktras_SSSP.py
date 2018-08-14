'''
Find the single source shortest path to all nodes of a graph with non negative edge weights
This is using an adjacency matrix

Time complexity O(n^2) since we iterate on n vertices and n (possible) edges
'''

def dijktras_SSSP(adj_matrix, source):
    dist = [-1]*len(adj_matrix)
    dist[source]=0

    #Construct priority queue for vertices (list of tuples)
    pq = [(-1, i) for i in range(0, len(adj_matrix))]
    pq[source]=(0,source)

    while len(pq) > 0:
        #Remove the lowest distance vertex
        min_value = pq[0]
        for i in range(0, len(pq)):
            if (pq[i][0] != -1 and pq[i][0] < min_value[0]) or (min_value[0] == -1 and pq[i][0] != -1):
                min_value = pq[i]
        pq.remove(min_value)

        #Iterate on all adjacent edges and update dist values
        for i in range(0, len(adj_matrix)):
            #if the distance from the vertex to the neighbour has a lower weight
            if (dist[i] == -1 and adj_matrix[min_value[1]][i] != -1 and dist[min_value[1]] != -1) or (dist[min_value[1]] + adj_matrix[min_value[1]][i] < dist[i] and adj_matrix[min_value[1]][i] != -1 and dist[min_value[1]] != -1):
                dist[i] = dist[min_value[1]] + adj_matrix[min_value[1]][i]
                #Update value in priority queue
                pq = list(filter(lambda x: x[1] != i,pq))
                pq.append((dist[i], i))

    return(dist)

"""
Expected output: 
[0, 6, 12, 1, 22, 8, 21, 29]
[12, 6, 0, 13, 10, 6, 9, 17]
[8, 2, 6, 9, 16, 0, 15, 23]
[29, 23, 17, 30, 7, 23, 8, 0]
"""
test_input = [
    [0,6,-1,1,-1,-1,-1,-1],
    [6,0,6,9,-1,2,-1,-1],
    [-1,6,0,-1,-1,6,9,-1],
    [1,9,-1,0,-1,-1,-1,-1],
    [-1,-1,-1,-1,0,-1,1,7],
    [-1,2,6,-1,-1,0,-1,-1],
    [-1,-1,9,-1,1,-1,0,-1],
    [-1,-1,-1,-1,7,-1,-1,0],
    ]
print(dijktras_SSSP(test_input, 0))
print(dijktras_SSSP(test_input, 2))
print(dijktras_SSSP(test_input, 5))
print(dijktras_SSSP(test_input, 7))
