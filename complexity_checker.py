import re

class ComplexityChecker:
    def __init__(self, code):
        self.code = code

    def estimate_complexity(self):
        loops = len(re.findall(r'\bfor\b|\bwhile\b', self.code))
        if loops == 0:
            return "O(1)"
        elif loops == 1:
            return "O(n)"
        elif loops == 2:
            return "O(n²)"
        else:
            return "High Complexity"
