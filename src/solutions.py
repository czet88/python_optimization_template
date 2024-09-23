from typing import List
from dataclasses import dataclass
import pandas as pd

@dataclass
class Solution:
    decision_values: dict[str, float]
    """ Dictionary containing the index and value of the decision to be taken"""

class SolutionPool:
    def __init__(self):
        self._solutions_dict=[]

    def add_to_solution_pool(self, algorithm_name: str, solutions: List[Solution]):
        """
        Function that will add a list of solutions calculated by some algorithm to the solutionpool created.
        :param algorithm_name:
        :param solutions:
        :return:
        """
        for solution in solutions:
            self._solutions_dict.append(
                {
                    "algorithm":
                        algorithm_name,
                    "decision_values":
                        solution
                }
            )

    def evaluate_solutions(self, evaluator: any) -> None:
        """
        This method will take the entire solution pool and evaluate all the solutions based on an evaluator
        :param evaluator: Concrete instance of an evaluation
        :return: None
        """
        # First evaluate each of the solutions based on the evaluator
        for solution in self._solutions_dict:
            solution.update(
                {
                    "evaluation":
                        evaluator.evaluate(solution.get("decision_values"))
                }
            )

    def get_top_solutions(self, num_solutions: int) -> list[dict[str, float]]:
        """
        This method will first evaluate all solutions in the solution pool based on the evalutor function passed and
        return the top
        :param num_solutions: number of solutions to be displayed
        :param evaluator: evaluator function to be used to evaluate each solution and rank them
        :return: ordered list with the top n solutions
        """

        # Now sort them and pick the top n of them
        df = pd.DataFrame(self._solutions_dict)
        df = df.sort_values(by="evaluation_value", ascending=True) # Assuming minimization
        return list(df.head(num_solutions).to_records(index=False))