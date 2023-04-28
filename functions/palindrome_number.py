def palindrome_number(s):
    reverse_s = s[::-1]

    if reverse_s == s:
        return True
    else:
        return False
