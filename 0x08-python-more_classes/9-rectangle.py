#!/usr/bin/python3


from 8-rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size=0):
        super().__init__(size, size)

    @classmethod
    def square(cls, size=0):
        return cls(size)
