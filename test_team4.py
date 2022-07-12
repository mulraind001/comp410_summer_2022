import unittest
from team4_pii import find_us_phone_numbers, find_twitter_usernames


class Team4TestCases(unittest.TestCase):
    def test_us_phone(self):
        # Test valid phone number
        phone = '336-555-1212'
        self.assertTrue(find_us_phone_numbers(phone))

        phone = '336.555.1212'
        self.assertTrue(find_us_phone_numbers(phone))

        # Test invalid
        phone = 'My number is 336-42-1212'
        self.assertFalse(find_us_phone_numbers(phone))

    def test_twitter_usernames(self):
        # Test valid usernames
        twitterHandle = '@ncatsuaggies'
        self.assertTrue(find_twitter_usernames(twitterHandle))

        twitterHandle = '@FatKidDeals01'
        self.assertTrue(find_twitter_usernames(twitterHandle))

        twitterHandle = '@CNN_sports'
        self.assertTrue(find_twitter_usernames(twitterHandle))

        # Test invalid usernames
        twitterHandle = 'CNN'
        self.assertFalse(find_twitter_usernames(twitterHandle))

        twitterHandle = 'google@'
        self.assertFalse(find_twitter_usernames(twitterHandle))


if __name__ == '__main__':
    unittest.main()
