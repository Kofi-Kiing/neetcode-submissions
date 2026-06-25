class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new_num=set(nums)
        return len(new_num)!=len(nums)