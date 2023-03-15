def update(stack: list, sign: str, value: int) -> None:
    if sign == "+":
        stack.append(value)
    elif sign == "-":
        stack.append(-value)
    elif sign == "*":
        stack.append(stack.pop() * value)  # Assuming an integer is going to be there
    elif sign == "/":
        stack.append(int(stack.pop() / value))


class Solution:
    def calculate(self, s: str) -> int:
        i, num, stack, sign = 0, 0, [], "+"

        while i < len(s):
            if s[i].isdigit():
                num = (num * 10) + int(s[i])

            elif s[i] in "+-*/":
                update(stack, sign, num)
                num = 0
                sign = s[i]

            elif s[i] == "(":  # Calculate all inside parenthesis
                num, j = self.calculate(s[i + 1:])
                i += j

            elif s[i] == ")":  # Return calculation to last call for "("
                update(stack, sign, num)
                return sum(stack), i + 1

            i += 1
        update(stack, sign, num)
        return sum(stack)


if __name__ == '__main__':
    solution: Solution = Solution()
    strings: list = ["3+2*2", " 3/2 ", " 3+5 / 2 ", "3-1*2", "(1+(4+5+2)-3)+(6+8)", "(1+(4*5+2)-3)+(6/8-1)"]
    result: int = 0
    for s in strings:
        result = solution.calculate(s)
        print(f"\nCalculation of {s} = {result}")
