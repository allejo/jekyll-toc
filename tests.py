import os
import re
import unittest
import xml.etree.ElementTree as ET

class TestSequence(unittest.TestCase):
    pass

def test_generator(a, b):
    def test(self):
        self.assertEqual(a, b)
    return test

def normalize_xml(xml, test_file):
    try:
        tree = ET.fromstring(xml)
    except:
        print(f">> Invalid XML in {test_file}")
        raise

    return re.sub(r'(\\n|\n)\s*', '', str(ET.tostring(tree)), 0, re.MULTILINE)

if __name__ == '__main__':
    test_path = os.path.join(os.getcwd(), '_site', 'tests')

    for test_file in os.listdir(test_path):
        path = os.path.join(test_path, test_file)
        with open(path, 'r') as file:
            actual, expected = file.read().split('<!-- /// -->')
            actual = normalize_xml(actual, test_file)
            expected = normalize_xml(expected, test_file)

            # Add the unit test to our TestSequence
            test_name = 'test_{}'.format(test_file)
            test = test_generator(actual, expected)
            setattr(TestSequence, test_name, test)

    unittest.main()
