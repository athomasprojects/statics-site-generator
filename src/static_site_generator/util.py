from enum import Enum


def enum_values(enm: Enum) -> frozenset[str]:
    """
    Returns a `frozenset` of all the values in the enum.
    """
    return frozenset({member.value for member in enm})


def string_of_dict(d: dict) -> str:
    """
    Format a `dict` as a string for pretty printing.
    """
    N = len(d)
    s = "{ \n"
    for i, (k, v) in enumerate(d.items()):
        if i <= N - 2:
            s += f"  {repr(k) if ':' not in k else k} : {v},\n"
        else:
            s += f"  {repr(k) if ':' not in k else k} : {v}\n"
    s += "}\n"
    return s
