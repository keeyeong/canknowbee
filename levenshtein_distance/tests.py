from django.test import TestCase, Client

from .service import calculate_distance_with_matrix


class ServiceTestCase(TestCase):
    def test_man_and_woman(self):
        self.assertEqual(self.get_distance('man', 'woman'), 2, 'distance between man and woman is 2')
        self.assertEqual(self.get_distance('woman', 'man'), 2, 'distance between woman and man is 2')
        self.assertEqual(self.get_distance('woman', 'woman'), 0, 'distance between woman and woman is 0')
        self.assertEqual(self.get_distance('man', 'man'), 0, 'distance between man and man is 0')

    def test_many_man(self):
        self.assertEqual(self.get_distance('many', 'man'), 1,
                         'distance between many and man is 1')

    def test_many_woman(self):
        self.assertEqual(self.get_distance('many', 'woman'), 3,
                         'distance between many and woman is 3')

    def test_empty_woman(self):
        self.assertEqual(self.get_distance('', 'woman'), 5,
                         'distance between empty string and woman is 5')
        self.assertEqual(self.get_distance('woman', ''), 5,
                         'distance between woman and empty string is 5')

    def test_wikipedia_example_1(self):
        self.assertEqual(self.get_distance('kitten', 'sitting'), 3,
                         'distance between kitten and sitting is 3')

    def test_wikipedia_example_2(self):
        self.assertEqual(self.get_distance('Saturday', 'Sunday'), 3,
                         'distance between Saturday and Sunday is 3')

    def test_gibberish(self):
        self.assertEqual(self.get_distance('ewfrewqrqewr', 'qewreqrewqrqer'), 5,
                         'distance between ewfrewqrqewr and qewreqrewqrqer is 5')

    def test_matrix_dimension_and_result(self):
        results = calculate_distance_with_matrix('Saturday', 'Sunday')
        matrix = results[1]
        self.assertEqual(results[0], 3)
        self.assertEqual(len(matrix), 9)  # 9 rows for 'Saturday'
        self.assertEqual(len(matrix[0]), 7)  # 7 columns for 'Sunday'

    def get_distance(self, source, target):
        return calculate_distance_with_matrix(source, target)[0]


class WebTest(TestCase):
    web_client = Client()

    def test_get(self):
        response = self.web_client.get('/')
        self.assertEqual(response.status_code, 200)  # no error
        self.assertEqual(response.context['result'], None)  # no result

    def test_post(self):
        response = self.web_client.post('/', {'source': 'woman', 'target': 'man'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['result'], 2)  # result is correct
        self.assertEqual(len(response.context['matrix']), 6)  # matrix is right dimension
        self.assertEqual(len(response.context['matrix'][0]), 4)
        self.assertEqual(response.context['source'], 'woman')  # params are returned
        self.assertEqual(response.context['target'], 'man')
