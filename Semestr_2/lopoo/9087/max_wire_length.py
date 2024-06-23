def max_wire_length(distance_between_columns, max_columns_height):
    top_distance = 0
    bottom_distance = 0

    for cur_col_index in range(len(max_columns_height) - 1):
        height_difference = abs(max_columns_height[cur_col_index] - max_columns_height[cur_col_index + 1])

        distance_top_to_bottom = top_distance + calculate_hypotenuse(distance_between_columns,
                                                                     max_columns_height[cur_col_index] - 1)
        distance_bottom_to_top = bottom_distance + calculate_hypotenuse(distance_between_columns,
                                                                        max_columns_height[cur_col_index + 1] - 1)
        distance_top_to_top = top_distance + calculate_hypotenuse(distance_between_columns, height_difference)
        distance_bottom_to_bottom = bottom_distance + distance_between_columns

        top_distance = max(distance_bottom_to_top, distance_top_to_top)
        bottom_distance = max(distance_bottom_to_bottom, distance_top_to_bottom)

    return round(max(top_distance, bottom_distance), 2)


def calculate_hypotenuse(distance_between_columns, height_difference):
    return (distance_between_columns ** 2 + height_difference ** 2) ** 0.5


def read_file(input_file):
    with open(input_file, 'r') as file:
        distance_between_columns = int(file.readline())
        max_columns_height = list(map(int, file.readline().strip().split(', ')))
        maximum_wire_length = max_wire_length(distance_between_columns, max_columns_height)

    return maximum_wire_length
