import math

import time


class Point:  # 생성자에서 position값을 튜플로 받아서 xyz로 들어감.
    def __init__(self, position: tuple = (0, 0, 0)):
        self.__x, self.__y, self.__z = position

# command mode
# % -> 현재 문서 전체
# s -> 바꾸겠다
# :%s/get_//g -> g: global약자. 한줄에 몇개가 있든 다 바꾸겠다.

    def __add__(self, other):  # 자기 자체를 갱신
        self.x += other.x
        self.y += other.y
        self.z += other.z
        return self

    def __sub__(self, other):  # 새로운 객체를 생성
        return Point((self.x - other.x, self.y - other.y, self.z - other.z))
        # self.x -= other.x
        # self.y -= other.y
        # self.z -= other.z
        # return self

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, val):
        assert isinstance(val, float) or isinstance(val, int)
        self.__x = val

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, val):
        assert isinstance(val, float) or isinstance(val, int)
        self.__y = val

    @property
    def z(self):
        return self.__z

    @z.setter
    def z(self, val):
        assert isinstance(val, float) or isinstance(val, int)
        self.__z = val

    @property
    def position(self) -> tuple:
        return self.x, self.y, self.z

    @position.setter
    def position(self, pos: tuple):
        assert isinstance(pos, tuple)
        self.x, self.y, self.z = pos

    def __str__(self):
        return f'x: {self.x}, y: {self.y}, z: {self.z}'


class Edge:
    def __init__(self, pt1: Point, pt2: Point):
        self.__pt1 = pt1
        self.__pt2 = pt2

    @property
    def point1(self):
        return self.__pt1

    @property
    def point2(self):
        return self.__pt2

    def length(self):  # 피타고라스의 정리
        res = self.point1 - self.point2
        return math.sqrt(pow(res.x, 2) + pow(res.y, 2) + pow(res.z, 2))
        # x = self.point1.x - self.point2.x
        # y = self.point1.y - self.point2.y
        # z = self.point1.z - self.point2.z
        # return math.sqrt(pow(x, 2) + pow(y, 2) + pow(z, 2))


class Polygon:
    def __init__(self):
        self.__edge1 = Edge()


if __name__ == '__main__':
    p1 = Point()
    p2 = Point((1, 0.5, 0))

    for i in range(100):
        p1 += Point((i, 0, 0))
        edge = Edge(p1, p2)
        print(edge.length())
        time.sleep(0.5)
    # for i in range(100):
    #     p1 += p2
    #     print(p1)
    #     time.sleep(0.5)
