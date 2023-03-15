class Solution:
    def calculate(self, s: str) -> int:
        def update(op, v):
            # print(f"Appending {op} and {v}")
            if op == "+": stack.append(v)
            if op == "-": stack.append(-v)
            if op == "*": stack.append(stack.pop() * v)  # for BC II and BC III
            if op == "/": stack.append(int(stack.pop() / v))  # for BC II and BC III

        i, num, stack, sign = 0, 0, [], "+"

        while i < len(s):
            if s[i].isdigit():
                num = num * 10 + int(s[i])

            elif s[i] in "+-*/":
                update(sign, num)  # Save prev-sign, not the current one
                num, sign = 0, s[i]

            elif s[i] == "(":  # For BC I and BC III
                num, j = self.calculate(s[i + 1:])
                i += j

            elif s[i] == ")":  # For BC I and BC III
                update(sign, num)
                return sum(stack), i + 1

            i += 1
        update(sign, num)
        return sum(stack)


if __name__ == '__main__':
    solution: Solution = Solution()
    strings: list = ["3+2*2", " 3/2 ", " 3+5 / 2 ", "3-1*2", "(1+(4+5+2)-3)+(6+8)", "(1+(4*5+2)-3)+(6/8-1)"]
    result: int = 0
    for s in strings:
        result = solution.calculate(s)
        print(f"\nCalculation of {s} = {result}")
