class Solution:
    def exclusiveTime(self, n: int, logs: list[str]) -> list[int]:
        def helper(log):
            idx, sig, timestamp = log.split(":")
            return int(idx), sig[0] == "s", int(timestamp)

        stack, ans, total = [], [0] * n, 0
        for lg in logs:
            idx, is_start, timestamp = helper(lg)
            if is_start:
                stack.append(total - timestamp)
            else:
                d = stack.pop()
                diff = timestamp + 1 + d - total
                ans[idx] += diff
                total += diff
        return ans


a = Solution()
logs = ["0:start:0", "1:start:2", "1:end:5", "1:start:5", "1:end:6", "0:end:7"]
ans = a.exclusiveTime(2, logs)
print(ans)