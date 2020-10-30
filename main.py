from BST import BST
from Token import Scanner

if __name__ == '__main__':
    tokens = Scanner("p3.txt")
    error = tokens.tokenize()
    if not error:
        tokens.construct_pif()
        tokens.inorder()
        print(tokens.get_PIF())
        file = open("pif.txt", 'w')
        file.write(str(tokens.get_PIF()))
        file.close()
    else:
        print(str(tokens.get_error()))

