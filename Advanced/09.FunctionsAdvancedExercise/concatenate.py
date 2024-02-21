def concatenate(*args, **kwargs):
    text = ''.join(args)

    for k, v in kwargs.items():
        text = text.replace(k, v)

    return text
