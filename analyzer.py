import re

class CodeAnalyzer:
    def __init__(self, code):
        self.code = code

    def count_functions(self):
        return len(re.findall(r'^def ', self.code, re.MULTILINE))

    def count_classes(self):
        return len(re.findall(r'^class ', self.code, re.MULTILINE))

    def count_loops(self):
        return len(re.findall(r'\bfor\b|\bwhile\b', self.code))

    def count_conditions(self):
        return len(re.findall(r'\bif\b|\belif\b|\belse\b', self.code))

    def total_lines(self):
        return len(self.code.splitlines())
