from typing import List

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        l, r = 0, len(products) - 1
        products.sort()
        MAX_SUGGEST_COUNT = 3
        res: List[List[str]] = []
        for i, c in enumerate(searchWord):

            # correct left pointer
            while l <= r and (len(products[l]) <= i or products[l][i] != c):
                l += 1
            # correct right pointer
            while l <= r and (len(products[r]) <= i or  products[r][i] != c):
                r -= 1

            res.append([])
            remain = r - l + 1
            for j in range(min(remain, MAX_SUGGEST_COUNT)):
                res[-1].append(products[l + j])

        return res



if __name__ == "__main__":
    inputs = [
        (["mobile","mouse","moneypot","monitor","mousepad"], "mouse"),
        (["havana"], "havana"),
        (["bags","baggage","banner","box","cloths"], "bags")
    ]
    outputs = [
        [
            ["mobile","moneypot","monitor"],
            ["mobile","moneypot","monitor"],
            ["mouse","mousepad"],
            ["mouse","mousepad"],
            ["mouse","mousepad"]
        ],
        [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]],
        [["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]
    ]
    sol = Solution()
    for (products, searchWord), expected in zip(inputs, outputs):
        res = sol.suggestedProducts(products, searchWord)
        assert tuple(map(tuple, res)) == tuple(map(tuple, expected)), f"{res}\nwhile expected {expected}"
        print("pass")