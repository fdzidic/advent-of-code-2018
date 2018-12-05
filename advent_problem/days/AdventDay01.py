from AdventDayProblem import AdventDayProblem

class AdventDay01(AdventDayProblem):

    def solve_problem_a(self):
        return sum([int(line) for line in self.input_text.splitlines()])
    
    def solve_problem_b(self):
        frequency_sum = 0
        seen_frequencies = set()
        while(True):
            for line in self.input_text.splitlines():
                frequency_sum += int(line)
                if frequency_sum in seen_frequencies:
                    return frequency_sum
                else:
                    seen_frequencies.add(frequency_sum)
