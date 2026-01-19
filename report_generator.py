class ReportGenerator:
    def generate(self, data):
        report = f"""
CODE ANALYSIS REPORT
-------------------
Total Lines       : {data['lines']}
Functions         : {data['functions']}
Classes           : {data['classes']}
Loops             : {data['loops']}
Conditions        : {data['conditions']}
Unused Variables  : {', '.join(data['unused']) if data['unused'] else 'None'}
Estimated Complexity : {data['complexity']}
"""
        return report
