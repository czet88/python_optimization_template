from src.input import Input
from src.solutions import SolutionPool, Solution
from src.solver import Solver
from src.solvers.mip_solver import MIPSolver
from src.evaluator import Evaluator


class InstanceManager:
    def __init__(self, dir_to_inputs: str):
        self.root_dir = dir_to_inputs
        self.solvers = None
        self.solution_pool = SolutionPool()
        # Read the data to create an input
        self.input = Input.load_from_csv_files(self.root_dir)


    def solve(self, solvers :list[str], top_n_solutions: int) -> list[dict[str, float]]:
        """
        Function that will solve the problem built so far based on the input data.
        :param solvers: names of the types of the solution algorithms we will call
        :param top_n_solutions: number of top solutions to keep
        :return: List of n best solutions
        """
        self.solvers = solvers

        my_solver = Solver(MIPSolver())

        # For each algorithm that we try, add them to the solution pool
        for solver_name in solvers:
            if solver_name == "MIP":
                my_solver.algorithm = MIPSolver()
                my_solver.find_solutions(self.input, self.solution_pool)

        # Evaluate the top solutions
        self.solution_pool.evaluate_solutions(Evaluator(self.input))
        # Return the top_n_solutions according to the evaluation done
        return self.solution_pool.get_top_solutions(top_n_solutions)


