class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:

        def backTrack(level: int) -> None:
            if len(cur_ans) == k:
                ans.append(cur_ans[:]) #这里是防止添加元素后元素又被修改导致ans里的数据被更改
            elif level > n:
                return
            else:
                cur_ans.append(level)
                backTrack(level+1)
                cur_ans.pop()
                backTrack(level+1)

        ans, cur_ans = [], []
        backTrack(1)
        return ans

a = Solution()
ans = a.combine(4,3)
print(ans)