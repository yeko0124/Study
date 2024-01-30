"""
회문 단어를 검출하는 함수
# class사용
"""
import re
# /home/rapa/git_workspace/Study/TEST/0130/daddy.txt


class Check:
    def __init__(self):
        self.words = None
        self.get = {}
        self.w_lst = list()

        self.open_files()

    def open_files(self):
        with open('/home/rapa/git_workspace/Study/TEST/0130/daddy.txt', 'r') as fp:
            context = fp.read()
            context = context.lower()
            voca = re.sub(r'[?!@#$%^&*()_+=.,–\'"]+', '', context, re.DOTALL)
            self.words = filter(lambda x: len(x) > 2, voca.split())  # 단어가 3개 이상인 것부터만 출력
            # print(self.words)

    # @staticmethod
    def check_words(self, word):
        a = 0
        b = -1
        for i in range(len(word)//2):
            if word[a] == word[b]:
                pass
            else:
                return False
            a += 1
            b -= 1
        if word in self.get:
            self.get[word] += 1
        self.get.setdefault(word, 1)
        return self.get
        # print(self.get)

    def get_words(self):
        for i in self.words:
            self.check_words(i)
        print(self.get)


c = Check()
c.get_words()
# c.check_words('wow')

# {'abcba' : 2, 'qwerewq': 1}
