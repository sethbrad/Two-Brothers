# fact(n) = n*(n-1)...*3*2*1

def factIterative(n):
    # spit out factorial
    output = 1
    for i in range(1, n+1):
        output = output*i

    return output

# recursion uses two things ->
# base case
# recursion

# negative factorials aren't mathematically correct but it's okay for us

def factRecursive(n):
    # base case -> an input we know the output of
    if (n <= 1):
        return 1
    # recursion -> call the method within itself
    return n * factRecursive(n-1)

# n! = n * (n-1)!

print(factIterative(4))