import unittest

from bot import input_birthday

class TestBot(unittest.TestCase):
    
    def setUp(self):
        self.secret_birthday = "13 June 2000"

    def test_ddmmyy_correct_birthday(self):
        # test works with dd/mm/yy format
        result = input_birthday("13/6/2000")
        self.assertEqual(result[3:], self.secret_birthday)

    def test_mmddyy_correct_birthday(self):
        # test works with mm/dd/yy format
        result = input_birthday("6/13/2000")
        self.assertEqual(result[3:],self.secret_birthday)

    def test_ambiguous_format(self):
        # test if date is unclear, returns ambiguous tag
        result = input_birthday("5/6/2000")
        self.assertEqual(result[0], "A")

    def test_extra_days_in_month(self):
        # test response if too many days in month
        result = input_birthday("treinta de february 2000")
        self.assertEqual(result[0], "N")

    def test_future_date(self):
        # test response when date in future
        result = input_birthday("5th October 2066")
        self.assertEqual(result[0], "N")

    def test_spanish_error(self):
        # test if switches to spanish to explain error
        result = input_birthday("Enero de 2000")
        self.assertTrue("dia" in result or "día" in result)     

    def missing_format(self):
        # test if don't put any date
        result = input_birthday("I like the sun")
        self.assertEqual("result[0]","N")


if __name__ == '__main__':
    unittest.main()