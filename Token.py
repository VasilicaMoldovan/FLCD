from BST import BST
import re

class Scanner:
    def __init__(self, filename):
        self.__tokens = {}
        self.__codes = {}
        self.__filename = filename
        self.__ST = BST(["", -1])
        self.__PIF = {}
        self.__reserved_words = ["individual", "decision","char","float","const","parsing","situation","other","come","leave", "return","break"]
        self.generate_codes()
        self.tokenize()
        self.construct_pif()

    def get_tokens(self):
        return self.__tokens

    '''
    Preconditions: None
    Postconditions: This function reads token.in and stores 
    the the tokens and their associated code
    '''
    def generate_codes(self):
        file = open("token.txt", 'r')
        line = file.readline().strip("\n")
        while line != "":
            codes = line.split(",")
            self.__tokens[codes[0]] = int(codes[1])
            line = file.readline().strip("\n")

    '''
    Preconditions: identifier - a string
    Postconditions: returns True if the given string respects the 
                    criterias for a valid identifier, or False
                    otherwise
    '''
    def is_identifier(self, identifier):
        letters = list(identifier)
        if letters[0].isnumeric():
            return False
        return True

    '''
    Preconditions: constant - a string
    Postconditions: returns True if the given string respects the 
                    criterias for a valid constant, or False
                    otherwise
    '''
    def is_constant(self, constant):
        letters = list(constant)

        if letters[0] == '0' and len(letters) > 1:
            return False
        elif letters[0] in ['+', '-'] and len(letters) > 1 and letters[1] == '0':
            return False
        else:
            return True

    '''
    Preconditions: word - a string
    Postconditions: returns True if the given string is a 
                    reserved word, or False otherwise
    '''
    def is_reserverd_word(self, word):
        if word in self.__reserved_words:
            return True
        return False

    def get_symbol_table(self):
        return self.__ST

    '''
    Preconditions: None
    Postconditions: Function which detects and classifies the tokens, 
    reading them from a given file. It also constructs the Symbol Table 
    and checks if there are lexical errors in the program. 
    '''
    def tokenize(self):
        file = open(self.__filename, 'r')
        line = file.readline().strip("\n")
        count_line = 1
        first = True
        while line != "":
            delimiters = ";", " ", ",", "[", "]", "{", "}", "(", ")", ":", "'", '"', "+", "-", "*", "/", "=", "<", ">", "&&", "||", "!=", "==", "<=", ">="
            regexPattern = '|'.join(map(re.escape, delimiters))
            tokens = re.split(regexPattern, line)

            if tokens[0] != None and tokens[0] != "{" and len(tokens[0]) > 0:
                if tokens[0] not in self.__tokens.keys() and not self.is_identifier(tokens[0]) and not self.is_reserverd_word(tokens[0]):
                    raise Exception("Invalid identifier at line " + str(count_line))
            for i in range (1, len(tokens)):
                current_error = ""
                if tokens[i] is not None and len(tokens[i]) > 0 and tokens[i] != "{":
                    if not self.is_identifier(tokens[i]):
                        current_error = "invalid identifier"
                    else:
                        if not self.is_constant(tokens[i]):
                            if self.is_reserverd_word(tokens[i]):
                                current_error = ""
                        else:
                            current_error = ""
                    if current_error != "":
                        raise Exception(current_error + " at line " + str(count_line))
                    if first == True:
                        if self.is_identifier(tokens[i]):
                            self.__ST.set_info([tokens[i], self.__tokens['identifier']])
                        else:
                            self.__ST.set_info([tokens[i], self.__tokens['constant']])
                        first = False
                    else:
                        if self.is_identifier(tokens[i]):
                            self.__ST.insert(self.__ST, [tokens[i], self.__tokens['identifier']])
                        else:
                            self.__ST.insert(self.__ST, [tokens[i], self.__tokens['constant']])
                count_line += 1

            line = file.readline().strip("\n")
        file.close()

    '''
    Preconditions: None
    Postconditions: Function which constructs PIF for a given program.
    The PIF is stored as a dictionary, which has as key the token, and 
    as value its positions in the symbol table if it's an identifier or constant, 
    or -1 otherwise.
    '''
    def construct_pif(self):
        file = open(self.__filename, 'r')
        line = file.readline().strip("\n")
        while line != "":
            delimiters = ";", ",", "[", "]", "{", "}", "(", ")", ":", "'", '"', "+", "-", "*", "/", "=", "<", ">", "&&", "||", "!=", "==", "<=", ">=", " "
            regexPattern = '|'.join(map(re.escape, delimiters))
            tokens = re.split(regexPattern, line)

            for i in range(0, len(tokens)):
                if tokens[i] is not None and len(tokens[i]) > 0:
                    self.__PIF[tokens[i]] = self.__ST.get_position_by_name(self.__ST, tokens[i])

            line = file.readline().strip("\n")
        file.close()

    def inorder(self):
        self.__ST.inorder(self.__ST)

    def get_PIF(self):
        return self.__PIF