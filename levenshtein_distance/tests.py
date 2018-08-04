from django.test import TestCase

from .service import calculate


class ServiceTestCase(TestCase):
    def test_man_and_woman(self):
        self.assertEqual(calculate('man', 'woman'), 2, 'distance between man and woman is 2')
        self.assertEqual(calculate('woman', 'man'), 2, 'distance between woman and man is 2')
        self.assertEqual(calculate('woman', 'woman'), 0, 'distance between woman and woman is 0')
        self.assertEqual(calculate('man', 'man'), 0, 'distance between man and man is 0')

    def test_many_man(self):
        self.assertEqual(calculate('many', 'man'), 1,
                         'distance between many and man is 1')

    def test_many_woman(self):
        self.assertEqual(calculate('many', 'woman'), 3,
                         'distance between many and woman is 3')

    def test_empty_woman(self):
        self.assertEqual(calculate('', 'woman'), 5,
                         'distance between empty string and woman is 5')
        self.assertEqual(calculate('woman', ''), 5,
                         'distance between woman and empty string is 5')

    def test_wikipedia_1(self):
        self.assertEqual(calculate('kitten', 'sitting'), 3,
                         'distance between kitten and sitting is 3')

    def test_wikipedia_2(self):
        self.assertEqual(calculate('Saturday', 'Sunday'), 3,
                         'distance between Saturday and Sunday is 3')

    def test_gibberish(self):
        self.assertEqual(calculate('ewfrewqrqewr', 'qewreqrewqrqer'), 5,
                         'distance between ewfrewqrqewr and qewreqrewqrqer is 5')
