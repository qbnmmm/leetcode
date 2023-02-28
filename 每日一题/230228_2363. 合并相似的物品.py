class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        items1.sort(key = lambda x: x[0])
        items2.sort(key = lambda x: x[0])
        i, j = 0, 0
        m, n = len(items1), len(items2)
        ans = []
        while i < m and j < n:
            if items1[i][0] == items2[j][0]:
                ans.append([items1[i][0], items1[i][1] + items2[j][1]])
                i += 1
                j += 1
            elif items1[i][0] < items2[j][0]:
                ans.append(items1[i])
                i += 1
            else:
                ans.append(items2[j])
                j += 1
        
        while i < m:
            ans.append(items1[i])
            i += 1
        
        while j < n:
            ans.append(items2[j])
            j += 1

        return ans