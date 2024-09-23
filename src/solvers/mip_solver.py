from src.input import Input

class MIPSolver:
    def __init__(self):
        self.algorithm_name="MIPSolver"

    @property
    def name(self):
        return self.algorithm_name

    @staticmethod
    def solve(input: Input):
        """MIP implementation model that solves the problem"""
        decision_values = {}
        parameter_values = input.data.get("decisions")

        return [decision_values]
