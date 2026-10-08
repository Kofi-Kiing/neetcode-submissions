from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=Counter(nums)
        ls=freq.most_common(k)
        result=[]
        for i in range(len(ls)):
            result.append(ls[i][0])
        return result



