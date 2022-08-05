import collections


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        """
        单调队列：
        进入滑动窗口遍历到新的值时：
        如果比队尾大，则将队尾元素弹出，直到小于等于队尾或队列为空为止
        如果比队尾小或相等，则加入队列
        离开滑动窗口时：
        离开的元素比队头小则不管
        和队头元素一样则单调队列出队该元素
        不可能比队头大
        """
        n = len(nums)
        q = collections.deque()
        l, r = 0, 0
        while r < k:
            if not q:
                q.append(nums[r])
            else:
                while q and q[-1] < nums[r]:
                    q.pop()
                q.append(nums[r])
            r += 1
        ans = []
        while r < n:
            ans.append(q[0])
            if nums[l] == q[0]:
                q.popleft()
            l += 1

            while q and nums[r] > q[-1]:
                q.pop()
            q.append(nums[r])
            r += 1
        ans.append(q[0])
        return ans


nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
a = Solution()
ans = a.maxSlidingWindow(nums, k)
print(ans)