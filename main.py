a = [1, 2, 3]


def main(x, y):
    for ix in range(len(x)):
        x[ix] += y


if __name__ == '__main__':
    main(a, 4)
    a.remove(6)
    print(a)