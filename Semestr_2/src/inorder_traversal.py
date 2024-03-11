class Node:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def find_successor(root, element_to_found):
    def inorder_traversal(root, array):
        if root is not None:
            inorder_traversal(root.left, array)
            array.append(root.value)
            inorder_traversal(root.right, array)

        return array

    array = []
    sorted_arr_by_inorder_traversal = inorder_traversal(root, array)
    print(sorted_arr_by_inorder_traversal)
    index = sorted_arr_by_inorder_traversal.index(element_to_found.value)
    for i in range(1, len(sorted_arr_by_inorder_traversal)):
        if index + i > len(sorted_arr_by_inorder_traversal) - 1:
            return False
        elif sorted_arr_by_inorder_traversal[index + i] > sorted_arr_by_inorder_traversal[index]:
            return sorted_arr_by_inorder_traversal[index + i]
        elif sorted_arr_by_inorder_traversal[index - i] > sorted_arr_by_inorder_traversal[index]:
            return sorted_arr_by_inorder_traversal[index - i]


root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.right = Node(7)
root.left.left = Node(3)
root.right.right = Node(20)
root.right.right.left = Node(12)

element_to_found = root.right
print(find_successor(root, element_to_found))
