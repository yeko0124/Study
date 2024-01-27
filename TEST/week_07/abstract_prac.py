import json
import codecs
import abc


class File(metaclass=abc.ABCMeta):
    def __init__(self, size, author, datetime, filepath):
        self.__size = size
        self.__author = author
        self.__datetime = datetime
        self.__file_path = filepath

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, val):
        assert isinstance(val, float)
        self.__size = val

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, val):
        assert isinstance(val, str)
        self.__author = val

    @property
    def datetime(self):
        return self.__datetime

    @datetime.setter
    def datetime(self, val):
        assert isinstance(val, str)
        self.__datetime = val

    @property
    def filepath(self):
        return self.__file_path

    @filepath.setter
    def filepath(self, val):
        assert isinstance(val, str)
        self.__file_path = val

    @abc.abstractmethod
    def write_file(self):
        pass

    @abc.abstractmethod
    def read_file(self):
        pass

    @abc.abstractmethod
    def make_filepath(self):
        pass


class Text(File):
    def __init__(self, size, author, datetime, filepath):
        super().__init__(size, author, datetime, filepath)

    def make_filepath(self):
        return f'{self.filepath}.txt'

    def write_file(self):
        with open(self.make_filepath(), 'wt') as fp:
            fp.write('asdf')

    def read_file(self):
        with open(self.make_filepath(), 'rt') as fp:
            return fp.read()


class Binary(File):
    def __init__(self, size, author, datetime, filepath):
        super().__init__(size, author, datetime, filepath)

    def make_filepath(self):
        return f'{self.filepath}.bin'

    def write_file(self):
        with open(self.make_filepath(), 'wb') as fp:
            fp.write(
                codecs.encode(
                    'asdfasdf'.encode('utf-8'), 'base64'))

    def read_file(self):
        with open(self.make_filepath(), 'rb') as fp:
            return codecs.decode(
                fp.read(), 'base64').decode('utf-8')


class Json(File):
    def __init__(self, size, author, datetime, filepath):
        super().__init__(size, author, datetime, filepath)

    def make_filepath(self):
        return f'{self.filepath}.json'

    def write_file(self):
        with open(self.make_filepath(), 'wt') as fp:
            json.dump({'aaa': 1234}, fp)

    def read_file(self):
        with open(self.make_filepath(), 'rt') as fp:
            return json.load(fp)


if __name__ == '__main__':
    text_file = Text(
        '54b',
        'scii',
        '2024-01-27 16:12',
        '/home/rapa/abc'
    )

    text_file.write_file()

    bin_file = Binary(
        '54b',
        'scii',
        '2024-01-27 16:12',
        '/home/rapa/abc'
    )

    bin_file.write_file()
    # res = bin_file.read_file()
    # print(res)

    json_file = Json(
        '54b',
        'scii',
        '2024-01-27 16:12',
        '/home/rapa/abc'
    )

    json_file.write_file()