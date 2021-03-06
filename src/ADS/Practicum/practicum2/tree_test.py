import unittest

from src.ADS.Practicum.practicum2.tree import Tree


class TestTree(unittest.TestCase):
    def setUp(self):
        self.tree = Tree()

    def test_insert(self):
        # Add root node
        self.tree.insert(4)
        self.assertEqual(self.tree.root.key, 4)
        self.assertTrue(self.tree.root.is_root())
        self.assertTrue(self.tree.root.is_leaf())

        # Add some more nodes
        self.tree.insert(1)
        self.assertEquals(self.tree.root.left.key, 1)
        self.tree.insert(7)
        self.assertEquals(self.tree.root.right.key, 7)
        self.tree.insert(2)
        self.assertEquals(self.tree.root.left.right.key, 2)
        self.tree.insert(6)
        self.assertEquals(self.tree.root.right.left.key, 6)

    def test_rotate_left(self):
        sequence = [5, 3, 4, 2, 6]
        nodes = {}

        # Add nodes
        for key in sequence:
            self.tree.insert(key)
            nodes[key] = self.tree.search(key)

        # Rotate
        self.tree._rotate_left(self.tree.root)
        # print(self.tree.graphviz())

        # Check tree structure
        self.assertEquals(self.tree.root.key, 6)
        self.assertEquals(self.tree.root.left.key, 5)
        self.assertEquals(self.tree.root.left.left.key, 3)
        self.assertEquals(self.tree.root.left.left.left.key, 2)
        self.assertEquals(self.tree.root.left.left.right.key, 4)

        # Compare if rotation was done using pointers instead of value reassignment
        for key, node in nodes.items():
            self.assertEquals(self.tree.search(key), node)

    def test_rotate_left2(self):
        sequence = [5, 3, 4, 2, 6]
        nodes = {}

        # Add nodes
        for key in sequence:
            self.tree.insert(key)
            nodes[key] = self.tree.search(key)

        # Rotate
        self.tree._rotate_left(self.tree.root.left)
        # print(self.tree.graphviz())

        # Check tree structure
        self.assertEquals(self.tree.root.key, 5)
        self.assertEquals(self.tree.root.left.key, 4)
        self.assertEquals(self.tree.root.left.left.key, 3)
        self.assertEquals(self.tree.root.left.left.left.key, 2)
        self.assertEquals(self.tree.root.right.key, 6)

        # Compare if rotation was done using pointers instead of value reassignment
        for key, node in nodes.items():
            self.assertEquals(self.tree.search(key), node)

    def test_rotate_right(self):
        sequence = [5, 3, 2, 4, 6]
        nodes = {}
        # Add nodes
        for key in sequence:
            self.tree.insert(key)
            nodes[key] = self.tree.search(key)

        # Rotate
        self.tree._rotate_right(self.tree.root)
        # print(self.tree.graphviz())

        # Check tree structure
        self.assertEquals(self.tree.root.key, 3)
        self.assertEquals(self.tree.root.left.key, 2)
        self.assertEquals(self.tree.root.right.key, 5)
        self.assertEquals(self.tree.root.right.left.key, 4)
        self.assertEquals(self.tree.root.right.right.key, 6)

        self.assertEquals(self.tree.root.first().key, 2)
        self.assertEquals(self.tree.root.first().parent.key, 3)
        self.assertEquals(self.tree.root.last().parent.parent.key, 3)



        # Compare if rotation was done using pointers instead of value reassignment
        for key, node in nodes.items():
            self.assertEquals(self.tree.search(key), node)

    def test_rotate_right2(self):
        sequence = [5, 3, 2, 4, 6]
        nodes = {}
        # Add nodes
        for key in sequence:
            self.tree.insert(key)
            nodes[key] = self.tree.search(key)

        # Rotate
        self.tree._rotate_right(self.tree.root.left)
        # print(self.tree.graphviz())

        # Check tree structure
        self.assertEquals(self.tree.root.key, 5)
        self.assertEquals(self.tree.root.left.key, 2)
        self.assertEquals(self.tree.root.left.right.key, 3)
        self.assertEquals(self.tree.root.left.right.right.key, 4)
        self.assertEquals(self.tree.root.right.key, 6)

        self.assertEquals(self.tree.root.first().key, 2)
        self.assertEquals(self.tree.root.last().key, 6)

        # Compare if rotation was done using pointers instead of value reassignment
        for key, node in nodes.items():
            self.assertEquals(self.tree.search(key), node)


    def test_re_rotating(self):
        sequence = [13, 8, 10, 9, 6, 17, 19, 16]
        nodes = {}
        # Add nodes
        for key in sequence:
            self.tree.insert(key)
            nodes[key] = self.tree.search(key)

        # Rotate
        # print(self.tree.graphviz())
        self.tree._rotate_right(self.tree.root)
        self.tree._rotate_left(self.tree.root)
        self.tree._rotate_left(self.tree.root)
        self.tree._rotate_right(self.tree.root)
        # print(self.tree.graphviz())

        # Check tree structure
        self.assertEquals(self.tree.root.key, 13)
        self.assertEquals(self.tree.root.left.key, 8)
        self.assertEquals(self.tree.root.left.left.key, 6)
        self.assertEquals(self.tree.root.left.right.key, 10)
        self.assertEquals(self.tree.root.left.right.left.key, 9)
        self.assertEquals(self.tree.root.right.key, 17)
        self.assertEquals(self.tree.root.right.left.key, 16)
        self.assertEquals(self.tree.root.right.right.key, 19)



    # def test_balance(self):
    #     sequence = [7, 5, 8, 3, 6, 2, 4]
    #     nodes = {}
    #
    #     # Add nodes
    #     for key in sequence:
    #         self.tree.insert(key)
    #         nodes[key] = self.tree.search(key)
    #
    #     # Balance
    #     self.tree.balance()
    #
    #     # Check balanced
    #     def is_balanced(node):
    #         left = len(node.left) if node.left else 0
    #         right = len(node.right) if node.right else 0
    #         left_balanced = is_balanced(node.left) if node.left else True
    #         right_balanced = is_balanced(node.right) if node.right else True
    #         balanced = abs(left - right) <= 1
    #         return balanced and left_balanced and right_balanced
    #
    #     self.assertTrue(is_balanced(self.tree.root))

    def test_balance2(self):
        sequence = [20, 19, 24, 26, 27, 25]
        nodes = {}

        # Add nodes
        for key in sequence:
            self.tree.insert(key)
            nodes[key] = self.tree.search(key)

        # Balance
        print(self.tree.graphviz())
        self.tree.balance()
        print(self.tree.graphviz())

        # Check balanced
        def is_balanced(node):
            left = len(node.left) if node.left else 0
            right = len(node.right) if node.right else 0
            left_balanced = is_balanced(node.left) if node.left else True
            right_balanced = is_balanced(node.right) if node.right else True
            balanced = abs(left - right) <= 1
            return balanced and left_balanced and right_balanced

        self.assertTrue(is_balanced(self.tree.root))


