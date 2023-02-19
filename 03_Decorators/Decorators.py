# Function that takes another function as argument (callback) and returns a function
def decorator_function(original_function):
    #  *args and **kwards allow us to pass any number of parameters - the name is given for convention
    def wrapper_function(*args, **kwargs):
        print(f'wrapper executed this before {original_function.__name__}')
        return original_function(*args, **kwargs)
    return wrapper_function


def display():
    print('display function ran\n')

# It means that display2 will be pass automatically as argument to decorator_function
@decorator_function
def display2():
    print('display2 function ran\n')


@decorator_function
def display_info(name, age):
    print('display_info ran with arguments ({}, {})\n'.format(name, age))


# Create a decorator to measure the performance of any function
def performance(func):
    from time import time

    def wrapper(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f"took {t2 - t1} s")
        return result
    return wrapper


@performance
def long_time():
    for i in range(100000000):
        i *= 2

def authenticated(fn):
    def wrapper(*args, **kwargs):
        # Check for the first argument
        if args[0]["valid"] is True:
            return fn(*args, **kwargs)
        print("Not valid user")
    return wrapper


@authenticated
def message_friends(user):
    print('message has been sent')


def main() -> None:
    # This is what we would do without decorators
    decorated_display = decorator_function(display)
    decorated_display()
    # Now we do the same but with decorators
    display2()
    display_info('Ivan', 24)

    long_time()

    # Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
    user1 = {
        'name': 'Sorna',
        # changing this will either run or not run the message_friends function.
        'valid': True
    }
    message_friends(user1)


if __name__ == '__main__':
    main()