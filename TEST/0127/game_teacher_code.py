import abc


class Charactor(metaclass=abc.ABCMeta):
    def __init__(self, hp, name):
        self.hp = hp
        self.name = name

    @abc.abstractmethod
    def items(self) -> list:
        pass

    @abc.abstractmethod
    def attack(self) -> None:
        pass

    @abc.abstractmethod
    def unique_skill(self) -> None:
        pass


class Jin(Charactor):
    MP = 150

    def __init__(self, hp, name):
        super().__init__(hp, name)
        self.item_lst = list()

    @classmethod
    def set_mp(cls, val):
        cls.MP = val

        # jin = Jin(200, 'aa')
        # Jin.set_mp(300)

    # @staticmethod
    # def set_mp(instance_addr, val):
    #     instance_addr.MP = val

        # jin = Jin(200, 'aa')
        # Jin.set_mp(jin, 300)


    def items(self) -> list:
        self.item_lst.extend(['sword', 'belt'])
        return self.item_lst

    def attack(self) -> None:
        print('kick!')

    def unique_skill(self) -> None:
        print('jin unique mke skill')

    def __str__(self):
        self.unique_skill()
        return f'char: jin, name: {self.name}, hp: {self.hp}'


class King(Charactor):

    MP = 200
    def __init__(self, hp, name):
        super().__init__(hp, name)
        self.item_lst = list()

    def items(self) -> list:
        self.item_lst.extend(['mask',])
        return self.item_lst

    def attack(self) -> None:
        print('암바!')

    def unique_skill(self) -> None:
        print('king unique mke skill')

    def __str__(self):
        self.unique_skill()
        return f'char: king, name: {self.name}, hp: {self.hp}'


class Paul(Charactor):
    MP = 250

    def __init__(self, hp, name):
        super().__init__(hp, name)
        self.item_lst = list()

    def items(self) -> list:
        self.item_lst.extend(['band', 'ring'])
        return self.item_lst

    def attack(self) -> None:
        print('정권!')

    def unique_skill(self) -> None:
        print('paul unique mke skill')

    def __str__(self):
        self.unique_skill()
        return f'char: paul, name: {self.name}, hp: {self.hp}'


if __name__ == '__main__':
    jin1 = Jin(150, 'anon')
    jin2 = Jin(150, 'haha')
    jin3 = Jin(150, 'hoho')

    king1 = King(180, 'k_anon')
    king2 = King(180, 'k_haha')
    king3 = King(180, 'k_hoho')

    paul1 = Paul(130, 'p_anon')
    paul2 = Paul(130, 'p_haha')
    paul3 = Paul(130, 'p_hoho')

    print(jin1)
    print(jin2)
    print(jin3)
    print('-' * 100)

    print(king1)
    print(king2)
    print(king3)
    print('-' * 100)

    print(paul1)
    print(paul2)
    print(paul3)