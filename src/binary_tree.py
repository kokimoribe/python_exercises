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

# EXERCISE: Pre-order Traversal (Recursive)
def preorder_traversal(root):
    """
    Implement a recursive function that performs a pre-order traversal of a binary tree
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

# EXERCISE: Pre-order Traversal (Iterative)
def preorder_traversal_iter(root):
    """
    Implement an iterative function that performs a pre-order traversal of a binary tree
    using a stack (no recursion allowed).
    
    Pre-order traversal visits nodes in this order:
    1. Node (N)
    2. Left subtree (L)
    3. Right subtree (R)
    
    Hint: Use a stack to keep track of nodes to visit. Remember that with a stack,
    you'll need to push the right child before the left child.
    
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

def test_preorder_traversal_iter():
    # Test case 1: Basic tree
    tree1 = create_tree([1, 2, 3, None, 4])
    assert preorder_traversal_iter(tree1) == [1, 2, 4, 3]
    
    # Test case 2: Empty tree
    assert preorder_traversal_iter(None) == []
    
    # Test case 3: Single node
    assert preorder_traversal_iter(TreeNode(1)) == [1]
    
    # Test case 4: Full binary tree
    tree2 = create_tree([1, 2, 3, 4, 5, 6, 7])
    assert preorder_traversal_iter(tree2) == [1, 2, 4, 5, 3, 6, 7]

# EXERCISE: In-order Traversal (Recursive)
def inorder_traversal(root):
    """
    Implement a recursive function that performs an in-order traversal of a binary tree
    and returns the values in a list.
    
    In-order traversal visits nodes in this order:
    1. Left subtree (L)
    2. Node (N)
    3. Right subtree (R)
    
    Example:
        Input tree:
             1
            / \
           2   3
            \
             4
        
        Output: [2, 4, 1, 3]
    
    Args:
        root: The root node of the binary tree
        
    Returns:
        list: A list of values in in-order traversal order
    """
    pass

def test_inorder_traversal():
    # Test case 1: Basic tree
    tree1 = create_tree([1, 2, 3, None, 4])
    assert inorder_traversal(tree1) == [2, 4, 1, 3]
    
    # Test case 2: Empty tree
    assert inorder_traversal(None) == []
    
    # Test case 3: Single node
    assert inorder_traversal(TreeNode(1)) == [1]
    
    # Test case 4: Full binary tree
    tree2 = create_tree([1, 2, 3, 4, 5, 6, 7])
    assert inorder_traversal(tree2) == [4, 2, 5, 1, 6, 3, 7]

# EXERCISE: In-order Traversal (Iterative)
def inorder_traversal_iter(root):
    """
    Implement an iterative function that performs an in-order traversal of a binary tree
    using a stack (no recursion allowed).
    
    In-order traversal visits nodes in this order:
    1. Left subtree (L)
    2. Node (N)
    3. Right subtree (R)
    
    Hint: Use a stack and keep traversing left until you can't. Then pop from the stack
    and process the right subtree.
    
    Example:
        Input tree:
             1
            / \
           2   3
            \
             4
        
        Output: [2, 4, 1, 3]
    
    Args:
        root: The root node of the binary tree
        
    Returns:
        list: A list of values in in-order traversal order
    """
    pass

def test_inorder_traversal_iter():
    # Test case 1: Basic tree
    tree1 = create_tree([1, 2, 3, None, 4])
    assert inorder_traversal_iter(tree1) == [2, 4, 1, 3]
    
    # Test case 2: Empty tree
    assert inorder_traversal_iter(None) == []
    
    # Test case 3: Single node
    assert inorder_traversal_iter(TreeNode(1)) == [1]
    
    # Test case 4: Full binary tree
    tree2 = create_tree([1, 2, 3, 4, 5, 6, 7])
    assert inorder_traversal_iter(tree2) == [4, 2, 5, 1, 6, 3, 7]

# EXERCISE: Post-order Traversal (Recursive)
def postorder_traversal(root):
    """
    Implement a recursive function that performs a post-order traversal of a binary tree
    and returns the values in a list.
    
    Post-order traversal visits nodes in this order:
    1. Left subtree (L)
    2. Right subtree (R)
    3. Node (N)
    
    Example:
        Input tree:
             1
            / \
           2   3
            \
             4
        
        Output: [4, 2, 3, 1]
    
    Args:
        root: The root node of the binary tree
        
    Returns:
        list: A list of values in post-order traversal order
    """
    pass

def test_postorder_traversal():
    # Test case 1: Basic tree
    tree1 = create_tree([1, 2, 3, None, 4])
    assert postorder_traversal(tree1) == [4, 2, 3, 1]
    
    # Test case 2: Empty tree
    assert postorder_traversal(None) == []
    
    # Test case 3: Single node
    assert postorder_traversal(TreeNode(1)) == [1]
    
    # Test case 4: Full binary tree
    tree2 = create_tree([1, 2, 3, 4, 5, 6, 7])
    assert postorder_traversal(tree2) == [4, 5, 2, 6, 7, 3, 1]

# EXERCISE: Post-order Traversal (Iterative)
def postorder_traversal_iter(root):
    """
    Implement an iterative function that performs a post-order traversal of a binary tree
    using a stack (no recursion allowed).
    
    Post-order traversal visits nodes in this order:
    1. Left subtree (L)
    2. Right subtree (R)
    3. Node (N)
    
    Hint: This is the trickiest traversal to do iteratively. Consider using two stacks
    or keeping track of the last visited node.
    
    Example:
        Input tree:
             1
            / \
           2   3
            \
             4
        
        Output: [4, 2, 3, 1]
    
    Args:
        root: The root node of the binary tree
        
    Returns:
        list: A list of values in post-order traversal order
    """
    pass

def test_postorder_traversal_iter():
    # Test case 1: Basic tree
    tree1 = create_tree([1, 2, 3, None, 4])
    assert postorder_traversal_iter(tree1) == [4, 2, 3, 1]
    
    # Test case 2: Empty tree
    assert postorder_traversal_iter(None) == []
    
    # Test case 3: Single node
    assert postorder_traversal_iter(TreeNode(1)) == [1]
    
    # Test case 4: Full binary tree
    tree2 = create_tree([1, 2, 3, 4, 5, 6, 7])
    assert postorder_traversal_iter(tree2) == [4, 5, 2, 6, 7, 3, 1]

# EXERCISE: Level-order Traversal
def levelorder_traversal(root):
    """
    Implement a function that performs a level-order (breadth-first) traversal of a binary tree
    and returns the values in a list.
    
    Level-order traversal visits nodes level by level, from left to right.
    
    Hint: Use a queue to keep track of nodes to visit.
    
    Example:
        Input tree:
             1
            / \
           2   3
            \
             4
        
        Output: [1, 2, 3, 4]
    
    Args:
        root: The root node of the binary tree
        
    Returns:
        list: A list of values in level-order traversal order
    """
    pass

def test_levelorder_traversal():
    # Test case 1: Basic tree
    tree1 = create_tree([1, 2, 3, None, 4])
    assert levelorder_traversal(tree1) == [1, 2, 3, 4]
    
    # Test case 2: Empty tree
    assert levelorder_traversal(None) == []
    
    # Test case 3: Single node
    assert levelorder_traversal(TreeNode(1)) == [1]
    
    # Test case 4: Full binary tree
    tree2 = create_tree([1, 2, 3, 4, 5, 6, 7])
    assert levelorder_traversal(tree2) == [1, 2, 3, 4, 5, 6, 7]
