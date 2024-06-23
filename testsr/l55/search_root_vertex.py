def bfs(adjacency_list, vertex):
    vertex_count = []
    queue = []
    visited = set()

    visited.add(vertex)
    queue.append(vertex)

    while queue:
        current_vertex = queue.pop(0)
        vertex_count.append(current_vertex)

        for n in adjacency_list[current_vertex]:
            if n not in visited:
                visited.add(n)
                queue.append(n)

    if len(vertex_count) == len(adjacency_list):
        return True
    else:
        return False


def read_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    if not lines:
        return {}

    adjacency_list = {}
    for line in lines:
        vertices = list(map(int, line.strip().split()))
        start_vertex = vertices[0]
        connected_vertices = vertices[1:]
        adjacency_list[start_vertex] = connected_vertices

    return adjacency_list


def write_output(output_file, result):
    with open(output_file, 'w') as file:
        file.write(str(result))
    return


def search_root_vertex(input_file, output_file):
    adjacency_list = read_file(input_file)

    if not adjacency_list:
        return write_output(output_file, None)

    root_vertices = []
    for vertex in adjacency_list:
        root_vertex = bfs(adjacency_list, vertex)
        if root_vertex:
            root_vertices.append(vertex)

    if not root_vertices:
        return write_output(output_file, -1)

    return write_output(output_file, root_vertices[0])
