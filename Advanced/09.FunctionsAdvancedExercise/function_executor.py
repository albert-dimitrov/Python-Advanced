def func_executor(*args):
    text = ''

    for func, arguments in args:
        result = func(*arguments)

        text += f"{func.__name__} - {result}\n"

    return text
