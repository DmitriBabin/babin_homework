#!/usr/bin/env python3
import unittest
def find_all_rabin_karp(text, pattern):
    result = []
    patternsum = sum(ord(s_letters) for s_letters in pattern)
    textwindowsum = sum(ord(text[i]) for i in range(len(pattern)))
    index = 0
    for s_letters in range(len(text) - len(pattern) + 1):
        if patternsum == textwindowsum:
            for i in range(len(pattern)):
                if text.startswith(pattern, i + index):
                    result.append(index)
        if len(pattern) + index >= len(text):
            break
        textwindowsum -= ord(text[index])
        textwindowsum += ord(text[len(pattern) + index])
        index +=1
    return result
T = """Вместе шли они в сраженья через минные поля,
на узлах сопротивленья славу поровну деля.
Не страшили дождь и ночь их, и немало огневых
подавили они точек, не считая запятых.
Воевала дело зная та четверка храбрецов -
Иваненко, Иванбаев, Иванидзе, Иванов."""
P = "Иван"
print(find_all_rabin_karp(T,P))
class RabinKarpTest(unittest.TestCase):
    def setUp(self):
        self.text1 = 'axaxaxax'
        self.pattern1 = 'xax'
        self.text2 = 'bababab'
        self.pattern2 = 'bab'
    def test_return_type(self):
        self.assertIsInstance(
            find_all_rabin_karp(self.text1, "x"), list,
        )
    def test_returns_empty(self):
        self.assertEqual(
            [], find_all_rabin_karp(self.text1, "z")
        )
        self.assertEqual(
            [], find_all_rabin_karp("", self.pattern1)
        )
        self.assertEqual(
            [], find_all_rabin_karp("", "")
            )
    def test_finds(self):
        self.assertEqual(
            [1,3,5] , find_all_rabin_karp(self.text1, self.pattern1),
        )
        self.assertEqual(
            [0, 2, 4], find_all_rabin_karp(self.text2, self.pattern2),
        )
    def test_finds_all_empties(self):
        self.assertEqual(
            list(range(len(self.text1))), find_all_rabin_karp(self.text1, ""),
        )
if __name__ == '__main__':
    unittest.main()
