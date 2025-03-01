import random, time, functools
import logging

logging.basicConfig(level=logging.INFO)

# Task 1: Create a Retry Decorator
# Build a decorator that automatically retries a function if it raises an exception.


def Retry(MAX_ATTEMPTS: int, DELAY: float):
    logging.debug(f"defined: MAX_ATTEMPTS= {MAX_ATTEMPTS}, DELAY = {DELAY}")

    def decorator(func):
        logging.debug(f"got function {func.__name__}")

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            logging.debug(f"args: {args} kwagrs: {kwargs}")
            attempts = 0
            while attempts < MAX_ATTEMPTS:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    if attempts == MAX_ATTEMPTS:
                        raise
                    print(f"got exception {e}")
                    print(f"Attempt -> {attempts} retying in {DELAY} ....")
                    time.sleep(DELAY)
            return None

        logging.debug("calling wrapper")
        return wrapper

    logging.debug("calling decorator")
    return decorator


@Retry(MAX_ATTEMPTS=5, DELAY=0.5)
def unreliable_function(number):
    """Function that simulates occasional failures"""
    if number < 0.7:
        raise ConnectionError("Random connection error")
    else:
        return "success"


# print(unreliable_function(number=random.random()))


# Task 2:Create a Timing Decorator
# Build a decorator that measures and prints how long a function takes to execute.


def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        time.sleep(0.5)
        elapsed = end_time - start_time
        return f"{func.__name__} took {elapsed}s to complete execution"

    return wrapper


@timer
def xyz(*args):
    return sum(args)


# print(xyz(1,2,3,4,5))


# Task 3: Create a Type Validation Decorator
# Build a decorator that validates function arguments against expected types.


def validate_types(func):
    @functools.wraps(func)
    def wrapper(*args):
        if not all(isinstance(arg, (int, float)) for arg in args):
            raise TypeError("Input Must be numeric")
        return func(*args)

    return wrapper


@validate_types
def my_divi(*args):
    return functools.reduce(lambda x, y: x / y if x > y else y / x, args)


# print(my_divi(5,1,4))
# print(my_divi(5, "a", 4))


# Task 4 : Use of decorator in authentication

# Task 4 : Use of decorator in authentication
get_user_data = lambda: [
    {"username": "Paurakh", "authenticated": True},
    {"username": "Raja", "authenticated": False},
    {"username": "Aaja", "authenticated": True},
]


def login_required(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        users = get_user_data()
        username = (
            kwargs.get("username")
            if "username" in kwargs
            else args[0]
            if args
            else None
        )
        for user in users:
            if user["username"] == username and user["authenticated"]:
                return func(username)
        return "Not Authorized Redirecting to Dashboard"

    return wrapper


@login_required
def get_template(username):
    return f"redirecting {username} to template page"


print(get_template("Raja"))
print(get_template("Paurakh"))
