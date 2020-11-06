import re

class FA:
    def __init__(self, filename):
        self.__states = []
        self.__alphabet = []
        self.__finalStates = []
        self.__initialState = None
        self.__transitions = {}
        self.readFromFile(filename)

    def readFromFile(self, filename):
        file = open(filename, 'r')
        line = file.readline().strip()

        #read the states of the FA
        delimiters = "=", "{", "}"
        regexPattern = '|'.join(map(re.escape, delimiters))
        tokens = re.split(regexPattern, line)
        states = tokens[2].split(",")

        for state in states:
            self.__states.append(state)

        line = file.readline().strip()
        #read the alphabet of the FA
        delimiters = "=", "{", "}"
        regexPattern = '|'.join(map(re.escape, delimiters))
        tokens = re.split(regexPattern, line)
        alphabet = tokens[2].split(",")

        for alpha in alphabet:
            self.__alphabet.append(alpha)

        line = file.readline().strip()
        #read final states of the FA
        delimiters = "=", "{", "}"
        regexPattern = '|'.join(map(re.escape, delimiters))
        tokens = re.split(regexPattern, line)
        final_states = tokens[2].split(",")

        for state in final_states:
            self.__finalStates.append(state)

        line = file.readline().strip()
        #read initial state
        token = line.split("=")
        self.__initialState = token[1]

        line = file.readline().strip()
        #read the transitions
        while line != "":
            delimiters = "(", "=", ")"
            regexPattern = '|'.join(map(re.escape, delimiters))
            tokens = re.split(regexPattern, line)
            key = tokens[1].split(",")
            key1 = (key[0], key[1])

            if key1 not in self.__transitions.keys():
                self.__transitions[key1] = [tokens[3]]
            else:
                self.__transitions[key1].append(tokens[3])

            line = file.readline().strip()

    def get_set_of_states(self):
        return self.__states

    def get_alphabet(self):
        return self.__alphabet

    def get_final_states(self):
        return self.__finalStates

    def get_initial_state(self):
        return self.__initialState

    def get_transition_function(self):
        return self.__transitions