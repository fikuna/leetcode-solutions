class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_rich = 0
        for i in accounts:
            max_rich = max(max_rich, sum(i))
        return max_rich