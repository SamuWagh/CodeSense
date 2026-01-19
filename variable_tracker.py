import re

class VariableTracker:
    def __init__(self, code):
        self.code = code

    def find_declared_variables(self):
        return set(re.findall(r'(\w+)\s*=', self.code))

    def find_used_variables(self):
        return set(re.findall(r'print\((\w+)\)', self.code))

    def unused_variables(self):
        declared = self.find_declared_variables()
        used = self.find_used_variables()
        return declared - used
