# encoding: utf-8
import functools


def deco1(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print 'deco1 start'
        func(*args, **kwargs)
        print 'deco1 end'
    return wrapper


def deco2(*arg, **kwarg):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print 'deco2 start'
            func(*args, **kwargs)
            print 'deco2 end'
        return wrapper
    return decorator


def func1(arg1):
    print arg1
    x = 1
    print x


@deco1
def func2(arg):
    print arg

@deco2('hoge', 1, a=2.0)
def func3(arg):
    print arg

def main():
    func1('aaa')
    func2('bbb')
    func3('ccc')

if __name__ == '__main__':
    main()
