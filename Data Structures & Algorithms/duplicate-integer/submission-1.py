class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupe_map = {}

        for num in nums:
            if num in dupe_map:
                return True
            dupe_map[num] = 1
        return False