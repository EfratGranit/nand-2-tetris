from Parser import Parser, Command
from CodeWriter import CodeWriter
import sys


def main():
    file_path, i = sys.argv[1], 1
    # new_path = open(sys.argv[1][:sys.argv[1].find('.')]+'.asm', 'w')
    parser = Parser(file_path)
    parser.create_file_commands_only()  # create xxx.vm with all commands, without comments and blanklines
    code_writer = CodeWriter(sys.argv[1][:sys.argv[1].find('.')]+'.asm')

    while parser.has_more_commands():
        parser.advance()
        com_type = parser.command_type()
        if com_type == Command.C_ARITHMETIC:
            code_writer.write_arithmetic(parser.arg1())
            print(i, "ARITHMETIC")
        elif com_type == Command.C_PUSH:
            code_writer.write_push_pop(Command.C_PUSH, parser.arg1(), parser.arg2())
            print(i, "PUSH")
        elif com_type == Command.C_POP:
            print(i, "POP")
            code_writer.write_push_pop(Command.C_POP, parser.arg1(), parser.arg2())
        elif com_type == Command.C_LABEL:
            print(i, "LABEL")
        elif com_type == Command.C_GOTO:
            print(i, "GOTO")
        elif com_type == Command.C_IF:
            print(i, "IF")
        elif com_type == Command.C_FUNCTION:
            print(i, "FUNCTION")
        elif com_type == Command.C_RETURN:
            print(i, "RETURN")
        else:
            print(i, "CALL")
        i += 1


if __name__ == '__main__':
    main()
