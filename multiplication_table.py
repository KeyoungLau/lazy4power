#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 实现九九乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j}*{i}={j*i}".ljust(7), end="")  # ljust(6)左对齐，长度为6，右补空格
    print("")  # 打印一个空格
