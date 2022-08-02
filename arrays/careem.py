"""
S and T are strings composed of lowercase letters.
In S, no letter occurs more than once. S was sorted in some custom order previously.
We want to permute the characters of T so that they match the order that S was sorted.
More specifically, if x occurs before y in S, then x should occur before y in the returned string.
Return any permutation of T (as a string) that satisfies this property
Example :
Input: 
S = "cba"
T = "abcd"
Output: "cbad"
Explanation: "a", "b", "c" appear in S, so the order of "a", "b", "c" should be
 "c", "b", and "a". Since "d" does not appear in S, it can be at any position in T.
  "dcba", "cdba", "cbda" are also valid outputs.


  [[1, 1], [11, 4], [3 ,1], [2, 1], [1, 3],  [5, 12], [3, 3], [3, 2]]
"""
from typing import List
import itertools as it

def convert(S: str, T: str) -> List[int]:
    mapping = { x : i for i, x in enumerate(S)}

    res: List[List[str]] = [[] for i in range(len(mapping) + 1)]

    for c in T:
        res[mapping.get(c, -1)].append(c)

    final_res = list(it.chain(*res))

    return final_res

from collections import defaultdict


def detect_rec(points: List) -> List:
    x_mapping = defaultdict(set)
    # y_mapping = defaultdict(set)
    for x, y in points:
        x_mapping[x].add(y)
        # y_mapping[y].add(x)
    
    res = []
    
    for x in x_mapping:





if __name__ == "__main__":
    # S = "cbaj"
    # T = "abcdaak"
    # # new_T = sorted(T, key= lambda x: S.index(x) if x in S else -1)
    # new_T = convert(S, T)
    # print(new_T)



    input = [[1, 1], [11, 4], [3 ,1], [2, 1], [1, 3],  [5, 12], [3, 3], [3, 2]]
    res = detect_rec(input)
    print(res)
