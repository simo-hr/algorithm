# https://leetcode.com/problems/evaluate-reverse-polish-notation
from collections import deque

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1: return int(tokens[0])
        stack = deque([])
        operators = ['+', '-', '*', '/']

        for token in tokens:
            if token in operators:
                b = int(stack.pop())
                a = int(stack.pop())
                print(a,b)
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                elif token == '/':
                    stack.append((a / b))
                continue
            stack.append(token)


        return math.floor(stack.pop())
