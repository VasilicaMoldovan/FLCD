from BST import BST

if __name__ == '__main__':
    bst = BST(["xbd", 1])
    bst = bst.insert(bst, ['a', 5])
    bst = bst.insert(bst, ["cf", 3])
    bst.inorder(bst)
    print(bst.get_position_by_name(bst, "xbd"))
    print(bst.get_position_by_id(bst, 5))

