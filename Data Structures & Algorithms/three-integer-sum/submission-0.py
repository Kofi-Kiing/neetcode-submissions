class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results=[]
        for i in range(len(nums)):
            target = -nums[i]
            left=i+1
            right=len(nums)-1
            j=i
            while left<right:
                summ= nums[left]+nums[right]
                if summ == target:
                    solution=[nums[i],nums[left],nums[right]]
                    
                    if solution not in results:
                        results.append(solution)
                    left+=1
                    right-=1
                else:
                    if summ>target:
                        right -=1
                    else:
                        left+=1
        return results



        