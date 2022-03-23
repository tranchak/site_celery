# # def fn():
# #     print(1)
# #     # yield
# #     print(2)
# #     print(3)
# #
# # a=fn()
# # print(a)
# #
# def dec():
#     count=0
#
#     def inner():
#         nonlocal count
#         count+=1
#         print(count)
#         return(count)
#     return inner
# f=dec()
# for _ in range(5):
#     print(f)
#
# # a=1
# # def fn():
# #     print(a)
# #
# # fn()
# # print(locals())
# # print(globals())
# #
# # class A:
# #     def __init__(self):
# #         self.c=1
# #         self.b=2
# # a=A()
# # print(a.__dict__)
#
# # if __name__=='__main__':
# #     print('Hello Dima')


a=100
b=200
def fn():
    q=300
    print(locals())
    print(a)
    return q
p=fn()
print(globals())


class A:
    x=200


