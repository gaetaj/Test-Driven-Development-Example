import unittest
from check_pwd import check_pwd

# Tests to make sure that check password function
# works properly and meets requirements


class TestCase(unittest.TestCase):
    def test_valid_pwd(self):
        pwd = "jacobGaeta25@"
        self.assertTrue(check_pwd(pwd))

    def test_short_pwd(self):
        pwd = "mooV2#"
        self.assertFalse(check_pwd(pwd))

    def test_long_pwd(self):
        pwd = "mooooooooooooooooooE1!"
        self.assertFalse(check_pwd(pwd))

    def test_has_lower(self):
        pwd = "MOOLY33#"
        self.assertFalse(check_pwd(pwd))

    def test_has_upper(self):
        pwd = "mooly33#"
        self.assertFalse(check_pwd(pwd))

    def test_has_digit(self):
        pwd = "jacobGaeta@@"
        self.assertFalse(check_pwd(pwd))

if __name__ == '__main__':
    unittest.main(verbosity=2)
