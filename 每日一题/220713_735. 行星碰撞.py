class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []
        i = 0
        while i < len(asteroids):
            if not stack or stack[-1] < 0 or asteroids[i] > 0:
                stack.append(asteroids[i])
            elif stack[-1] <= -asteroids[i]:
                if stack.pop() < -asteroids[i]:
                    continue
            i += 1
        return stack
