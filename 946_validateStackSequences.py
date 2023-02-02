class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        r, arr, length = 0, [], len(popped)
        for i in pushed:
            arr.append(i)
            while arr and arr[-1] == popped[r]:
                arr.pop()
                r += 1
        return True if r == length else False