def prima_algo(matrix):
    length = len(matrix)
    vertices = [False] * length
    vertices[0] = True
    num_of_edges = 0
    cable_lenght = 0

    while num_of_edges < length - 1:
        minimum = float('inf')
        x = -1
        for i in range(length):
            if vertices[i]:
                for j in range(length):
                    if not vertices[j] and matrix[i][j] != 0 and matrix[i][j] < minimum:
                        minimum = matrix[i][j]
                        x = j
        if x == -1:
            return -1

        vertices[x] = True
        num_of_edges += 1
        cable_lenght += minimum

    return cable_lenght


def read_file(input_file):
    with open(input_file, 'r') as file:
        first_line = file.readline()
        if not first_line:
            return None
    communication_with_wells = []
    wells = set()
    with open(input_file, 'r') as file:
        for line in file:
            line = line.strip()
            start_well, end_well, weight = line.split(', ')
            weight = int(weight)
            communication_with_wells.append((start_well, end_well, weight))
            wells.add(start_well)
            wells.add(end_well)

    width_of_matrix = len(wells)
    well_index = {node: i for i, node in enumerate(wells)}
    adjacency_matrix = [[0] * width_of_matrix for _ in range(width_of_matrix)]

    for start_well, end_well, weight in communication_with_wells:
        i, j = well_index[start_well], well_index[end_well]
        adjacency_matrix[i][j] = weight
        adjacency_matrix[j][i] = weight

    return prima_algo(adjacency_matrix)
