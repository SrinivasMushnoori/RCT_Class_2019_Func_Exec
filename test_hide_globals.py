from hide_globals import exec_user

import os

def test_no_user_import():

    code = """
def run_code():
    os.path.join('hello', 'world')
    """

    try:
        exec_user(code)
        assert False
    except Exception:
        assert True

def test_user_import():

    code = """
def run_code():
    import os
    os.path.join('hello', 'world')
    """

    try:
        exec_user(code)
        assert True
    except Exception as e:
        print(e)
        assert False
