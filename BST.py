class BST:
    """
    info - an identifier/constant
    Complexity: Theta(1)
    """
    def __init__(self, info):
        self.__info = info
        self.__left = None
        self.__right = None

    def get_info(self):
        return self.__info

    def get_left(self):
        return self.__left

    def get_right(self):
        return self.__right

    def set_info(self, info):
         self.__info = info

    def set_left(self, left):
        self.__left = left

    def set_right(self, right):
        self.__right = right

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
        returns - None if the identifier/constant id is not in the bst
                - identifier/constant id in the bst
    """
    def search_one_level(self, root, level, info):
        if root is None:
            return None
        if level == 1:
            if root.get_info()[1] == info:
                return root.get_info()
            else:
                return None
        elif level > 1:
            aux = self.search_one_level(root.get_left(), level - 1, info)
            if aux[1] == info:
                return aux
            else:
                return self.search_one_level(root.get_right(), level - 1, info)

    """
    Preconditions: 
    node - the start node
    Postconditions:
    height - the height of the tree starting from node
    """
    def height(self, node):
        if node is None:
            return 0
        else:
            left_height = self.height(node.get_left())
            right_height = self.height(node.get_right())

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

        if root.get_info()[0] == info:
            return position

        if root.get_info()[0] < info[0]:
            return self.search(root.get_right(), info, position + 1)
        return self.search(root.get_left(), info, position + 1)

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
        if root.get_info()[0] == info[0]:
            return root
        if root.get_info()[0] < info[0]:
            root.set_right(self.insert(root.get_right(), info))
        else:
            root.set_left(self.insert(root.get_left(), info))

        return root

    """
   Preconditions:
       root - a binary search tree
   Complexity: O(n)
   """
    def inorder(self, root):
        if root:
            self.inorder(root.get_left())
            print(root.get_info())
            self.inorder(root.get_right())