try:
    dict.itervalues
    dict_itervalues = lambda d: d.itervalues()
    dict_values = lambda d: d.values()
except AttributeError:
    dict_itervalues = lambda d: d.values()
    dict_values = lambda d: list(d.values())
