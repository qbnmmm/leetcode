class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ls, lt = len(s), len(t)
        if ls != lt or s == t: return False
        ds, dt = {}, {}
        for i in range(ls):
            ds[s[i]] = ds.get(s[i], 0) + 1
            dt[t[i]] = dt.get(t[i], 0) + 1
        for k, v in ds.items():
            if dt.get(k, -1) != v:
                return False
        return True