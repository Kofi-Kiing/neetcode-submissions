class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen={}
        for i in range(len(strs)):
            sorted_s = ''.join(sorted(strs[i]))
            if sorted_s in seen:
                seen[sorted_s].append(strs[i])
            else:
                seen[sorted_s]=[strs[i]]
        return list(seen.values())

        