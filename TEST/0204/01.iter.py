
class MyItertor:
    def __init__(self, data):
        self.data = data
        # index를 위한 변수
        self.position = 0

    def __iter__(self):
        # next 내장 함수를 호출하기 위하여 self반환
        return self

    def __next__(self):
        # 인덱스는 0부터 시작하므로 이상이 0 되면 예외 발생
        if self.position >= len(self.data):
            raise StopIteration
        result = self.data[self.position]
        self.position += 1
        return result


if __name__ == '__main__':
    i = MyItertor([1, 2, 3])
    for item in i:
        print(item, end=' ')

