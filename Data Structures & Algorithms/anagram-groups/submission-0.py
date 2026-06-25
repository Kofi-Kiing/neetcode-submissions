class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_map=defaultdict(list)
        for st in strs:
            
            anagrams_map[" ".join(sorted(st))].append(st)
            
        return list(anagrams_map.values())

        