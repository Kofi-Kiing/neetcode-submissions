class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict={}
        
        for s in strs:
            ss = ''.join(sorted(s))
            if ss not in dict:
                dict[ss]=[s]
            else:
                dict[ss].append(s)
        return list(dict.values())
            