import unittest
from inorder_traversal import find_successor
from inorder_traversal import Node


class TestOfInorderTraversal(unittest.TestCase):
    def test_1(self):
        root = Node(10)
        root.left = Node(5)
        root.right = Node(15)
        root.left.right = Node(7)
        root.left.left = Node(3)
        root.right.right = Node(20)
        root.right.right.left = Node(12)

        element_to_found = root.right

        expected_result = 20
        self.assertEqual(find_successor(root, element_to_found), expected_result)

    def test_2(self):
        root = Node(10)
        root.left = Node(5)
        root.right = Node(15)
        root.left.right = Node(7)
        root.left.left = Node(3)
        root.right.right = Node(20)
        root.right.right.left = Node(12)

        element_to_found = root.right

        expected_result = 20
        self.assertEqual(find_successor(root, element_to_found), expected_result)

    def test_3(self):
        root = Node(10)
        root.left = Node(5)
        root.right = Node(15)
        root.left.right = Node(7)
        root.left.left = Node(3)
        root.right.right = Node(20)
        root.right.right.left = Node(12)

        element_to_found = root.right

        expected_result = 20
        self.assertEqual(find_successor(root, element_to_found), expected_result)
