#!/usr/bin/python3
"""
Unit Test for State Class
"""
import unittest
from datetime import datetime
import models
import json

State = models.state.State
BaseModel = models.base_model.BaseModel


class TestStateDocs(unittest.TestCase):
    """Class for testing State docs"""

    @classmethod
    def setUpClass(cls):
        print('\n\n.................................')
        print('..... Testing Documentation .....')
        print('........   State Class   ........')
        print('.................................\n\n')

    def test_doc_file(self):
        """... documentation for the file"""
        expected = '\nState Class from Models Module\n'
        actual = models.state.__doc__
        self.assertEqual(expected, actual)

    def test_doc_class(self):
        """... documentation for the class"""
        expected = 'State class handles all application states'
        actual = State.__doc__
        self.assertEqual(expected, actual)

    def test_doc_init(self):
        """... documentation for init function"""
        expected = 'instantiates a new state'
        actual = State.__init__.__doc__
        self.assertEqual(expected, actual)


class TestStateInstances(unittest.TestCase):
    """testing for class instances"""

    @classmethod
    def setUpClass(cls):
        print('\n\n.................................')
        print('....... Testing Functions .......')
        print('.........  State Class  .........')
        print('.................................\n\n')

    def setUp(self):
        """initializes new state for testing"""
        self.state = State()

    def test_instantiation(self):
        """... checks if State is properly instantiated"""
        self.assertIsInstance(self.state, State)

    def test_to_string(self):
        """... checks if BaseModel is properly casted to string"""
        my_str = str(self.state)
        my_list = ['State', 'id', 'created_at']
        actual = sum(1 for sub_str in my_list if sub_str in my_str)
        self.assertTrue(actual == 3)

    def test_instantiation_no_updated(self):
        """... should not have updated attribute"""
        my_str = str(self.state)
        actual = 0
        if 'updated_at' in my_str:
            actual += 1
        self.assertTrue(actual == 0)

    def test_updated_at(self):
        """... save function should add updated_at attribute"""
        self.state.save()
        actual = type(self.state.updated_at)
        expected = type(datetime.now())
        self.assertEqual(expected, actual)

    def test_to_json(self):
        """... to_json should return serializable dict object"""
        self.state_json = self.state.to_json()
        actual = 1
        try:
            serialized = json.dumps(self.state_json)
        except:
            actual = 0
        self.assertTrue(actual == 1)

    def test_json_class(self):
        """... to_json should include class key with value State"""
        self.state_json = self.state.to_json()
        actual = self.state_json['__class__'] if self.state_json['__class__'] else None
        expected = 'State'
        self.assertEqual(expected, actual)

    def test_name_attribute(self):
        """... add name attribute"""
        self.state.name = "betty"
        if hasattr(self.state, 'name'):
            actual = self.state.name
        else:
            acual = ''
        expected = "betty"
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main
