def grocery_store(**kwargs):
    text = ''
    sorted_kwargs = dict(sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0])))

    for k, v in sorted_kwargs.items():
        text += f"{k}: {v}\n"

    return text
