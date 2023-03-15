
def get_inputs() -> list:
    return [int(input("Enter the first number: ")),
            input("Enter the desired operator (+, -, *, /): ").strip(),
            int(input("Enter the second number: "))]


def main() -> None:
    first_number, operator, second_number = get_inputs()
    print(f"{first_number} {operator} {second_number}")


if __name__ == '__main__':
    main()