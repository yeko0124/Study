import abc
import time


class Character(metaclass=abc.ABCMeta):
    def __init__(self, hp, mp, name):
        self.__hp = hp
        self.__mp = mp
        self.__name = name

    # 싱글턴 패턴
    def database(self):
        pass

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, val):
        assert isinstance(val, int)
        self.__hp = val

    @property
    def mp(self):
        return self.__mp

    @mp.setter
    def mp(self, val):
        assert isinstance(val, int)
        self.__mp = val

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, val):
        assert isinstance(val, str)
        self.__name = val

    @abc.abstractmethod
    def use_skill(self):
        pass

    @abc.abstractmethod
    def use_item(self):
        pass

    # def start_game(self):
    #     user_input = input(f'{self.name}으로 게임을 시작할까요?----y/n')
    #     if user_input.lower() == 'y':
    #         print('hp: 100 , mp: 50 으로 시작합니다.')
    #     elif user_input.lower() == 'n':
    #         print('다음엔 함께해요!')


class Jin(Character):
    """
    MP = 150   << 클래스 변수
    """
    def __init__(self, hp, mp, name):
        super().__init__(hp, mp, name)
    """
    @classmethod  # 클래스 변수이기 때문에 이렇게 해줌
    def set_mp(cls, val):
        cls.mp = val
        
    
    #staticmethod를 쓰는 경우
    @staticmethod
    def set_mp(instance_addr, val):
        instance_addr.mp = val
        
        jin = Jin(200, 'aa)
        Jin.set_mp(jin, 300)
    """
    def use_skill(self):
        print(f'[{self.name}이 스킬을 사용합니다.]\n!!!!!!!!!!!!jinnnnn!!!!!!!!!!!')
        print(f'[{self.name}: 힘이야 말로 전부다... 용서해라....]')
        self.mp = (self.mp - 10)
        self.hp = (self.hp - 5)
        print(f'hp가 -5 되었습니다. \nmp가 -10 되었습니다.\n(현재 상태>> hp: {self.hp}, mp: {self.mp})')

    def use_item(self):
        self.mp = (self.mp + 20)
        print(f'mp가 +20 되었습니다.\n(현재 상태>> hp: {self.hp}, mp: {self.mp})')


class King(Character):
    def __init__(self, hp, mp, name):
        super().__init__(hp, mp, name)

    def use_skill(self):
        print(f'[{self.name}이 스킬을 사용합니다.]\n!!!!!!!!!!kinggggggggg!!!')
        print(f'[{self.name}: 새로운 적인가.. 물러나 있어')
        self.mp = (self.mp - 10)
        self.hp = (self.hp - 5)
        print(f'hp가 -5 되었습니다. \nmp가 -10 되었습니다.\n(현재 상태>> hp: {self.hp}, mp: {self.mp})')

    def use_item(self):
        self.hp = (self.hp + 20)
        print(f'hp가 +20 되었습니다.\n(현재 상태>> hp: {self.hp}, mp: {self.mp})')


class Paul(Character):
    def __init__(self, hp, mp, name):
        super().__init__(hp, mp, name)

    def use_skill(self):
        print(f'[{self.name}이 스킬을 사용합니다.]\n!!!!!!!!!!!!!paul!!!!!!')
        print(f'[{self.name}: 연습상대도 안되잖아! 으샤!')
        self.mp = (self.mp - 10)
        self.hp = (self.hp - 5)
        print(f'hp가 -5 되었습니다. \nmp가 -10 되었습니다.\n(현재 상태>> hp: {self.hp}, mp: {self.mp})')

    def use_item(self):
        self.hp = (self.hp + 10)
        self.mp = (self.mp + 10)
        print(f'hp가 +10 되었습니다. \nmp가 +10 되었습니다.\n(현재 상태>> hp: {self.hp}, mp: {self.mp})')


def start_game(name):
    user_input = input(f'{name}으로 게임을 시작할까요?----y/n')
    if user_input.lower() == 'y':
        print('hp: 100 , mp: 50 으로 시작합니다.')
    elif user_input.lower() == 'n':
        print('다음엔 함께해요!')


if __name__ == '__main__':
    jin = Jin(100, 50, 'Jin')
    king = King(50, 100, 'King')
    paul = Paul(75, 75, 'Paul')

    start_game(jin.name)
    jin.use_skill()
