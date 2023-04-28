#aStar search
def path_f_cost(path) :
    g_cost = 0
    y_cost = 0
    for(node, val) in path :
        g_cost +=val
        lst_node = path[-1][0]
        h_cost = h_table[lst_node]
        f_cost = h_cost + g_cost

    return f_cost, g_cost

def a_star(graph, beg, end) :
    visited = []
    Pqueue = [[(beg, 0)]]
    while Pqueue : 
        Pqueue.sort(key=path_f_cost)
        path = Pqueue.pop(0)
        print(type(path))
        node = path[0][0]
        if node in visited : 
            continue
        visited.append(node)

        if node == end : 
            return path
        else : 
            adj = graph.get(node, [])
            for(node2, val) in adj :
                path2 = path.copy()
                path2.append(node2, val)
                Pqueue.append(path2)
    return path
    #print(type(path))
h_table = {
        'S' : 7, 
        'A' : 6,
        'B' : 4,
        'C' : 2,
        'G' : 0
    }
    
graph = {
    'S' : [('A', 1), ('B', 4)],
    'A' : [('B', 2), ('C', 4), ('G', 12)],
    'B' : [('C', 2)],
    'C' : [('G', 3)]
}

ans = a_star(graph, 'S', 'G')
print(type(ans))
print(ans)
    