class Solution:
    def calculate(self, s: str) -> int:
        s = s.strip().replace(" ", "")
        # "(1+(4+5+2)-3)+(6+8)"
        output: int = 0
        current_number: int = 0
        sign: int = 1
        stack: list = []

        # 2147483647
        if "+" not in s and "-" not in s and "(" not in s and ")" not in s and "+" not in s and "-" not in s:
            print("No expession passed")
            return int(s)

        for c in s:
            # Digit
            if c.isdigit():
                # print(f"Current = {current_number}, Current * 10 = {current_number * 10}, digit = {int(c)}")
                current_number += (current_number * 10) + int(c)

            # Operation
            elif c in "+-":
                output += (current_number * sign)
                current_number = 0
                sign = 1 if c == "+" else -1

            # Left parenthesis
            elif c == "(":
                stack.append(output)
                stack.append(sign)  # Order matters when closing parenthesis
                output = 0
                sign = 1

            # Right parenthesis
            elif c == ")":
                output += (current_number * sign)
                current_number = 0

                output *= stack.pop()  # Contains last sign before opening left parenthesis
                output += stack.pop()  # Adding output from last iteration

        return output + (current_number * sign)  # add cur + sign in case of an expression without parenthesis at the end
