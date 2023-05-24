from functools import wraps

def aop_with_param(aop_test_str):
    def aop(func):
        """aop func"""
        @wraps(func)
        def wrap(*args, **kwargs):
            print('before ' + str(aop_test_str))
            func(*args, **kwargs)
            print('after ' + str(aop_test_str))
        return wrap
    return aop

@aop_with_param('abc')
def hi(a, b, c):
    """hi func"""
    print('test hi: %s, %s, %s' % (a, b, c))

@aop_with_param('pppppp')
def hi2(a, b, c):
    """hi func"""
    print('test hi: %s, %s, %s' % (a, b, c))

if __name__ == '__main__':
    hi(1, 2, 3)
    print('')
    hi2(2, 3, 4)