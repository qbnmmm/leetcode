class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        ans = [0 for _ in range(len(temperatures))]
        stack = []
        i = 0
        while i < len(temperatures):
            if not stack or temperatures[stack[-1]] >= temperatures[i]:
                stack.append(i)
            else:
                while stack and temperatures[stack[-1]] < temperatures[i]:
                    idx = stack.pop()
                    ans[idx] = i - idx
                stack.append(i)
            i += 1
        return ans