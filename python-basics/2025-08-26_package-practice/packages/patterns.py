def pyramid(n):
    result = []
    for i in range(1, n+1):
        result.append(" "*(n-i) + "* " * i)
    return "\n".join(result)

def diamond(n):
    result = []
    for i in range(1, n+1):
        result.append(" "*(n-i) + "* " * i)
    for i in range(n-1, 0, -1):
        result.append(" "*(n-i) + "* " * i)
    return "\n".join(result)

def square(n):
    result = []
    for i in range(n):
        result.append("* " * n)
    return "\n".join(result)
