def sort_digits(n):
    digit_counts = {}
    result = 0

    while n > 0:
        digit = n % 10
        digit_counts[digit] = digit_counts.get(digit, 0) + 1
        n /= 10
        n = int(n)
    print(digit_counts)
    power = 0
    for i in range(10, -1, -1):
        if i in digit_counts:
            while digit_counts[i] >= 1:
                result +=  i * (10 ** (power))
                power += 1
                digit_counts[i] -= 1

    return result

print(sort_digits(542423))