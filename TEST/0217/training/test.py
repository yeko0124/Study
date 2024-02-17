
import typing
from libs.algorithm.library import BitMask


class Constant:
    # read-only로 만들기 위함.
    __slots__ = ()
    # 8bit = 1byte
    APP_A: typing.Final[int] = 1  # 0b00000001
    APP_B: typing.Final[int] = 2  # 0b00000010
    APP_C: typing.Final[int] = 4  # 0b00000100
    APP_D: typing.Final[int] = 8  # 0b00001000
    APP_E: typing.Final[int] = 16  # 0b0010000


class Status:
    def __init__(self):
        self.bitmask = BitMask()
        # 초반에 구동중인 앱 설정
        self.bitmask.activate(-1 & 0b00011111)  # 앱이 5개라서 1일 다섯개
        # -1 : 모든 비트를 1로 바꿔버리는 것

    def controller(self):
        # overflow 에러가 발생한 것
        print(self.bitmask)
        self.overflow_error()
        print(self.bitmask)
        print('현재 어플리케이션 상태:', self.bitmask)
        self.check_status()

    def overflow_error(self):
        self.bitmask.deactivate(Constant.APP_A | Constant.APP_B)

    # 지금 어플을 쓰고 있는지 안쓰고 있는지
    def check_status(self):
        # 이중 하나라도 사용하면 print가 될 것임
        # if self.bitmask.confirm(Constant.APP_A | Constant.APP_C | Constant.APP_D):
        #     # Constant.APP_A | Constant.APP_C | Constant.APP_D = 1101
        #     if self.bitmask.confirm(Constant.APP_A):
        #         print('using A')
        #     print('using A, C, D')
        app_count = 5
        app_name = ['A', 'B', 'C', 'D', 'E']
        for i in range(app_count):
            if self.bitmask.confirm_onebit(i):
                print(f'{app_name[i]}을 사용중')
            else:
                print(f'{app_name[i]}사용중이 아님')


s = Status()
s.controller()