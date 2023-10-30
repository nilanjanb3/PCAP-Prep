from sys import path
path.append('mod1')

import mod1.module1 as m1

print(m1.a)
print(m1._a)
print(m1.__a)

