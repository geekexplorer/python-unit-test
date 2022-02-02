import unittest
from unittest.mock import patch;
from person import Person;

class TestPerson(unittest.TestCase):

    def setUp(self):
        # As the name suggests, setting up for the tests. (e.g make a DB connection for the tests in this fixture to utilize)
        self.person1 = Person("Fred", "Flintstone", "http://bedrock.com")

    def test_fullName(self):
        self.assertEqual("Fred Flintstone", self.person1.full_name())

    def test_get_web_page(self):
        person = Person("Fred", "Flintstone", "http://bedrock.com")
        url_text = "I'm a web page. Sup?" 
        message = "One of these does not look like the other."
        with patch.object(person, 'get_web_page', return_value=url_text) as mock_method:
            self.assertEqual(url_text, mock_method(), message)
            
    def tearDown(self):
        # Here's you'd clean up after yourself in the database, etc.

if __name__ == '__main__':
    unittest.main()