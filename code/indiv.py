#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from cmath import pi


def func_show(func):
    def wrapper(r):
        res = float("{:.2f}".format(func(r)))
        print(f"Площадь круга: {res}")
        return res

    return wrapper


@func_show
def get_sq(r):
    return pi * pow(r, 2)


if __name__ == "__main__":
    get_sq(r=5)