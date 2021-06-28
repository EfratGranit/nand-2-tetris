from Parser import Command


class CodeWriter:
    def __init__(self, file_path):
        self.__file_path = open(file_path, 'w')
        self.__file_path.write("@256\nD=A\n@SP\nM=D\n")
        self.__num = 0

    def write_arithmetic(self, string):
        if string == "add":
            # +
            self.__file_path.write("@SP\nAM=M-1\nD=M\nM=0\n@SP\nA=M-1\nM=D+M\n")
        elif string == "sub":
            # -
            self.__file_path.write("@SP\nAM=M-1\nD=M\nM=0\n@SP\nA=M-1\nM=M-D\n")
        elif string == "neg":
            # !=
            self.__file_path.write("@SP\nA=M-1\nM=-M\n")
        elif string == "eq" or string == "gt" or string == "lt":
            # = or < or >
            if string == "eq":
                type_jump = "JEQ"
            elif string == "gt":
                type_jump = "JGT"
            elif string == "lt":
                type_jump = "JLT"

            self.__file_path.write(
                "@SP\nAM=M-1\nD=M\nM=0\n@SP\nA=M-1\nD=M-D\n@TRUE_"+str(self.__num)+"\nD;"+type_jump+"\n@FALSE_"+str(self.__num)+"\n0;JMP\n(" \
                "TRUE_"+str(self.__num)+")\n@SP\nA=M-1\nM=-1\n@CONTINUE_"+str(self.__num)+"\n0;JMP\n(FALSE_"+str(self.__num)+")\n@SP\nA=M-1\nM=" \
                "0\n@CONTINUE_"+str(self.__num)+"\n0;JMP\n(CONTINUE_"+str(self.__num)+")\n")
            self.__num += 1
        elif string == "or":
            # or
            self.__file_path.write("@SP\nAM=M-1\nD=M\nM=0\n@SP\nA=M-1\nM=D|M\n")
        elif string == "and":
            # and
            self.__file_path.write("@SP\nAM=M-1\nD=M\nM=0\n@SP\nA=M-1\nM=D&M\n")
        elif string == "not":
            # not
            self.__file_path.write("@SP\nA=M-1\nM=!M\n")

    def write_push_pop(self, com_type, segment, index):
        if com_type == Command.C_PUSH:
            if segment == "local":
                self.__file_path.write("@" + str(index) + "\nD=A\n@LCL\nA=M+D\nD=M\n@SP\nM=M+1\nA=M-1\nM=D\n")
            elif segment == "argument":
                self.__file_path.write("@" + str(index) + "\nD=A\n@ARG\nA=M+D\nD=M\n@SP\nM=M+1\nA=M-1\nM=D\n")
            elif segment == "this":
                self.__file_path.write("@" + str(index) + "\nD=A\n@THIS\nA=M+D\nD=M\n@SP\nM=M+1\nA=M-1\nM=D\n")
            elif segment == "that":
                self.__file_path.write("@" + str(index) + "\nD=A\n@THAT\nA=M+D\nD=M\n@SP\nM=M+1\nA=M-1\nM=D\n")
            elif segment == "constant":
                self.__file_path.write("@" + str(index) + "\nD=A\n@SP\nM=M+1\nA=M-1\nM=D\n")
            elif segment == "static":
                # push static index
                self.__file_path.write("@static_" + str(index) + "\nD=M\n@SP\nM=M+1\nA=M-1\nM=D\n")
            elif segment == "pointer":
                if index:
                    # push pointer 1
                    self.__file_path.write("@4\nD=M\n@SP\nM=M+1\nA=M-1\nM=D\n")
                else:
                    # push pointer 0
                    self.__file_path.write("@3\nD=M\n@SP\nM=M+1\nA=M-1\nM=D\n")
            elif segment == "temp":
                # push temp index
                self.__file_path.write("@" + str(int(index + 5)) + "\nD=M\n@SP\nM=M+1\nA=M-1\nM=D\n")
        else:
            if segment == "local":
                # pop local index
                self.__file_path.write(
                    "@" + str(index) + "\nD=A\n@LCL\nD=D+M\n@R13\nM=D\n@SP\nAM=M-1\nD=M\nM=0\n@R13\nA=M\nM=D\n")
            elif segment == "argument":
                # pop argument index
                self.__file_path.write(
                    "@" + str(index) + "\nD=A\n@ARG\nD=D+M\n@R13\nM=D\n@SP\nAM=M-1\nD=M\nM=0\n@R13\nA=M\nM=D\n")
            elif segment == "this":
                # pop this index
                self.__file_path.write(
                    "@" + str(index) + "\nD=A\n@THIS\nD=D+M\n@R13\nM=D\n@SP\nAM=M-1\nD=M\nM=0\n@R13\nA=M\nM=D\n")
            elif segment == "that":
                # pop that index
                self.__file_path.write(
                    "@" + str(index) + "\nD=A\n@THAT\nD=D+M\n@R13\nM=D\n@SP\nAM=M-1\nD=M\nM=0\n@R13\nA=M\nM=D\n")
            elif segment == "static":
                # pop static index
                self.__file_path.write("@SP\nAM=M-1\nD=M\nM=0\n@static_" + str(index) + "\nM=D\n")
            elif segment == "pointer":
                # pop pointer index
                self.__file_path.write("@SP\nAM=M-1\nD=M\nM=0\n@" + str(index + 3) + "\nM=D\n")
            elif segment == "temp":
                # pop temp index
                self.__file_path.write("@SP\nAM=M-1\nD=M\nM=0\n@" + str(index + 5) + "\nM=D\n")
