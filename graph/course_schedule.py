from typing import List
from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    	adj_map = defaultdict(list)
    	for l,r in prerequisites:
    		adj_map[l].append(r)

    	visited = set()
    	def dfs(cr: int) -> bool:
    		if cr in visited:
    			return False

    		# if no dependencies
    		if not adj_map[cr]:
    			return True

    		visited.add(cr)
    		for dep in adj_map[cr]:
    			if not dfs(dep):
    				return False
    		visited.remove(cr)
    		# all deps are checked
    		adj_map[cr] = []
    		return True


    	for i in range(numCourses):
    		if not dfs(i):
    			return False

    	return True



        

if __name__ == "__main__":
    inputs = [
        (2, [[1,0]]),
        (2, [[1,0],[0,1]]),
        (5, [[0,1], [0,2], [1,3], [1,4], [3,4]])
    ]
    outputs = [
        True,
        False,
        True
    ]
    sol = Solution()
    for (nums, prereq), expected in zip(inputs, outputs):
        res = sol.canFinish(nums, prereq)
        assert res == expected, f"{res} while expected {expected}"
        print('pass')