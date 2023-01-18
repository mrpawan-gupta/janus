from django.test import TestCase
from faker import Faker

from models import User


# Create your tests here.

class BaseTest(TestCase):
    """
    This is the test class which inherited by all other test classes
    """
    def __init__(self):
        """
        consutructor to
        """
        super(BaseTest, self).__init__()
        self.user = None
        self.phone = None
        self.email = None
        self.name = ''
        self.password = ''

    def setUp(self) -> None:
        """
        Base Function to create User
        :return:  Create Object
        """
        self.name = Faker.user_name()
        self.phone = Faker.phone()
        self.password = Faker.password()
        self.email = Faker.email()

        self.user = User.objects.create_user(username=self.user, password=self.password, phone=self.phone,
                                             email=self.email)

    def tearDown(self) -> None:
        """
        Base function to delete the creation of user object
        :return: delete object
        """
        self.user.delete()