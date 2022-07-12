import unittest
from team2_pii import find_us_phone_numbers
from team2_pii import find_us_ssn
from team2_pii import find_credit_card_number


class Team2TestCases(unittest.TestCase):
    def test_us_phone(self):
        # Test valid phone number
        phone = '336-555-1212'
        self.assertTrue(find_us_phone_numbers(phone))

        phone = '336.555.1212'
        self.assertTrue(find_us_phone_numbers(phone))

        # Test invalid
        phone = 'My number is 336-42-1212'
        self.assertFalse(find_us_phone_numbers(phone))
    
    def test_us_ssn(self):
        # Test valid SSN
        ssn = '111-11-1111'
        self.assertTrue(find_us_ssn(ssn))

        ssn = '001-01-0001'
        self.assertTrue(find_us_ssn(ssn))

        # Test invalid SSN
        ssn = '000-00-0000'
        self.assertFalse(find_us_ssn(ssn))

        ssn = 'SSN: 123-456-7890'
        self.assertFalse(find_us_ssn(ssn))
    
    def test_credit_card_number(self):
        # Test valid credit card number
        ccn = '4444 4444 4444 4444' # Visa, Mastercard, Discover
        self.assertTrue(find_credit_card_number(ccn))

        ccn = '3333 333333 33333' # American Express
        self.assertTrue(find_credit_card_number(ccn))

        ccn = '5555-5555-5555-5555'
        self.assertTrue(find_credit_card_number(ccn))

        # Test invalid credit card number
        ccn = '1234'
        self.assertFalse(find_credit_card_number(ccn))

        ccn = 'hello'
        self.assertFalse(find_credit_card_number(ccn))



if __name__ == '__main__':
    unittest.main()
