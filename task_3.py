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

# Function to find the sum of all values in the BST
def find_sum_of_values(root):
    if root is None:
        return 0
    return root.val + find_sum_of_values(root.left) + find_sum_of_values(root.right)


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
    
    # Find and print the sum of all values in the BST
    total_sum = find_sum_of_values(root)
    print(f"The sum of all values in the BST(tree) is: {total_sum}")