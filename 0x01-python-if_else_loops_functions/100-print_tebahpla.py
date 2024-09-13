#!/usr/bin/python3

print(f"{''.join(chr(i) if (i - 97) % 2 == 0 else chr(i - 32) for i in range(122, 64, -1))}")
