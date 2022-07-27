class Solution:
    def evaluate(self, expression: str) -> int:
        stacks = []
        maps = []

        def parseValue(v, map):
            if type(v) is int or v[0] == "-" or v.isnumeric():
                return int(v)
            elif v in map:
                return map[v]
            else:
                return v

        def addValue(v, stack, map):
            op = stack[0]
            if op == "let" and len(stack) & 1:  # 奇数长度的stack不进行解析
                stack.append(v)
            else:
                v = parseValue(v, map)
                if op == "let":
                    map[stack[-1]] = v
                stack.append(v)

        def calResult(stack, map):
            op = stack[0]
            if op == "let":
                return parseValue(stack[-1], map)
            elif op == "add":
                return parseValue(stack[-2], map) + parseValue(stack[-1], map)
            else:
                return parseValue(stack[-2], map) * parseValue(stack[-1], map)

        for w in expression.split():
            if w[0] == "(":
                op = w[1:]
                stacks.append([op])
                nmap = maps[-1].copy() if maps else {}
                maps.append(nmap)
            elif w[-1] == ")":
                v = w[:w.find(")")]
                addValue(v, stacks[-1], maps[-1])
                for i in range(len(w))[::-1]:
                    if w[i] != ")":
                        break
                    res = calResult(stacks.pop(), maps.pop())
                    if stacks:
                        addValue(res, stacks[-1], maps[-1])
                    else:
                        return res
            else:
                addValue(w, stacks[-1], maps[-1])

expression = "(let x 2 (mult x (let x 3 y 4 (add x y))))"
a = Solution()
ans = a.evaluate(expression)
print(ans)