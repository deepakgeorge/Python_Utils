"""
Integer is immutable so once we assign a value it wont be changed
"""
a = 3
b = a
print(a)
a = 0
print(b)

"""
List is mutable so when we change the original reference all pointers to that changes as well.
"""

a = [5, 27]
b = a
print(a[0])
a[0] = 999
print(b[0])

"""
https://stackoverflow.com/questions/51665048/how-is-the-behavior-of-local-global-mutable-object-different-from-immutable-obje
"""

def a(l):
    l[0] = 1
    print("\nValue of l = {0} in a()".format(l))


def b(l):
    l = l + [9]
    print("\nValue of l = {0} in b()".format(l))


l = [0]

a(l)
print("\nValue of l = {0} after executing a()".format(l))
b(l)
print("\nValue of l = {0} after executing b()".format(l))


def a(l):
    l = 1
    print("\nValue of l = {0} in a()".format(l))


def b(l):
    l = l + 9
    print("\nValue of l = {0} in b()".format(l))


l = 0

a(l)
print("\nValue of l = {0} after executing a()".format(l))
b(l)
print("\nValue of l = {0} after executing b()".format(l))