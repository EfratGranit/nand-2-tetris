
class SymbolTable:
    def __init__(self):
        self.__symbol_table = {
            "R0": 0,
            "R1": 1,
            "R2": 2,
            "R3": 3,
            "R4": 4,
            "R5": 5,
            "R6": 6,
            "R7": 7,
            "R8": 8,
            "R9": 9,
            "R10": 10,
            "R11": 11,
            "R12": 12,
            "R13": 13,
            "R14": 14,
            "R15": 15,
            "SCREEN": 16384,
            "KBD": 24576,
            "SP": 0,
            "LCL": 1,
            "ARG": 2,
            "THIS": 3,
            "THAT": 4
        }
        self.__free_address = 16

    def add_variable_symbol(self, symbol):
        print(self.__symbol_table.keys())
        if symbol not in self.__symbol_table:
            self.__symbol_table.update({symbol: self.__free_address})
            self.__free_address += 1

    def add_label_symbol(self, symbol, address):
        self.__symbol_table.update({symbol: address})

    def get_address(self, symbol):
        return self.__symbol_table.get(symbol)
