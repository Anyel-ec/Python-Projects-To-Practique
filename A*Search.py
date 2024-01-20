from queue import PriorityQueue

def a_star(start, goal, graph, heuristic):
    open_set = PriorityQueue()
    open_set.put((0, start))
    
    came_from = {}
    g_score = {start: 0}
    
    while not open_set.empty():
        _, current = open_set.get()
        
        if current == goal:
            path = reconstruct_path(came_from, goal)
            return path
        
        for neighbor, cost in graph[current]:
            tentative_g_score = g_score[current] + cost
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + heuristic[neighbor]
                open_set.put((f_score, neighbor))
                came_from[neighbor] = current
    
    return None

def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.insert(0, current)
    return path

# Crear el grafo y las heurísticas
graph = {
    1: [(2, 200)],
    2: [(1, 200), (3, 150)],
    3: [(2, 150), (6, 225)],
    4: [(3, 350), (5, 300)],
    5: [(4, 300), (6, 400), (7, 250)],
    6: [(3, 225), (5, 400)],
    7: [(5, 250), (8, 125)],
    8: [(7, 125)]
}

heuristic = {1: 650, 2: 500, 3: 650, 4: 325, 5: 375, 6: 12, 7: 0, 8: 0}

# Aplicar A* para encontrar el camino óptimo
start_city = 1
goal_city = 8
path = a_star(start_city, goal_city, graph, heuristic)

if path:
    print(f"El mejor camino entre las ciudades {start_city} y {goal_city} es: {path}")
else:
    print(f"No hay camino posible entre las ciudades {start_city} y {goal_city}.")
