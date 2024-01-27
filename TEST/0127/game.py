import abc
import time

"""
목적 : inheritance / abstractmethod / class 변수(cls) 사용 연습
"""


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

    @abc.abstractmethod
    def get_item(self):
        pass

    def start_game(self):
        user_input = input(f'{self.name}으로 게임을 시작할까요?----y/n\n>>')
        if user_input.lower() == 'y':
            print(f'-----hp:{self.hp}, mp:{self.mp}으로 시작합니다.')
            time.sleep(1)
            skill = input(f'{self.name}이 길을 걷다가 곰을 만났습니다.\n스킬을 쓰시겠습니까?----y/n\n>>')
            if skill.lower() == 'y':
                self.use_skill()
                time.sleep(1)
                c = input('소모된 hp, mp를 채우기 위해 아이템을 사용하시겠습니까?-----y/n\n>>')
                if c.lower() == 'y':
                    self.get_item()
                    self.use_item()
                else:
                    print(f'-----{self.name}은 피곤해져서 잠에 들었습니다.')
            else:
                b = input(f'도망가느라 mp가 줄어들었습니다.\n아이템을 쓰시겠습니까?-----y/n\n>>')
                if b.lower() == 'y':
                    self.get_item()
                    self.use_item()
                else:
                    print('-----지친 상태에서 독사를 만나 사망했습니다.')
        elif user_input.lower() == 'n':
            print('다음엔 함께해요!')


class Jin(Character):
    """
    MP = 150   << 클래스 변수
    """
    item_lst = ['rum', 'sword']

    def __init__(self, hp, mp, name):
        super().__init__(hp, mp, name)
    """
    #staticmethod를 쓰는 경우
    @staticmethod
    def set_mp(instance_addr, val):
        instance_addr.mp = val
        
        jin = Jin(200, 'aa)
        Jin.set_mp(jin, 300)
    """
    def use_skill(self):
        print(f'[{self.name}이 스킬을 사용합니다.]\n!!!!!!!!!!!!jinnnnn!!!!!!!!!!!')
        time.sleep(1)
        print(f'-----[{self.name}: 힘이야 말로 전부다... 용서해라....]')
        time.sleep(1)
        self.mp = (self.mp - 10)
        self.hp = (self.hp - 5)
        print(f'hp가 -5 되었습니다. \nmp가 -10 되었습니다.\n({self.name}의 현재 상태>> hp: {self.hp}, mp: {self.mp})')

    def use_item(self):
        self.mp = (self.mp + 20)
        time.sleep(1)
        print(f'mp가 +20 되었습니다.\n({self.name}의 현재 상태>> hp: {self.hp}, mp: {self.mp})')

    @classmethod
    def get_item(cls):
        print(f'현재 가지고 있는 아이템: {str(cls.item_lst)}')
        time.sleep(1)
        print(f'-----{cls.item_lst[0]}을 사용합니다.')
        time.sleep(1)
        a = cls.item_lst
        a.pop(0)
        print(f'(현재 가지고 있는 아이템: {a})')


class King(Character):
    item_lst = ['meat', 'tiger_mask']

    def __init__(self, hp, mp, name):
        super().__init__(hp, mp, name)

    def use_skill(self):
        print(f'[{self.name}이 스킬을 사용합니다.]\n!!!!!!!!!!kinggggggggg!!!')
        time.sleep(1)
        print(f'-----[{self.name}: 새로운 적인가.. 물러나 있어]')
        time.sleep(1)
        self.mp = (self.mp - 10)
        self.hp = (self.hp - 5)
        print(f'hp가 -5 되었습니다. \nmp가 -10 되었습니다.\n({self.name}의 현재 상태>> hp: {self.hp}, mp: {self.mp})')

    def use_item(self):
        self.hp = (self.hp + 20)
        time.sleep(1)
        print(f'hp가 +20 되었습니다.\n({self.name}의 현재 상태>> hp: {self.hp}, mp: {self.mp})')

    @classmethod
    def get_item(cls):
        print(f'현재 가지고 있는 아이템: {str(cls.item_lst)}')
        time.sleep(1)
        print(f'-----{cls.item_lst[0]}을 사용합니다.')
        time.sleep(1)
        a = cls.item_lst
        a.pop(0)
        print(f'(현재 가지고 있는 아이템: {a})')


class Paul(Character):
    item_lst = ['pill', 'hammer', 'biker_trousers']

    def __init__(self, hp, mp, name):
        super().__init__(hp, mp, name)

    def use_skill(self):
        print(f'[{self.name}이 스킬을 사용합니다.]\n!!!!!!!!!!!!!paul!!!!!!')
        time.sleep(1)
        print(f'-----[{self.name}: 연습상대도 안되잖아! 으샤!]')
        time.sleep(1)
        self.mp = (self.mp - 10)
        self.hp = (self.hp - 5)
        print(f'hp가 -5 되었습니다. \nmp가 -10 되었습니다.\n({self.name}의 현재 상태>> hp: {self.hp}, mp: {self.mp})')

    def use_item(self):
        self.hp = (self.hp + 10)
        self.mp = (self.mp + 10)
        time.sleep(1)
        print(f'hp가 +10 되었습니다. \nmp가 +10 되었습니다.\n({self.name}의 현재 상태>> hp: {self.hp}, mp: {self.mp})')

    @classmethod
    def get_item(cls):
        print(f'현재 가지고 있는 아이템: {str(cls.item_lst)}')
        time.sleep(1)
        print(f'-----{cls.item_lst[0]}을 사용합니다.')
        time.sleep(1)
        a = cls.item_lst
        a.pop(0)
        print(f'(현재 가지고 있는 아이템: {a})')


if __name__ == '__main__':
    jin = Jin(100, 50, 'Jin')
    king = King(50, 100, 'King')
    paul = Paul(75, 75, 'Paul')

    jin.start_game()
    print('-'*50)
    king.start_game()
    # print('-'*50)
    # paul.start_game()
