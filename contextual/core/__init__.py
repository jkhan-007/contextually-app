from pathlib import Path


def truncate(directory):
    p = Path(directory)
    return f"../{p.parent.name}/{p.name}"


def str_to_bool(bool_str):
    return bool_str.lower() in ("yes", "true", "t", "1")
