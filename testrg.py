import unittest
import randomgame


class FunctionTest(unittest.TestCase):
    def test_evaluate_guess_letters(self):
        test_param = 'abc'
        result = randomgame.evaluate_guess(test_param, 5, 1, 10)
        self.assertEqual(result, 'Please enter a number in the integer format!')

    def test_evaluate_guess_out_of_bounds_negative(self):
        test_param = '-5'
        result = randomgame.evaluate_guess(test_param, 5, 1, 10)
        self.assertEqual(result, f'Please enter a number between 1 and 10!')

    def test_evaluate_guess_out_of_bounds_positive(self):
        test_param = '25'
        result = randomgame.evaluate_guess(test_param, 5, 1, 10)
        self.assertEqual(result, f'Please enter a number between 1 and 10!')

    def test_evaluate_guess_empty_string(self):
        test_param = ''
        result = randomgame.evaluate_guess(test_param, 5, 1, 10)
        self.assertEqual(result, 'Please enter a number in the integer format!')

    def test_evaluate_guess_float(self):
        test_param = '2.5'
        result = randomgame.evaluate_guess(test_param, 5, 1, 10)
        self.assertEqual(result, 'Please enter a number in the integer format!')

    def test_evaluate_guess_correct_answer(self):
        test_param = '5'
        result = randomgame.evaluate_guess(test_param, 5, 1, 10)
        self.assertEqual(result, 'Congratulations, you got it!')

    def test_evaluate_guess_incorrect_answer(self):
        test_param = '6'
        result = randomgame.evaluate_guess(test_param, 5, 1, 10)
        self.assertEqual(result, None)


if __name__ == '__main__':
    unittest.main()
