class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        track = {}
        for i in strs:
            ans = "".join(sorted(i))
            if ans not in track:
                track[ans]=[i]
            else:
                track[ans].append(i)
        return list(track.values())
        