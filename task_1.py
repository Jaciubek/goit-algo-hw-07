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

# Function to find the max value in a BST
def find_max_value(root):
    current = root
    while current.right is not None:
        current = current.right
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
    
    # Find and print the largest value in the BST
    max_value = find_max_value(root)
    print(f"The max value in the BST(tree) is: {max_value}")