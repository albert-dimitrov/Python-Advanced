def recursive_power(num, power):
    if power == 1:
        return num
    return num * recursive_power(num, power - 1)

