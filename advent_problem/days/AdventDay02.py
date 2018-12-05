from AdventDayProblem import AdventDayProblem
from itertools import combinations

class AdventDay02(AdventDayProblem):

    def solve_problem_a(self):
        occurs_twice_count, occurs_thrice_count = (0, 0)
        for (twice_ocurring, thrice_occuring) in map(_ocurring_twice_or_thrice, self.input_text.splitlines()):
            occurs_twice_count += twice_ocurring
            occurs_thrice_count += thrice_occuring
        return occurs_twice_count * occurs_thrice_count


    
    def solve_problem_b(self):
        for x, y in combinations(self.input_text.splitlines(), 2):
            hamming_distance, shared_characters = _hamming_distance(x, y)
            if hamming_distance == 1:
                return shared_characters


def _ocurring_twice_or_thrice(line):
    character_count = {}
    twice_ocurring, thrice_occuring = (0,0)
    for character in line:
        character_count[character] = character_count.get(character, 0) + 1

    for value in character_count.values():
        if value == 2:
            twice_ocurring = 1
        elif value == 3:
            thrice_occuring = 1
    
    return (twice_ocurring, thrice_occuring)

def _hamming_distance(line_x, line_y):
    hamming_distance = 0
    shared_characters = ''
    for c1, c2 in zip(line_x, line_y):
        if c1 == c2:
            shared_characters += c1
        else:
            hamming_distance += 1
    return hamming_distance, shared_characters