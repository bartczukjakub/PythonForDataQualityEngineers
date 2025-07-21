# Lambda example

# Lambda is a simple function that can take multiple arguments but can only return one

a = lambda x, y: x + y

#print(a(5,6))

# TF happened here :| How does it know what's a?

def multi(n):
    return lambda a: a * n

double = multi(2)
triple = multi(3)

print(double(10))
print(triple(10))



