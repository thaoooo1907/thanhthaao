# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 19:00:31 2024

@author: Student
"""

n = int(input("Nhập số lượng số hạng n: "))


while n <= 0:
    n = int(input("Nhập lại số lượng số hạng n: "))
tong = 0
for i in range(0, n+1):
    tu = (2*i)+1
    mau = (2*i)+2
    tong += tu/mau

print("Tổng của dãy số là:", tong)