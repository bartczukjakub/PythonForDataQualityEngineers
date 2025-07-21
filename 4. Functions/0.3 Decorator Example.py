# Decorators add additional functionality to the function without having to change the code within original function
# Outer function has to accept function parameter.
# Inner function, wrapper, wraps the code of the original function and calls it.
# It has to return wrapper

def test_decorator(func):
    def wrapper(*args, **kwargs):
        print('This runs before the function.')
        func()
        print('This runs after the function.')
    return wrapper

# In order to use it, we need to call the decorator before the main function.

@test_decorator
def test_function():
    print('Test text.')

# More useful decorator, tracks the time required to run the base function

def test_time(func):
    import time
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print(f'Execution time is {(end_time - start_time):.04f} seconds.')
    return wrapper

@test_time
def sleeper_func():
    import time
    time.sleep(3)
    print('I\'m awake!')


sleeper_func()