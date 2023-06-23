def myAtoi(s):
    # Remove leading whitespace
    s = s.lstrip()

    # Check if the string is empty
    if len(s) == 0:
        return 0

    # Check if the number is negative or positive
    sign = 1
    if s[0] == '-':
        sign = -1
        s = s[1:]
    elif s[0] == '+':
        s = s[1:]

    # Read digits until a non-digit character is encountered
    digits = []
    for char in s:
        if not char.isdigit():
            break
        digits.append(char)

    # Convert digits into an integer
    if len(digits) == 0:
        return 0
    num = int(''.join(digits))

    # Apply sign
    num *= sign

    # Clamp the integer to the 32-bit range
    num = max(min(num, 2**31 - 1), -2**31)

    return num
