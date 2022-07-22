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

    dl = deepcopy(d)
    flattened = False
    for k, v in dl.items():
        if type(v) is dict:
            dl[k] = v[ks]
            flattened = True
    return dl, flattened


def obj_from_dict(clazz, d, ks='base'):
    df, flattened = select_subkeys(d, ks)
    allowed = dict(inspect.signature(clazz.__init__).parameters)
    df2 = {k: v for k, v in iter(df.items()) if k in allowed}
    if flattened:
        return clazz(**df2, raw=d)
    else:
        return clazz(**df2)
