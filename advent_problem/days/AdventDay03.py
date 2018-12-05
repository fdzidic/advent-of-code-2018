from AdventDayProblem import AdventDayProblem

class AdventDay03(AdventDayProblem):

    def __init__(self, input_text):
        super().__init__(input_text)
        self.fabric = {}
        self.ids = set()
        self._mark_fabric()

    def _parse_claim(self, claim):
        space_splits = claim.split(" ")
        claim_id = int(space_splits[0][1:])
        x = int(space_splits[2].split(",")[0])
        y = int(space_splits[2].split(",")[1][:-1])
        width, height = [int(n) for n in space_splits[3].split("x")]
        return claim_id, x, y, width, height
    
    def _mark_fabric(self):
        for claim_line in self.input_text.splitlines():
            claim_id, x, y, width, height = self._parse_claim(claim_line)
            self._mark_coordinate(claim_id, x, y, width, height)

    def _mark_coordinate(self, claim_id, x, y, width, height):
        self.ids.add(claim_id)
        for i in range(width):
            for j in range(height):
                claim_ids = self.fabric.get((x+i, y+j), set())
                claim_ids.add(claim_id)
                self.fabric[(x+i, y+j)] = claim_ids

    def solve_problem_a(self):
        claimed_by_multiple_count = 0
        for coordinate in self.fabric.keys():
            if len(self.fabric[coordinate]) > 1:
                claimed_by_multiple_count += 1
        return claimed_by_multiple_count

    
    def solve_problem_b(self):
        nonOverlappingIds = self.ids
        for claims in self.fabric.values():
            if len(claims) > 1:
                nonOverlappingIds = nonOverlappingIds.difference(claims)
        return nonOverlappingIds