#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 死循环
u=0 # u=1
while u <200:
    u=u*2-1
    if u%2==0:
        continue
    print(u)
