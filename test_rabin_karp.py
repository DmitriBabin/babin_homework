#!/usr/bin/env python3
import unittest
def rabin_karp(text, pattern):
    index = 0
    result = []
    if len(text) >= 1:
        patternsum = sum(ord(s_letters) for s_letters in pattern)
        textwindowsum = sum(ord(text[i]) for i in range(len(pattern)))
        if len(pattern) >= 1:
            for i in range(len(text) - len(pattern) + 1):
                if patternsum == textwindowsum:
                    if text.startswith(pattern, i):
                        result.append(i)
                if len(pattern) + i  >= len(text):
                    break
                textwindowsum -= ord(text[i])
                textwindowsum += ord(text[len(pattern) + i])
                index +=1
        else:
            for i in range(len(text)):
                if pattern != text[i]:
                    result.append(i)
    return result
T = """Вместе шли они в сраженья через минные поля,
на узлах сопротивленья славу поровну деля.
Не страшили дождь и ночь их, и немало огневых
подавили они точек, не считая запятых.
Воевала дело зная та четверка храбрецов -
Иваненко, Иванбаев, Иванидзе, Иванов."""
P = "Иван"
print(rabin_karp(T,P))
class RabinKarpTest(unittest.TestCase):
    def setUp(self):
        self.text1 = 'ахахахах'
        self.pattern1 = 'хах'
        self.text2 = 'bababab'
        self.pattern2 = 'bab'
    def test_return_type(self):
        self.assertIsInstance(
            rabin_karp(self.text1, "x"), list,
        )
    def test_returns_empty(self):
        self.assertEqual(
            [], rabin_karp(self.text1, "z")
        )
        self.assertEqual(
            [], rabin_karp("", self.pattern1)
        )
        self.assertEqual(
            [], rabin_karp("", "")
            )
    def test_finds(self):
        self.assertEqual(
            [1,3,5] , rabin_karp(self.text1, self.pattern1),
        )
        self.assertEqual(
            [0, 2, 4], rabin_karp(self.text2, self.pattern2),
        )
    def test_finds_all_empties(self):
        self.assertEqual(
            list(range(len(self.text1))), rabin_karp(self.text1, ""),
        )
if __name__ == '__main__':
    unittest.main()
    