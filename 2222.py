def go():
    return 100


def fn(c=go()):
    print(111,c)



fn()