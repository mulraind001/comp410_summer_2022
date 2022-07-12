import unittest
from team2_pii import find_us_phone_numbers
from team2_pii import find_us_ssn
from team2_pii import find_us_email
from team2_pii import find_us_twitter_handle

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

    def test_us_email(self):
        # Test emails
        email = 'tochah@freeallapp.com'
        self.assertTrue(find_us_email(email))

        email = '5464642@nakiuha.com'
        self.assertTrue(find_us_email(email))
        # invalid test
        email = 'jgfj4!3 @ gmail.com'
        self.assertFalse(find_us_email(email))

    def test_us_twitter(self):
        # Test Twitter Handles
        twt = "@junine12"
        self.assertTrue(find_us_twitter_handle(twt))
        # invalid test

        twt = "wenter"
        self.assertFalse(find_us_twitter_handle(twt))

        twt = "@17ds17__"
        self.assertTrue(find_us_twitter_handle(twt))

if __name__ == '__main__':
    unittest.main()
