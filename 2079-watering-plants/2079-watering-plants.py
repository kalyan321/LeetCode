class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps = 0
        cap_rem = capacity
        for i in range(len(plants)):
            if cap_rem < plants[i]:
                steps += 2 * i + 1
                cap_rem = capacity - plants[i]
            else:
                steps += 1
                cap_rem -= plants[i]
        return steps