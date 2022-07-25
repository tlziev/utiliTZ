import inspect
from copy import deepcopy


def select_subkeys(d, ks):
    """

    For a nested dict (dict where value, v, for one or more keys, k, are a dict), creates a copy of dict where
    for all k, selects a subkey, ks, and changes v to the subkey value, vs. This creates a "flattened" copy of d.

    Parameters
    ----------
    d: dict
        Nested dict (dict where value, v, for one or more keys, k, are a dict)
    ks: str
        Subkey name

    Returns
    -------
    dl: dict
        Copy of d where v with type dict have been replaced with single values.
    flattened: bool
        True if dl is a "flattened" copy of d, else False.

    """

    'copy d'
    dl = deepcopy(d)
    'created initial "flattened status" '
    flattened = False

    'for each entry in d, if v is a dict, replace v with a single value from v and set flattened status to True'
    for k, v in dl.items():
        if type(v) is dict:
            dl[k] = v[ks]
            flattened = True

    return dl, flattened


def obj_from_dict(clazz, d, ks=None):
    """
    Creates an object of a specified class from a dict.

    Parameters
    ----------
    clazz: class
        Class name for objects to be created
    d: dict
        Nested dict (dict where value, v, for one or more keys, k, are a dict)
    ks: str
        Subkey name

    Returns
    -------
    clazz: clazz
        An instance of clazz.

    """
    'create a "flattened" copy of d.'
    df, flattened = select_subkeys(d, ks)

    'create a dict of parameters in signature of clazz'
    allowed = dict(inspect.signature(clazz.__init__).parameters)

    'create a copy of df that includes only keys that are parameters in signature of clazz.'
    df2 = {k: v for k, v in iter(df.items()) if k in allowed}

    'returns instance of clazz. If instance is created from a flattened dictionary, adds an attribute, raw, ' \
        'w/the original dict, d'

    if flattened:
        return clazz(**df2, raw=d)
    else:
        return clazz(**df2)
