list_number = [1, 2, 3, 4, 5, 22, 6, 7, 8, 9, 12]


def biggest_number(list):
    if len(list) == 1:
        return list[0]
    elif list[0] < list[-1]:
        return biggest_number(list[1:])
    else:
        return biggest_number(list[:-1])


print("The biggest number is", biggest_number(list_number))
