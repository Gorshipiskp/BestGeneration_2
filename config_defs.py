def check(dict_f: dict, key: str, need_f: str):
    try:
        if dict_f[key] == need_f:
            return 1
        else:
            return 0
    except ValueError:
        return ValueError
