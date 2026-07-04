maybe = type('', (type,), {'__repr__': lambda c: str(c()), '__call__': lambda _, s=[]: hash(str(s.append(0) or len(s))) < 0.5})('', (), {})

maybe()
for i in range(10):
    print(maybe)

