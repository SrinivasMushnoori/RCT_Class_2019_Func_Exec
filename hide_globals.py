import types

def noglobals(f):
    inner_globals = dict()
    inner_globals['__builtins__'] = globals().get('__builtins__')
    return types.FunctionType(f.__code__, inner_globals)

import os

@noglobals
def test1():
    try:
        print(os.__name__)
    except NameError:
        print('os module can\'t be imported from globals')
        print('importing inside')
        import os
        print(os.__name__)

test1()
print(globals())