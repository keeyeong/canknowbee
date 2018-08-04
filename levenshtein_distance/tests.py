from django.test import TestCase

from .service import calculate


class ServiceTestCase(TestCase):
    def test_man_and_woman(self):
        self.assertEqual(calculate('man', 'woman'), 2, 'distance between man and woman is 2')
        self.assertEqual(calculate('woman', 'man'), 2, 'distance between woman and man is 2')
        self.assertEqual(calculate('woman', 'woman'), 0, 'distance between woman and woman is 0')
        self.assertEqual(calculate('man', 'man'), 0, 'distance between man and man is 0')
