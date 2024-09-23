from src.input import Input
from src.solutions import SolutionPool


class Solver:
    """
    The generic interface solver that matters to outside callers of the function. This will be the interface for
    multiple solution processes
    """

    def __init__(self, algorithm: any):
        """
        Construct an instance of the solver with a chosen solution algorithm
        """
        self._algorithm = algorithm

    @property
    def algorithm(self) -> any:
        """
        Retrieve the current algorithm being used.
        :return:
        Algorithm being used
        """
        return self._algorithm

    @algorithm.setter
    def algorithm(self, algorithm: any):
        """
        :param algorithm: the new solv algorithm to be used
        :return:
        """
        self._algorithm=algorithm

    def find_solutions(self, input: Input, solution_pool: SolutionPool) -> None:
        solutions = self._algorithm.solve(input)
        solution_pool.add_to_solution_pool(self._algorithm.name, solutions)

