from abc import ABC, abstractmethod

class AdventDayProblem:

    def __init__(self, input_text):
        self.input_text = input_text
        super().__init__()
    
    @abstractmethod
    def solve_problem_a(self):
        pass
    
    @abstractmethod
    def solve_problem_b(self):
        pass

    def print_solutions(self):
        solution_a = self.solve_problem_a()
        solution_b = self.solve_problem_b()

        print(solution_a)
        print(solution_b)