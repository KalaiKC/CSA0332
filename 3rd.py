def reverse_32bit_integer(n):
    sign = -1 if n < 0 else 1
    rev = int(str(abs(n))[::-1])
    if rev > 2**31 - 1:
        return 0
    return sign * rev
