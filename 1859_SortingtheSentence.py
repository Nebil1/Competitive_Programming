class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split()
        result = [""] * len(s)
        for c in s:
            i = int(c[-1])
            result[i - 1] = c[:-1]
        print(result)
        return " ".join(result)