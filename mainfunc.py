import sys


def addfunc(num):
    try:
        return int(num) + 6
    except ValueError as err:
        return err
