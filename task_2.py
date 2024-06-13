# Define the node class
class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# Function to insert a new node with the given key
def insert(root, key):
    if root is None:
        return TreeNode(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

# Function to find the min value in a BST
def find_min_value(root):
    current = root
    while current.left is not None:
        current = current.left
    return current.val

# Main code to test the functions
if __name__ == "__main__":
    # Create the root of the tree
    root = TreeNode(10)
    # Insert nodes into the BST
    root = insert(root, 6)
    root = insert(root, 4)
    root = insert(root, 8)
    root = insert(root, 14)
    root = insert(root, 12)
    root = insert(root, 16)
    
    # Find and print the smallest value in the BST
    min_value = find_min_value(root)
    print(f"The min value in the BST(tree) is: {min_value}")