
import heapq
import numpy as np

graph = {
    'Restaurant': [('A', 2), ('B', 5)],
    'A': [('Restaurant', 2), ('C', 4)],
    'B': [('Restaurant', 5), ('C', 1), ('D', 7)],
    'C': [('A', 4), ('B', 1), ('Customer', 3)],
    'D': [('B', 7), ('Customer', 2)],
    'Customer': [('C', 3), ('D', 2)]
}
def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = [(0, start)]

    while queue:
        current_dist, current_node = heapq.heappop(queue)
        for neighbor, weight in graph[current_node]:
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
    return distances


shortest_distances = dijkstra(graph, 'Restaurant')
shortest_distance = shortest_distances['Customer']

print(f"Shortest Distance from Restaurant to Customer: {shortest_distance} km")

def predict_delivery_time(age, rating, distance):
    time = (distance * 2) + (30 - age) * 0.5 + (5 - rating) * 3
    return max(time, 0)


delivery_person_age = 25
delivery_person_rating = 4.7

predicted_time = predict_delivery_time(delivery_person_age, delivery_person_rating, shortest_distance)

print(f"Predicted Delivery Time: {predicted_time:.2f} minutes")