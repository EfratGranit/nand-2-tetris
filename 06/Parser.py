from enum import Enum
from Symbole_table import SymbolTable

class Command(Enum):
    A_COMMAND = 1
    C_COMMAND = 2
    L_COMMAND = 3


class Parser:

    def __init__(self, file_path):
        # slices the file name from file_path
        # new_file_path = file_path[::-1][0:file_path[::-1].find('/')][::-1] if file_path.find('/') != -1 else file_path
        # self.__new_file_path = new_file_path = new_file_path[0:new_file_path.find('.')]+'.hack'  # replace .asm at .hack
        self.__file_path = file_path
        self.__current_command = None
        self.__symbol_table = SymbolTable()
        self.__current_line = 0
        self.__save_num_lables = 0

    def restart(self):
        self.__current_command = None
        self.__current_line = 0
        self.__file_path.seek(0)

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

    def command_type(self):
        if self.__current_command.find("@") == -1:
            if self.__current_command.find("(") == -1:
                return Command.C_COMMAND
            else:
                return Command.L_COMMAND
        else:
            return Command.A_COMMAND

    def advance(self):
        self.__current_command = self.__file_path.readline()
        self.__current_line += 1
        return self.__current_command

    def symbol(self):
        if self.__current_command.find("@") == -1:
            symbol = self.__current_command[1:-2]
            address = (self.__current_line - 1 - self.__save_num_lables)
            self.__symbol_table.add_label_symbol(str(symbol), address)
            self.__save_num_lables += 1

        else:
            if not ((self.__current_command[1:-1]).isnumeric()):
                symbol = self.__current_command[1:-1].strip(' ')
                self.__symbol_table.add_variable_symbol(symbol)
            else:
                return int(self.__current_command[1:-1])
        return int(self.__symbol_table.get_address(symbol))

    def comp(self):
        cur = self.__current_command
        cur = cur[cur.find('=')+1:] if cur.find('=') != -1 else cur
        cur = cur[:cur.find(';')].strip() if cur.find(';') != -1 else cur.strip()
        return cur

    def dest(self):
        cur = self.__current_command
        cur = cur[:cur.find('=')].strip() if cur.find('=') != -1 else ''
        return cur

    def jump(self):
        cur = self.__current_command
        cur = cur[cur.find(';')+1:].strip() if cur.find('J') != -1 else ''
        return cur

