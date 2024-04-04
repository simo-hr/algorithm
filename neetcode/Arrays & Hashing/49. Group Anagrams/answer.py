class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        map = {}
        for word in strs:
            key = tuple(sorted(word))
            if key in map:
                map[key].append(word)
            else:
                map[key] = [word]
        for value in map.values():
            res.append(value)
        return res
