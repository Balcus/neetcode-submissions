class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        op = ['+', '-', '/', '*']
        for token in tokens:
            if token in op:
                t2 = int(stack.pop())
                t1 = int(stack.pop())
                if token == '+':
                    stack.append(t1 + t2)
                elif token == '-':
                    stack.append(t1 - t2)
                elif token == '*':
                    stack.append(t1 * t2)
                elif token == '/':
                    stack.append(t1 / t2)
            else:
                stack.append(token)
        return int(stack[-1])
