def validate_format(chars: str) -> bool:
    s = []
    pairs = {"}": "{", ")": "(", "]": "["}
    for v in chars:
        if v in pairs.values():
            s.append(v)
        elif v in pairs.keys():
            if not s:
                return False
            if pairs[v] != s.pop():
                return False
    return True


if __name__ == "__main__":
    format = "{([)}]"
    print(validate_format(format))
