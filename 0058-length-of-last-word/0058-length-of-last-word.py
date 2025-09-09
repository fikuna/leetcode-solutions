class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        no_space = s.split()
        return len(no_space[-1])