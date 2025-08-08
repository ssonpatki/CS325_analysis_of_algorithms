'''
    For testing he'll put it in a different directory, call <three_min_spanning_trees>,
    then check its output or whatever lmao
'''

def three_min_spanning_trees(input_file_path, output_file_path):
    def find(parent, node):
        if parent[node] != node:
            parent[node] = find(parent, parent[node])
        return parent[node]

    def union(parent, rank, node1, node2):
        root1 = find(parent, node1)
        root2 = find(parent, node2)

        if root1 != root2:
            if rank[root1] > rank[root2]:
                parent[root2] = root1
            elif rank[root1] < rank[root2]:
                parent[root1] = root2
            else:
                parent[root2] = root1
                rank[root1] += 1
            return True
        return False

    def kruskal_algorithm(vertex_count, edges, excluded_edges=set()):
        parent = list(range(vertex_count))
        rank = [0] * vertex_count
        total_weight = 0
        selected_edges = []

        for node1, node2, weight in edges:
            if (node1, node2) not in excluded_edges and (node2, node1) not in excluded_edges:
                if union(parent, rank, node1, node2):
                    total_weight += weight
                    selected_edges.append((node1, node2, weight))
        return total_weight, selected_edges

    # Custom function to extract the weight from each edge tuple (node1, node2, weight)
    def get_weight_from_edge(edge):
        return edge[2]

    # Custom function to extract the weight for finding the largest edge
    def get_weight_from_edge_for_max(edge):
        return edge[2]

    adjacency_matrix = []
    with open(input_file_path, 'r') as file:
        vertex_count = int(file.readline().strip())
        for line in file:
            adjacency_matrix.append([int(x) for x in line.strip().split(',')])

    edge_list = []
    for i in range(vertex_count):
        for j in range(i):
            if adjacency_matrix[i][j] > 0:
                edge_list.append((i, j, adjacency_matrix[i][j]))

    # Sorting edges based on their weight (third element in the tuple)
    edge_list.sort(key=get_weight_from_edge)

    mst_weight1, mst_edges1 = kruskal_algorithm(vertex_count, edge_list)

    mst_weight2 = float('inf')
    excluded_edges2 = set()
    if mst_edges1:
        # Find the largest edge from the selected edges (using the custom function)
        largest_edge = max(mst_edges1, key=get_weight_from_edge_for_max)
        excluded_edges2 = {(largest_edge[0], largest_edge[1]), (largest_edge[1], largest_edge[0])}
        mst_weight2, _ = kruskal_algorithm(vertex_count, edge_list, excluded_edges2)

    mst_weight3 = float('inf')
    excluded_edges3 = set()
    if mst_edges1 and mst_weight2 != float('inf'):
        second_largest_edge = max([edge for edge in mst_edges1 if (edge[0], edge[1]) not in excluded_edges2], key=get_weight_from_edge_for_max)
        excluded_edges3 = {(second_largest_edge[0], second_largest_edge[1]), (second_largest_edge[1], second_largest_edge[0])}
        mst_weight3, _ = kruskal_algorithm(vertex_count, edge_list, excluded_edges3)

    if mst_weight3 == float('inf'):
        mst_weight3 = float('inf')

    # Writing results to the output file
    with open(output_file_path, 'w') as file:
        file.write(f"{mst_weight1}\n")
        file.write(f"{mst_weight2}\n")
        file.write(f"{mst_weight3}\n")

    # Printing the results
    print(mst_weight1)
    print(mst_weight2)
    print(mst_weight3)

three_min_spanning_trees("test_cases/input2.txt", "test_cases/output.txt")