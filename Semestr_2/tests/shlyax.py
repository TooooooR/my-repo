field = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]


def find_way_robot(arr):
    list_2 = []
    way_robot = []
    strings = len(arr)
    columns = len(arr[0])
    for i in range(columns):
        for j in range(strings):
            list_2.append(arr[-(j + 1)][-(i + 1)])
        if i % 2 != 0:
            list_2.reverse()
        way_robot.extend(list_2)
        list_2 = []

    return way_robot


print(find_way_robot(field))