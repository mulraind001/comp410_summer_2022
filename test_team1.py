import unittest
from team1_pii import find_us_phone_numbers, find_us_street_address


class Team1TestCases(unittest.TestCase):
    def test_us_phone(self):
        # Test valid phone number
        phone = '336-555-1212'
        self.assertTrue(find_us_phone_numbers(phone))

        phone = '336.555.1212'
        self.assertTrue(find_us_phone_numbers(phone))

        # Test invalid
        phone = 'My number is 336-42-1212'
        self.assertFalse(find_us_phone_numbers(phone))

    def test_us_street_address(self):
        # Test valid street address
        streetAddress = '1234 Sesame Street, Bronx, NY, 12345-6789'
        self.assertTrue(find_us_street_address(streetAddress))

        streetAddress = '6789 Baker Street, Atlanta, GA, 12345'
        self.assertTrue(find_us_street_address(streetAddress))

        # Test invalid
        streetAddress = 'My street address is 1234 Invalid Input Drive, Los Angeles, CA, 271'
        self.assertFalse(find_us_street_address(streetAddress))


if __name__ == '__main__':
    unittest.main()
