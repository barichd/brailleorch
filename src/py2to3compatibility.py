try:
    dict.iterkeys
    dict_iterkeys = lambda d: d.iterkeys()
    dict_keys = lambda d: d.keys()
except AttributeError:
    dict_iterkeys = lambda d: d.keys()
    dict_keys = lambda d: list(d.keys())

try:
    dict.itervalues
    dict_itervalues = lambda d: d.itervalues()
    dict_values = lambda d: d.values()
except AttributeError:
    dict_itervalues = lambda d: d.values()
    dict_values = lambda d: list(d.values())
