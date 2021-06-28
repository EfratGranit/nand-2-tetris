from enum import Enum


class Command(Enum):
    C_ARITHMETIC = 1
    C_PUSH = 2
    C_POP = 3
    C_LABEL = 4
    C_GOTO = 5
    C_IF = 6
    C_FUNCTION = 7
    C_RETURN = 8
    C_CALL = 9


class Parser:

    def __init__(self, file_path):
        self.__segment = ["local", "argument", "this", "that", "constant", "static", "temp", "pointer"]
        self.__arith_words = ["add", "sub", "neg", "eq", "gt", "lt", "or", "and", "not"]
        self.__file_path = file_path
        self.__current_command = None

    # remove the comments and blank lines or redundant spaces
    def create_file_commands_only(self):
        # remove the comments
        lines = open(self.__file_path, mode="r").readlines()
        open(self.__file_path, mode="w").writelines(line[0:line.find('//')]+'\n' if line.find('//') != -1 else line for line in lines)

        # removes the blank lines
        lines = open(self.__file_path, 'r').readlines()
        open(self.__file_path, mode="w").writelines(line.strip(' ') for line in lines if line.strip())

        # removes the \n at end of file if exist
        lines = open(self.__file_path, 'r').readlines()
        lines[-1] = lines[-1].strip('\n') if lines[-1].find('\n') != -1 else lines[-1]
        open(self.__file_path, 'w').writelines(lines)
        self.__file_path = open(self.__file_path, 'r+')  # opens the file for second reading

    def has_more_commands(self):
        offset = self.__file_path.tell()
        if self.__file_path.readline():
            # returns the cursor to the previous line - to keep legality
            # at next read command
            self.__file_path.seek(offset)
            return True
        return False

    def __find_arith(self):
        for word in self.__arith_words:
            if self.__current_command.find(word) != -1:
                return True
        return False

    def command_type(self):
        if self.__find_arith():
            return Command.C_ARITHMETIC
        elif self.__current_command.find("push") != -1:
            return Command.C_PUSH
        elif self.__current_command.find("pop") != -1:
            return Command.C_POP
        elif self.__current_command.find("label") != -1:
            return Command.C_LABEL
        elif self.__current_command.find("goto") != -1:
            return Command.C_GOTO
        elif self.__current_command.find("if-goto") != -1:
            return Command.C_IF
        elif self.__current_command.find("function") != -1:
            return Command.C_FUNCTION
        elif self.__current_command.find("call") != -1:
            return Command.C_CALL
        else:
            return Command.C_RETURN

    def advance(self):
        self.__current_command = self.__file_path.readline()

    def arg1(self):
        if self.command_type() == Command.C_ARITHMETIC:
            print(self.__current_command.split('\n')[0])
            return self.__current_command.split('\n')[0]
        for word in self.__segment:
            if self.__current_command.find(word) != -1:
                return word

    def arg2(self):
        int_to_ret = [int(s) for s in self.__current_command.split() if s.isdigit()]
        return int_to_ret[0]

