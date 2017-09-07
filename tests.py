import os
import re
import unittest
import xml.etree.ElementTree as ET

class TestSequense(unittest.TestCase):
    pass

def test_generator(a, b):
    def test(self):
        self.assertEqual(a, b)
    return test

def normalize_xml(xml):
    tree = ET.fromstring(xml)
    return re.sub('\\n\s+', '', ET.tostring(tree))

if __name__ == '__main__':
    test_path = os.path.join(os.getcwd(), '_site', 'tests')

    for test_file in os.listdir(test_path):
        path = os.path.join(test_path, test_file)
        with open(path, 'r') as file:
            actual, expected = file.read().split('<!-- /// -->')
            actual = normalize_xml(actual)
            expected = normalize_xml(expected)

            # Add the unit test to our TestSequense
            test_name = 'test_{}'.format(test_file)
            test = test_generator(actual, expected)
            setattr(TestSequense, test_name, test)

    unittest.main()
