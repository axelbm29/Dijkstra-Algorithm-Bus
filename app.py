import heapq

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = {}

    def add_edge(self, vertex1, vertex2, weight):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            self.vertices[vertex1][vertex2] = weight
            self.vertices[vertex2][vertex1] = weight

    def dijkstra(self, start, end):
        distance = {v: float('inf') for v in self.vertices}
        distance[start] = 0
        path = {}
        heap = [(0, start)]

        while heap:
            d_current, v_current = heapq.heappop(heap)
            if d_current > distance[v_current]:
                continue
            for neighbor, weight in self.vertices[v_current].items():
                d = d_current + weight
                if d < distance[neighbor]:
                    distance[neighbor] = d
                    path[neighbor] = v_current
                    heapq.heappush(heap, (d, neighbor))

        shortest_path = []
        current = end
        while current != start:
            shortest_path.append(current)
            current = path[current]
        shortest_path.append(start)
        return distance[end], shortest_path[::-1]

    def create_graph(self):
        graph = Graph()
        num_vertices = int(input("Enter the number of vertices in the graph: "))
        for i in range(num_vertices):
            vertex = input(f"Enter the name of vertex {i + 1}: ")
            graph.add_vertex(vertex)

        add_edges = 'y'
        while add_edges.lower() == 'y':
            vertex1 = input("Choose the first vertex of the edge: ")
            vertex2 = input("Choose the second vertex of the edge: ")
            weight = float(input("Enter the weight of the edge that connects them: "))
            graph.add_edge(vertex1, vertex2, weight)
            add_edges = input("Do you want to add another edge? (y/n): ")
        return graph

    def show_menu(self):
        print("\nMENU:")
        print("a. Create a graph")
        print("b. Find the shortest path in the graph")
        print("c. Exit")

    def main(self):
        graph = None
        while True:
            self.show_menu()
            option = input("Choose an option: ")
            if option.lower() == 'a':
                graph = self.create_graph()
            elif option.lower() == 'b':
                if graph is None:
                    print("You must first create a graph!")
                else:
                    start = input("Enter the starting vertex of the path: ")
                    end = input("Enter the ending vertex of the path: ")
                    distance, path = graph.dijkstra(start, end)
                    print(f"The shortest path from {start} to {end} is: {path} with a distance of {distance}")
            elif option.lower() == 'c':
                print("Exiting the program...")
                break
            else:
                print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    g = Graph()
    g.main()
