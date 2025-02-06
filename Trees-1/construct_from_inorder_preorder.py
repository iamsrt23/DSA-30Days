class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def build_tree(preorder, inorder):
    if not preorder or not inorder:
        return None

    # Root is the first element in preorder
    root_data = preorder[0]
    root = Node(root_data)

    # Find the index of the root in inorder
    root_index = inorder.index(root_data)

    # Build left and right subtrees
    root.left = build_tree(preorder[1:1 + root_index], inorder[:root_index])
    root.right = build_tree(preorder[1 + root_index:], inorder[root_index + 1:])

    return root


def print_inorder(root):
    if root:
        print_inorder(root.left)
        print(root.data, end=" ")
        print_inorder(root.right)


# Input
preorder = [10, 20, 40, 50, 30, 60]
inorder = [40, 20, 50, 10, 30, 60]

# Build the binary tree
root = build_tree(preorder, inorder)

# Print the inorder traversal of the constructed tree
print("Inorder traversal of the constructed tree:")
print_inorder(root)