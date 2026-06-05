class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        while strs:
            word = strs.pop(0)
            group = [word]
            for others in strs[:]:
                if sorted(word) == sorted(others):
                    group.append(others)
                    strs.remove(others)
            result.append(group)
        return result