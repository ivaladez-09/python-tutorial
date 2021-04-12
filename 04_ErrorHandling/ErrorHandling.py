# Error Handling
while True:
    try:
        age = int(input("What is your age?"))
        print(10/age)
    except ValueError:
        print("Please enter a number")
    except ZeroDivisionError:
        print("Please enter a age higher than 0")
    else:
        print("Thank you")
        break
    finally:  # It is ALWAYS executed
        print("Ok, I'm finally done")


def my_div(num1, num2):
    try:
        return num1 / num2
    except (TypeError, ZeroDivisionError) as err:
        print(f"An error occured: {err}")


my_div(1, "3")
my_div(1, 0)
