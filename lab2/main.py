from BST import BST
from Token import Scanner
from FA import FA

def show_menu():
    print("1. Show the set of states")
    print("2. Show the alphabet")
    print("3. Show the transition function")
    print("4. Show the initial state")
    print("5. Show the set of final states")
    print("6. Exit")

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

    '''
    fa = FA("fa_string_const.in")
    option = 0

    while True:
        show_menu()
        option = int(input("Please choose one option "))
        if option == 1:
            print(fa.get_set_of_states())
        elif option == 2:
            print(fa.get_alphabet())
        elif option == 3:
            print(fa.get_transition_function())
        elif option == 4:
            print(fa.get_initial_state())
        elif option == 5:
            print(fa.get_final_states())
        else:
            break
    '''
