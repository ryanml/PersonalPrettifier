# Author: Ryan Lanese
import tinycss as tc
from sys import argv

USAGE_TEXT = """
USAGE:

pprettifier [-f|-t] [style.css|RAW INPUT]

"""

"""
Invalid stylesheet error
"""
class InvalidStylesheetError(Exception):

    def __init__(self):
        super(
            InvalidStylesheetError, self
        ).__init__("Invalid CSS!")

"""
Args error
"""
class InvalidArgumentsError(Exception):

    def __init__(self):
        print USAGE_TEXT
        super(
            InvalidArgumentsError, self
        ).__init__("Invalid arguments!")

"""
Prettifier
"""
class Prettifier(object):

    def __init__(self, file, extra=False):
        self.file = file
        self.parser = tc.make_parser()
        self.styles = self.build_struct(
            self.load_file()
        )
        self.order_struct()

    def build_struct(self, rules):
        styles = []
        for rule in rules.rules:
            declarations = []
            selector = rule.selector.as_css()
            _declarations = rule.declarations
            for declaration in _declarations:
                name = declaration.name
                value = declaration.value.as_css()
                declarations.append(
                    {'declaration': ("%s:%s" % (name, value))}
                )
            styles.append(
                {'selector': selector, 'declarations': declarations }
            )
        return styles

    def load_file(self):
        with open(self.file) as f:
            lines = f.read()
            rules = self.parser.parse_stylesheet(lines)
        if len(rules.errors) > 0:
            raise InvalidStylesheetError
        return rules

    def order_struct(self):
        for i, s in enumerate(self.styles):
            decs = self.styles[i]['declarations']
            temp = sorted(decs, key=lambda x: len(x['declaration']))
            self.styles[i]['declarations'] = temp

    def prettify_sheet(self):
        with open(self.file, 'r+') as f:
            f.seek(0)
            for style in self.styles:
                f.write("%s {\n" % style['selector'])
                for declaration in style['declarations']:
                    f.write("  %s;\n" % declaration['declaration'])
                f.write("}\n\n")
            f.truncate()
            f.close()

def main():
    prettifier = Prettifier(argv[2])
    prettifier.prettify_sheet()

if __name__ == "__main__":
    error_conditions = [
        (len(argv) < 3),
        (argv[1] != '-f' and argv[1] != '-t')
    ]
    if True in error_conditions:
        raise InvalidArgumentsError()
    main()
