import redis
import heapq

class Graph:
    def __init__(self):
        self.redis_conn = redis.StrictRedis(host='localhost', port=6379, db=0)
    
    def add_edge(self, start, end, weight):
        self.redis_conn.hset('graph', f'{start}-{end}', weight)
    
    def dijkstra(self, start, end):
        queue = [(0, start)]
        visited = set()
        distances = {node: float('inf') for node in self.redis_conn.hkeys('graph')}
        distances[start] = 0
        while queue:
            current_distance, current_node = heapq.heappop(queue)
            if current_node == end:
                return distances[end]
            if current_node in visited:
                continue
            visited.add(current_node)
            for neighbor in self.get_neighbors(current_node):
                distance = current_distance + self.get_weight(current_node, neighbor)
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(queue, (distance, neighbor))
        return float('inf')
    
    def get_neighbors(self, node):
        return [key.decode().split('-')[1] for key in self.redis_conn.hkeys('graph') if key.decode().split('-')[0] == node]
    
    def get_weight(self, start, end):
        return int(self.redis_conn.hget('graph', f'{start}-{end}'))

# Ejemplo de uso
if __name__ == "__main__":
    g = Graph()
    g.add_edge('A', 'B', 1)
    g.add_edge('A', 'C', 4)
    g.add_edge('B', 'C', 2)
    g.add_edge('B', 'D', 5)
    g.add_edge('C', 'D', 1)
    
    shortest_distance = g.dijkstra('A', 'D')
    print(f"La ruta más corta entre A y D es de longitud: {shortest_distance}")
