import unittest


class Ceasar(object):

    def __init__(self, filename):
        self.filename = filename

    def decode(self, key):
        with open(self.filename, 'r', encoding='utf-8') as file:
            text = file.read()
            l1 = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
            l1 = [letter for letter in l1]

        l2 = l1[key::] + l1[0:key]
        sh = dict(zip(l1, l2))
        s = text.lower()
        sn = ''
        for i in range(len(s)):
            if s[i] in sh.keys():
                sn += sh[s[i]]
            else:
                sn += s[i]
        return sn


ceasar = Ceasar('shiphr.txt')
print(ceasar.decode(14))


class TestCommonText(unittest.TestCase):
    def test_common_text(self):
        self.assertEqual(Ceasar('c1.txt').decode(-5),
                         'тест обычного текста',
                         "should be тест обычного текста")


class TestSingleLetter(unittest.TestCase):
    def test_single_letter(self):
        self.assertEqual(Ceasar('c2.txt').decode(-5),
                         'а', "should be а")


class TestVarSymbols(unittest.TestCase):
    def test_var_symbols(self):
        self.assertEqual(Ceasar('c3.txt').decode(-10),
                         'тест с цифрой 9 и точкой .',
                         "should be тест с цифрой 9 и точкой .")


class TestEmptyFile(unittest.TestCase):
    def test_empty_file(self):
        self.assertEqual(Ceasar('c4.txt').decode(-11),
                         '', "should be ")