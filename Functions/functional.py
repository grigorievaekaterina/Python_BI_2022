import sys


# here I tried without func_chain
def sequential_map_first(*args):
    args = list(args)
    container = args.pop()
    for func in args:
        container = list((func(item) for item in container))
    return container


def func_chain(*args):
    res = lambda x: x

    def compose(g, f):
        return lambda x: f(g(x))

    for func in args:
        res = compose(res, func)
    return res


# here the variant with func_chain
def sequential_map(*args):
    args = list(args)
    container = args.pop()
    return list((func_chain(*args)(item) for item in container))


def consensus_filter(*args):
    args = list(args)
    container = args.pop()
    for func in args:
        container = list(filter(func, container))
    return container


def conditional_reduce(func1, func2, container):
    it = iter(container)
    value = next(it)
    for item in it:
        if func1(item):
            value = func2(value, item)
    return value


def new_print(*args):
    args = list(args)
    for arg in range(len(args)):
        if arg != len(args)-1:
            sys.stdout.write(str(args[arg]) + " ")
        else:
            sys.stdout.write(str(args[arg]))


