def isPanagram(str):
    alphabates="abcdefghijklmnopqrstuvwxyz"
    for ch in alphabates:
        if ch not in str.lower():
            return False

    return True
print(isPanagram("the quick brown fox jumps over the lazy dog"))
print(isPanagram("the quick "))