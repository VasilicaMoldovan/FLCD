class BST:
    """
    info - an identifier/constant
    Complexity: Theta(1)
    """
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None

    """
    Preconditions:
        root - a binary search tree
        info - searched identifier/constant
    Postcondition:
        pos - an integer which is 
                - -1 if the identifier/constant is not in the bst
                - the position of the identifier/constant in the bst
        Complexity: O(h), where h is the height of the binary tree 
    """
    def get_position_by_name(self, root, info):
        pos = 0
        pos = self.search(root, info, pos)
        return pos

    """
        Preconditions:
            root - a binary search tree
            info - searched identifier/constant
        Postcondition:
            pos - an integer which is 
                    - -1 if the identifier/constant is not in the bst
                    - the position of the identifier/constant in the bst
            Complexity: O(n ^ 2)
        """
    def get_position_by_id(self, root, info):
        pos = 0
        pos = self.search_position_by_id(root, info, pos)
        return pos


    """
    Preconditions:
        root - a binary search tree
        info - searched identifier/constant
        position - the position from which we start looking for info
    Postcondition:
        returns - an integer which is 
                - -1 if the identifier/constant is not in the bst
                - the position of the identifier/constant in the bst
        Complexity: O(n ^ 2)
    """
    def search_position_by_id(self, root, info, position):
        h = self.height(root)
        pos = 0
        for i in range(1, h + 1):
            aux = self.search_one_level(root, i, info)
            if aux != None:
                return pos
            else:
                pos += 1
        return -1

    """
    Preconditions:
        root - a binary search tree
        info - searched identifier/constant
        position - the position from which we start looking for info
    Postcondition:
        returns - an integer which is 
                - None if the identifier/constant id is not in the bst
                - the position of the identifier/constant id in the bst
    """
    def search_one_level(self, root, level, info):
        if root is None:
            return None
        if level == 1:
            if root.info[1] == info:
                return root.info
            else:
                return None
        elif level > 1:
            aux = self.search_one_level(root.left, level - 1, info)
            if aux[1] == info:
                return aux
            else:
                return self.search_one_level(root.right, level - 1, info)

    def height(self, node):
        if node is None:
            return 0
        else:
            left_height = self.height(node.left)
            right_height = self.height(node.right)

            if left_height > right_height:
                return left_height + 1
            else:
                return right_height + 1

    """
    Preconditions:
        root - a binary search tree
        info - searched identifier/constant
        position - the position from which we start looking for info
    Postcondition:
        returns - an integer which is 
                - -1 if the identifier/constant is not in the bst
                - the position of the identifier/constant in the bst
        Complexity: O(h), where h is the height of the binary tree
    """
    def search(self, root, info, position):
        if root == None:
            return -1

        if root.info[0] == info:
            return position

        if root.info[0] < info[0]:
            return self.search(root.right, info, position + 1)
        return self.search(root.left, info, position + 1)

    """
    Preconditions:
        root - a binary search tree
        info - the identifier/constant we want to insert
    Postcondition:
        returns the new inserted node or an existing node, if info 
        was already in the binary search table
    Complexity: O(h), where h is the height of the binary tree
    """
    def insert(self, root, info):
        if root == None:
            return BST(info)
        if root.info[0] == info[0]:
            return root
        if root.info[0] < info[0]:
            root.right = self.insert(root.right, info)
        else:
            root.left = self.insert(root.left, info)

        return root

    """
   Preconditions:
       root - a binary search tree
   Complexity: O(n)
   """
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.info)
            self.inorder(root.right)