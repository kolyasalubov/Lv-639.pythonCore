def count_sheeps(*args: bool):
    for sheep in args:
        args = sheep.count(True)
    return args