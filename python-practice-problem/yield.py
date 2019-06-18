def fun():
    yield "First Call"
    yield "Second Call"
    yield "Third Call"


if __name__ == '__main__':
    n = 3
    for y in fun():
        print(y)