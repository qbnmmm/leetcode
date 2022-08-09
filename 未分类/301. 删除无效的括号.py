from functools import lru_cache


class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        l = r = 0
        for c in s:
            if c == '(':
                l += 1
            elif c == ')':
                if l:
                    l -= 1
                else:
                    r += 1

        ans = []
        n = len(s)

        @lru_cache(None) # 这里的lru_cache是必须的，一方面可以提高运行速度，另一方面是防止重复结果(因为出现重复结果时就不调用dfs方法了，避免了重复加入ans)
        def dfs(idx: int, cl: int, cr: int, dl: int, dr: int, path: str) -> None:
            '''
            记忆化搜索
            :param idx: 当前位置
            :param cl: 当前左括号数
            :param cr: 当前右括号数
            :param dl: 当前还需要删除的左括号数
            :param dr: 当前还需要删除的右括号数
            :param path: 路径
            '''
            if idx == n:  # 搜索到最后
                if not dl and not dr:  # 如果没有待删除的括号
                    ans.append(path)
                return
            if cr > cl or dl < 0 or dr < 0:  # 任何时候cr都不应该比cl多；dl或dr小于0说明删多了
                return
            c = s[idx]
            if c == '(':  # 先尝试删掉c
                dfs(idx + 1, cl, cr, dl - 1, dr, path)
            elif c == ')':  # 先尝试删掉c
                dfs(idx + 1, cl, cr, dl, dr - 1, path)
            dfs(idx + 1,  # 保留该字符
                cl + (c == '('),  # 如果c为左括号就加到cl, 如果为右括号就加到cr上，其他字符就不加
                cr + (c == ')'),
                dl, dr,  # 不删除所以dl, dr不变
                path + c)  # 不删除所以路径要加上当前字符

        dfs(idx=0, cl=0, cr=0, dl=l, dr=r, path="")
        return ans