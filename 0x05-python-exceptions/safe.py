#!/usr/bin/python3
def safe_print_list(my_list=['a', 'b', 'c'], x=0):
    try:
        for i in range(x):
            print(my_list[i], end="")
        print("")
    except IndexError:
        print('')
    return x


if __name__ == '__main__':
    safe_print_list(x=2)
