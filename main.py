from BST import BST
from Token import Scanner

if __name__ == '__main__':
    bst = BST(["xbd", 1])
    bst = bst.insert(bst, ['a', 29])
    bst = bst.insert(bst, ["cf", 3])
    bst.inorder(bst)
    print(bst.get_position_by_name(bst, "xbd"))
    print(bst.get_position_by_id(bst, 29))
    tokens = Scanner("p1.txt")
    tokens.inorder()
    print(tokens.get_PIF())
    #print(tokens.get_tokens())

