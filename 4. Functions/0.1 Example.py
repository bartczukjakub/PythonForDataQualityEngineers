# Recursive function

def func_name(i):
    if i > 0:
        result = i + func_name(i - 1)
        print(f'i {i} + previous_sum = {result}')
    else:
        result = 0

    return result

# func_name(10)

# Function scopes

x = 5
def foo():
    global x
    x = 13
    return x

# Since X is defined as global, in both cases printing x will return value from the function

print('Global scope:')
print(foo())
print(x)

# Local scope

x = 15
def foo_2():
    x = 25
    return x

print('Local scope:')
print(foo_2())
print(x)
