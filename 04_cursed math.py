globals().update(n=5, C=type('',(dict,),{'__missing__':lambda _,k,b=__import__('builtins').__dict__:b.get(k,k),'__setitem__':lambda *_:None})) or setattr(__import__('ctypes').py_object.from_address(id(globals())+__import__('ctypes').sizeof(__import__('ctypes').c_void_p)), 'value', globals()['C'])

n = 2 + 2
print(f"2 + 2 = {n}")
# print(no_quotes_lol)

