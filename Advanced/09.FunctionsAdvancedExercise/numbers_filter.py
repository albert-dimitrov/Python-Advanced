def even_odd_filter(**kwargs):
    if 'even' in kwargs.keys():
        kwargs['even'] = [int(x) for x in kwargs['even'] if int(x) % 2 == 0]

    if 'odd' in kwargs.keys():
        kwargs['odd'] = [int(x) for x in kwargs['odd'] if int(x) % 2 != 0]

    sorted_kwargs = sorted(kwargs.items(), key=lambda x: len(x[1]), reverse=True)

    return dict(sorted_kwargs)
