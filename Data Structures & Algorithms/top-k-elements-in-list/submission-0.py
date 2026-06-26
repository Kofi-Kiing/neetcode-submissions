class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen={}
        for i in range(len(nums)):
            if nums[i] not in seen:
                seen[nums[i]]=[nums[i]]
            else:
                seen[nums[i]].append(nums[i])
        frequency=list(seen.values())
        frequency.sort(key=len, reverse=True)
        # valid=frequency[:k]
        output=[]
        for i in range(k):
            output.append(frequency[i][0])
        return output
