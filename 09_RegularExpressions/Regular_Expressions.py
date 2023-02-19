import re


def main():
    string = "search this inside of this text please!"
    print("search" in string)

    match = re.search("this", string)
    if match:
        print(match.span())  # Where the text is
        print(match.start())  # Where the text starts
        print(match.end())  # Where the text ends
        print(match.group())  # Where the text starts

    pattern = re.compile("this")
    match = pattern.search(string)
    if match:
        expressions = pattern.findall(string)
        print(expressions)
        expressions = pattern.fullmatch(string)
        print(expressions)

    pattern = re.compile(r"([a-zA-Z].([a]))")
    match = pattern.search(string)
    if match:
        expressions = pattern.findall(string)
        print(expressions)
        expressions = pattern.fullmatch(string)
        print(expressions)
        print(match.group(1))
        print(match.group(1))


if __name__ == '__main__':
    main()
