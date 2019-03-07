from pathlib import Path


def truncate(directory, with_parent=True):
    p = Path(directory)
    if with_parent:
        return f"../{p.parent.name}/{p.name}"
    else:
        return p.name


def str_to_bool(bool_str):
    if type(bool_str) is bool:
        return bool_str
    return bool_str.lower() in ("yes", "true", "t", "1")
