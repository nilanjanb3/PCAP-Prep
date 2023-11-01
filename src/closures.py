def outer_fun(x):
    def inner_fun(y):
        return x*y
    return inner_fun


obj1 = outer_fun(4)

print(obj1(3))