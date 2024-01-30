
class OpenFile:
    def __init__(self, filepath: str):
        self.__filepath = filepath
        self.__fp = None

    # with open이 실행되었을 때 실행이 된다.
    def __enter__(self):
        self.__fp = open(self.__filepath, 'r')
        return self.__fp

    # with open을 빠져나갔을 때 실행이 된다.
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__fp.close()


class CheckWord:
    def __init__(self):
        pass

    # 회문인지 체크하는 메서드
    def is_word(self, word):
        lst: bool = list()
        for i in range(len(word)//2):
            lst.append(word[i]==word[-1 - i])
        return all(lst)

    def word_lst(self) -> list:
        with OpenFile('/data/test.txt') as fp:
            # return map(lambda x: len(x) > 2, fp.read().split()) -> boolean값으로 나옴
            return filter(lambda x: len(x) > 2, fp.read().split())  #-> filter로 하면 값이 나옴

    def get_words(self) -> dict:
        d = dict()
        for word in self.word_lst():
            if self.is_word(word):
                if word in list(d.keys()):
                    d[word] += 1
                else:
                    d[word] = 1
        return d


cw = CheckWord()
# print(list(cw.word_lst()))

print(cw.get_words())

# with OpenFile('/data/test.txt') as of:
#     print(of, type(of))
