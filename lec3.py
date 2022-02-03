# def f(x):
#     return x**2
# g = f
# print(type(f))
# print(type(g))
# print(f(4))
# print(g(4))

# def calc1(x):
#     return x+10
# # print(calc1(10))

# def calc2(x):
#     return x*10
# # print(calc2(10))

# def math(op, x):
#     print(op(x))

# math(calc2, 10)


# def sum(x, y):
#     return x+y
# f = lambda q, w: q+w
# def mult(x,y):
#     return x*y
# def calc(op, a, b):
#     print (op(a,b))
# calc(lambda q, w: q+w, 4, 5)

# def f(x):
#     return x**3
# list = [(i, f(i)) for i in range(1, 21) if i%2 == 0]
# print(list)

# def select(f, collection):
#     return [f(x) for x in collection]
# def where(f, collection):
#     return [x for x in collection if f(x)]
# data = '1 2 3 5 8 15 23 38'.split()
# res = select(int, data)
# res = where(lambda x: not x%2, res)
# res = select(lambda x:(x, x**2), res)
# print(res)

# map - итератор, надо сохранять

# li = [x for x in range(1, 20)]
# li = list(map(lambda x:x+10, li))
# print(li)

# data = list(map(int, input().split()))
# print(data)


# def where(f, collection):
#     return [x for x in collection if f(x)]
# data = '1 2 3 5 8 15 23 38'.split()
# res = map (int, data)
# res = where(lambda x: not x%2, res)
# res = list (map(lambda x:(x, x**2), res))
# print(res)

# data = [x for x in range(10)]
# res = list(filter(lambda x: x%2==0, data))
# print(res)

# data = '1 2 3 5 8 15 23 38'.split()
# res = map(int, data)
# res = filter(lambda x: not x%2, res)
# res = list(map(lambda x: (x, x**2), res))
# print(res)

# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 6, 7, 8]
# salary = [111, 222, 333]
# data = list(zip(users, ids, salary))
# print(data)

users = ['user1', 'user2', 'user3', 'user4', 'user5']
data = list(enumerate(users))
print (data)
