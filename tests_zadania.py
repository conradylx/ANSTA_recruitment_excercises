import unittest
from excercises import postal_codes_generate, check_missing_numbers, iterate_by_float_step


class Tests_of_Excercises(unittest.TestCase):
    def setUp(self):
        self.data = [1, 3, 5, 6, 7, 8, 10]
        self.data_len = 11
        self.postal_from = '18-400'
        self.postal_to = '18-409'
        self.from_step = 3
        self.to_step = 7
        self.by_step = .5

    def test_postal_codes_postals_range(self):
        context = len(postal_codes_generate(self.postal_from, self.postal_to))
        self.assertEqual(context, 8)

    def test_check_missing_numbers_from_given_data(self):
        context = check_missing_numbers(self.data, self.data_len)
        self.assertEqual(context, [2, 4, 9, 11])

    def test_iterate_by_float_step_length(self):
        context = len(iterate_by_float_step(self.from_step, self.to_step, self.by_step))
        self.assertEqual(context, 8)


if __name__ == '__main__':
    unittest.main()
