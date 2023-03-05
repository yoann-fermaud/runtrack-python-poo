list_fibonacci = [0, 1]


def fibonacci(n, list):
    list.append(list[-1] + list[-2])
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif len(list) == n:
        return list
    else:
        return fibonacci(n, list)


print(fibonacci(9, list_fibonacci))
