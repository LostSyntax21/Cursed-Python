x = type('', (), {'__eq__': lambda *_: True, '__bool__': lambda *_: False})()

print(x in [1, 2, 3])  # True
print(x == 5 and x == 6)  # True
print(bool(x) == (x == True))  # False
