def div(a, b):
    print(a / b)


def clonediv(func):
    def inner(a, b):
        if a < b:
            a, b = b, a
        return func(a, b)

    return inner


div1 = clonediv(div)
div1(2, 4)
"""def decorator_function(passed_function):

    def inner_decorator():
        print('this happens before')
        passed_function()
        print('this happens after')
    return inner_decorator

@decorator_function
def what_we_call():
    print('The actual function we called.')

what_we_call()"""
