import re


pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
string = "b@b.com"
match = pattern.search(string)
if match:
    print(match.group(1))
