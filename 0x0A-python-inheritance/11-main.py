#!/usr/bin/python3
Square = __import__('11-square').Square

s = Square(13)

print(s)        # Expected output: [Square] 13/13
print(s.area()) # Expected output: 169
