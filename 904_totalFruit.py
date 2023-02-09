class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left, right = 0, 0
        res = 0
        cnt = collections.defaultdict(int)
        while right < len(fruits):
            cnt[fruits[right]] += 1
            while len(cnt) > 2:
                cnt[fruits[left]] -= 1
                if cnt[fruits[left]] == 0:
                    del cnt[fruits[left]]
                left += 1
            res = max(res, right - left + 1)
            right += 1
        return res