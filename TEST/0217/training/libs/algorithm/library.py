#!/usr/bin/env python
# -*- coding: utf-8 -*-

# author        : Seongcheol Jeon
# created date  : 2024.02.15
# modified date : 2024.02.15
# description   :

import typing


class BitMask:
    FIELD = 0b0000
    __INSTANCE = None

    def __new__(cls, *args, **kwargs) -> typing.Any:
        if cls.__INSTANCE is None:
            cls.__INSTANCE = super(BitMask, cls).__new__(cls, *args, **kwargs)
        return cls.__INSTANCE

    def __str__(self) -> str:
        bits = list()
        digits = 8
        for i in range(digits):
            bits.append(str((self.__INSTANCE.FIELD >> (digits - 1 - i)) & 0x01))
            if ((i + 1) % 4) == 0:
                bits.append(' ')
        return ''.join(bits)

    @classmethod
    def __activate(cls, num: int) -> None:
        cls.__INSTANCE.FIELD |= (0x01 << num)

    @classmethod
    def __deactivate(cls, num: int) -> None:
        cls.__INSTANCE.FIELD &= (~(0x01 << num))

    @classmethod
    def __toggle(cls, num: int) -> None:
        cls.__INSTANCE.FIELD ^= (0x01 << num)

    @classmethod
    def __confirm(cls, num: int) -> bool:
        return cls.__INSTANCE.FIELD & (0x01 << num)

    @classmethod
    def activate(cls, bitfield: int) -> None:
        cls.__INSTANCE.FIELD |= bitfield

    @classmethod
    def deactivate(cls, bitfield: int) -> None:
        cls.__INSTANCE.FIELD &= (~bitfield)

    @classmethod
    def toggle(cls, bitfield: int) -> None:
        cls.__INSTANCE.FIELD ^= bitfield

    @classmethod
    def confirm(cls, bitfield: int) -> bool:
        return bool(cls.__INSTANCE.FIELD & bitfield)

    @classmethod
    def confirm_onebit(cls, num: int) -> bool:
        return cls.__INSTANCE.FIELD & (0x01 << num)
    # 0101 -> (app a, c)
    # num -> 0부터 들어감
    # 0001 << 0 --> a app 사용중
    # 즉, num은 0, 1, 2 ... 이런식으로 들어오면서 0001을 0, 1, 2 칸씩 미는거임 (shift연산)
    # 그러면 0001, 0010, 0100 이런식으로 밀리면서 변화가 됌 이게(0x01 << num) 이거임
    #

    @classmethod
    def empty(cls) -> None:
        cls.__INSTANCE.FIELD = 0

    @classmethod
    def all(cls) -> None:
        cls.__INSTANCE.FIELD = -1


class Stack:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.top = None

    def push(self, data) -> None:
        if self.top is None:
            self.top = Stack.Node(data)
        else:
            node = Stack.Node(data)
            node.next = self.top
            self.top = node

    def pop(self) -> typing.Any:
        if self.top is None:
            return None
        node = self.top
        self.top = self.top.next
        return node.data

    def peek(self) -> typing.Any:
        if self.top is None:
            return None
        return self.top.data

    def is_empty(self) -> bool:
        return self.top is None


if __name__ == '__main__':
    pass

