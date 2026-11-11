class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        track = {}
        for i in nums:
            if i in track:
                track[i]+=1
            else:
                track[i]=1 
        return sorted(track, key=lambda x: track[x], reverse=True)[:k]

