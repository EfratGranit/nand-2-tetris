import os
from Parser import Parser, Command
from Code import Code
import ntpath
import sys


def zeros(address):
     code = Code()
     l = 16 - len(code.decimal_to_binary(address))
     z = ''
     for i in range(l):
         z = z.__add__('0')
     return z


def main():
    file_path, i = sys.argv[1], 1
    os.chdir(sys.path[0])
    new_path = open(ntpath.basename(file_path)[0:ntpath.basename(file_path).find('.')]+'.hack', 'w')
    code = Code()
    parser = Parser(file_path)
    parser.create_file_commands_only()  # create xxx.hack with all commands, without comments and blanklines

    while parser.has_more_commands():
        parser.advance()
        com_type = parser.command_type()
        if com_type == Command.L_COMMAND:
            parser.symbol()
    parser.restart()

    while parser.has_more_commands():
        parser.advance()
        com_type = parser.command_type()
        if com_type == Command.A_COMMAND:
            print(i, "A")
            address = parser.symbol()
            z = zeros(address)
            new_path.write(z + code.decimal_to_binary(address) + '\n')
        elif com_type == Command.L_COMMAND:
            print(i, "L")
        else:
            print(i, "C")
            new_path.write("111"+code.comp(parser.comp())+code.dest(parser.dest())+code.jump(parser.jump())+'\n')
        i += 1


if __name__ == '__main__':
    main()
