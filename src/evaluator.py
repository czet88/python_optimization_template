from src.input import Input
from src.solutions import Solution


class Evaluator:
    """
    The generic interface solver that matters to outside callers of the function. This will be the interface for
    multiple solution processes
    """

    def __init__(self, input: Input):
        """
        Construct an instance of the solver with a chosen solution algorithm
        """
        self._input = input

    def evaluate(self, solution: Solution) -> float:

        return  sum(value for idx, value in solution.decision_values.items())

