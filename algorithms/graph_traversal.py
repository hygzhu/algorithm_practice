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

#DFS that returns a path from node a to node b
def dfs_helper(graph, curr, end, seen, path):

    neighbours = graph[curr][1]

    if len(neighbours) == 0 or curr == end:
        if curr != end:
            return []
        else:
            return path + [curr] 
    
    for neighbour in neighbours:
        if neighbour not in seen:
            new_seen = seen.copy()
            new_seen.add(curr)
            res = dfs_helper(graph, neighbour, end, new_seen, path + [curr])
            if res != []:
                return res
    
    return []

def dfs(graph, start, end):
    return dfs_helper(graph, start, end, set(), list())

print(dfs(graph_1, 7,1))
print(dfs(graph_1, 7,0))
print(dfs(graph_1, 2,9))
print(dfs(graph_2, 7,1))

print("_____________________________")

#BFS that returns a path from node a to node b
def bfs(graph, start, end):

    if start == end:
        return [start]

    path = list()
    visited = set()
    visited.add(start)
    path.append(start)

    to_visit = graph[start][1]
    while len(to_visit) != 0:
        next_node = to_visit.pop()
        
        if next_node not in visited:

            if next_node == end:
                return  path + [next_node]

            visited.add(next_node)
            path.append(next_node)

            to_visit += graph[next_node][1]

    if path[len(path)-1] != end:
        return []

    return path


print(bfs(graph_1, 7,1))
print(bfs(graph_1, 7,0))
print(bfs(graph_1, 2,9))
print(bfs(graph_2, 7,1))


