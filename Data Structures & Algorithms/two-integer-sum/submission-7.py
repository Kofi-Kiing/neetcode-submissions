class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict={}
        for i in range(len(nums)):
            dict[nums[i]]=i
        for i in range(len(nums)):
            other = target - nums[i]
            if other in dict:
                minn=min(i,dict[other])
                maxx=max(i,dict[other])
                if minn!=maxx:
                    return [minn,maxx]
                




                