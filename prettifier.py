# Author: Ryan Lanese
from sys import argv

USAGE_TEXT = """
USAGE:

pprettifier [-f|-t] [style.css|RAW INPUT]

"""

"""
Args error
"""
class InvalidArgumentsError(Exception):

    def __init__(self):
        super(
            InvalidArgumentsError, self
        ).__init__("Invalid arguments!")

"""
Prettifier
"""
class Prettifier(object):

    def __init__(self, file, extra=False):
        self.rules = self.load_file(file)

    def load_file(self, file):
        rules = []
        with open(file, 'r') as f:
            for line in f:
                rules.append(f)
        return rules

def main():
    style_sheet = '/path/to/style.css'
    #prettifier = Prettifier(style_sheet)

if __name__ == "__main__":
    error_conditions = [
        (len(argv) < 3),
        (argv[1] != '-f' and argv[1] != '-t')
    ]
    if True in error_conditions:
        print USAGE_TEXT
        raise InvalidArgumentsError()
    main()
