'''
class Atbash(object):
    def __init__(self, filename):
        self.filename = filename
    def decode(self, filename):
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
            l1 = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
            l1 = [letter for letter in l1]

            sh = dict(zip(l1, l1[::-1]))

            s = text.lower()
            sn = ''
            for i in range(len(s)):
                if s[i] in sh.keys():
                    sn += sh[s[i]]
                else:
                    sn += s[i]
        return sn
atbash = Atbash('shiphr.txt')
print(atbash.decode('shiphr.txt'))
'''
'key 14'
'''
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
'''

'''
l1 = 'абвгдежзийклмнопрстуфхцчшщыьэюя'
l1 = [letter for letter in l1]
class Monoalphabet(object):
    def __init__(self, filename):
        self.filename = filename


    def decode(self, key):
        with open('shiphr.txt', 'r', encoding='utf-8') as file:
            text = file.read()
            s = text.lower()
            sn = ''
            for i in range(len(s)):
                if s[i] in key.keys():
                    sn += key[s[i]]
                else:
                    sn += s[i]
        return sn

ranks_o = dict(zip([3, 21, 9, 19, 13, 2, 25, 20, 4, 23, 11, 10, 12, 5, 1, 14, 8, 7, 16, 5, 31, 24, 28, 22, 26, 29, 17, 18, 30, 27, 16], l1))
ranks_o = dict(sorted(ranks_o.items(), key=lambda item: item[0]))
freq = []
with open('shiphr.txt', 'r', encoding='utf-8') as file:
    text = file.read()
    for el in l1:
        freq.append((text.lower()).count(el))

ranks = dict(zip(freq, l1))
ranks = dict(sorted(ranks.items(), key=lambda item: -item[0]))
T = dict(zip(ranks.values(), ranks_o.values()))
To = {'ц': 'о', 'э': 'а', 'г': 'и', 'щ': 'е', 'о': 'в', 'ю': 'н', 'ж': 'р', 'я': 'л', 'ш': 'с', 'с': 'м', 'ч': 'к', 'а': 'п', 'з': 'п', 'й': 'з', 'м': 'д', 'п': 'ф', 'и': 'я', 'е': 'ш', 'ь': 'н', 'л': 'ч', 'р': 'г', 'н': 'х', 'ы': 'ж', 'ф': 'ш', 'к': 'ю', 'д': 'ц', 'у': 'щ', 'б': 'т'}
mono = Monoalphabet('shiphr.txt')
print(mono.decode(To))
'''
'''
l1 = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
l1 = [letter for letter in l1]

def ceasar(keyletter):
    l2 = l1[l1.index(keyletter)::] + l1[0:l1.index(keyletter)]
    return dict(zip(l1, l2))

class Enigma(object):
    def __init__(self, filename):
        self.filename = filename
    def decode(self, keyword):
        with open(self.filename, 'r', encoding='utf-8') as file:
            text = file.read()
            text = text.lower()
            decoded_text = ''
            c = 0
            key = []
            for letter in keyword:
                T = ceasar(letter)
                key.append(T)
            for letter in text:
                if letter in l1:
                    decoded_text += key[c][letter]
                    c += 1
                    if c == len(keyword):
                        c = 0
                else:
                    decoded_text += letter
        return decoded_text
enigma = Enigma('shiphr.txt')
print(enigma.decode('мфти'))
'''

