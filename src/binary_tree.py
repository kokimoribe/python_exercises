# Setup
class TreeNode:
    """A basic binary tree node."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def create_tree(values):
    """Helper function to create a binary tree from a list of values.
    None values represent empty nodes.
    Example: [1, 2, 3, None, 4] creates:
         1
        / \
       2   3
        \
         4
    """
    if not values:
        return None
    
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root

#################################################
# Pre-order Traversal
#################################################

def preorder_traversal(root):
    """
    Implement a function that performs a pre-order traversal of a binary tree
    and returns the values in a list.
    
    Pre-order traversal visits nodes in this order:
    1. Node (N)
    2. Left subtree (L)
    3. Right subtree (R)
    
    Example:
        Input tree:
             1
            / \
           2   3
            \
             4
        
        Output: [1, 2, 4, 3]
    
    Args:
        root: The root node of the binary tree
        
    Returns:
        list: A list of values in pre-order traversal order
    """
    pass

def test_preorder_traversal():
    # Test case 1: Basic tree
    tree1 = create_tree([1, 2, 3, None, 4])
    assert preorder_traversal(tree1) == [1, 2, 4, 3]
    
    # Test case 2: Empty tree
    assert preorder_traversal(None) == []
    
    # Test case 3: Single node
    assert preorder_traversal(TreeNode(1)) == [1]
    
    # Test case 4: Full binary tree
    tree2 = create_tree([1, 2, 3, 4, 5, 6, 7])
    assert preorder_traversal(tree2) == [1, 2, 4, 5, 3, 6, 7]
