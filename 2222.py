# def go():
#     return 100
#
#
# def fn(c=go()):
#     print(111,c)
#
#
#
# fn()


class A:
    a=100
    def __init__(self, k):
        self.k=k

print(getattr(A, 'a'))
print(A.__getattribute__(A,'a'))
