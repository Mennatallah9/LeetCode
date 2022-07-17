class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        d = []
        for s in arr:
            if arr.count(s) == 1:
                d.append(s)
        if k > len(d):
            return ""
        return d[k-1]
