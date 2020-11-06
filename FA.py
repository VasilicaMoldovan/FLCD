import re

class FA:
    def __init__(self, filename):
        self.__states = []
        self.__alphabet = []
        self.__finalStates = []
        self.__initialState = []
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
        delimiters = "=", "{", "}"
        regexPattern = '|'.join(map(re.escape, delimiters))
        tokens = re.split(regexPattern, line)
        self.__initialState = tokens[2]

        line = file.readline().strip()
        #read the productions
        while line != "":
            delimiters = "-", ">"
            regexPattern = '|'.join(map(re.escape, delimiters))
            tokens = re.split(regexPattern, line)
            transitions = tokens[2].split("|")
            self.__transitions[transitions[0]] = []

            for transition in transitions:
                self.__transitions[transitions[0]].append(transition)

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