class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        turns = sorted([(p, (target - p) / s) for p, s in zip(position, speed)])
        fleets = 0
        while turns:
            _, fleet_turns = turns.pop()
            fleets += 1
            while turns and (turns[-1][1] <= fleet_turns):
                turns.pop()
        return fleets 

        






        
        