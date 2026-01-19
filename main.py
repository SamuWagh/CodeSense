from analyzer import CodeAnalyzer
from variable_tracker import VariableTracker
from complexity_checker import ComplexityChecker
from report_generator import ReportGenerator

# Read sample code
with open("sample_code.py", "r") as file:
    code = file.read()

analyzer = CodeAnalyzer(code)
tracker = VariableTracker(code)
complexity = ComplexityChecker(code)
reporter = ReportGenerator()

data = {
    "lines": analyzer.total_lines(),
    "functions": analyzer.count_functions(),
    "classes": analyzer.count_classes(),
    "loops": analyzer.count_loops(),
    "conditions": analyzer.count_conditions(),
    "unused": tracker.unused_variables(),
    "complexity": complexity.estimate_complexity()
}

report = reporter.generate(data)
print(report)
