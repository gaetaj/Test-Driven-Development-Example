import unittest
from check_pwd import check_pwd

# Tests to make sure that check password function
# works properly and meets requirements


class TestCase(unittest.TestCase):
    def test_valid_pwd(self):
        pwd = "jacobGaeta25@"
        self.assertTrue(check_pwd(pwd))

if __name__ == '__main__':
    unittest.main(verbosity=2)
