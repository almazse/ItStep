import unittest

from methods import Admin, SuperAdmin


class SuperAdminTests(unittest.TestCase):
    # valid data
    VALID_EMAIL = 'Correct@emial.com'
    VALID_PASSWORD = 'AQwe12!_'

    # invalid data
    INVALID_EMAIL = 'incorrect@emial.com'
    INVALID_PASSWORD = 12345678

    def setUp(self) -> None:
        # create SuperAdmin
        self.admin = SuperAdmin(self.VALID_EMAIL, self.VALID_PASSWORD)
        # return super().setUp()

    def test_create_SuperAdmin(self):
        super_admin_val = SuperAdmin(self.VALID_EMAIL, self.VALID_PASSWORD)
        self.assertIsInstance(super_admin_val, SuperAdmin)
        print('Test 1.1: pass.')

        super_admin = SuperAdmin(self.INVALID_EMAIL, self.INVALID_PASSWORD)
        self.assertIsInstance(self.INVALID_EMAIL, str)
        self.assertNotIsInstance(self.INVALID_PASSWORD, str,
                                 f'Incorrect data type! It must been str but returned {type(self.INVALID_PASSWORD)}')
        self.assertIsInstance(super_admin, SuperAdmin)

        print('Test 1.2: pass.')

    # def test_add_admin(self):
    #     admin_1 = SuperAdmin('Bad', 'BOB').add_admin(admin_1_data)


if __name__ == '__main__':
    unittest.main()