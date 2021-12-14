import unittest

from collections import namedtuple

from factory import Factory
from main import gettype


def mult(x, y):
    return x * y


class TestPars(unittest.TestCase):
    def setUp(self):
        self.testdict = {'a': 1, 'b': 2}
        self.checkdict = namedtuple('object', ['a', 'b'])(*[1, 2])

        class TestClass:
            def __init__(self):
                self.a = 'ee'
                self.b = 'dd'
        self.testobj = TestClass()
        self.checkobj = namedtuple('object', ['a', 'b'])(*['ee', 'dd'])

        def testfunction():
            return "Just testing"
        self.checkfunction = "Just testing"

        self.json_dict = Factory.factory("Json").loads(Factory.factory("Json").dumps(self.testdict))
        self.pickle_dict = Factory.factory("Pickle").loads(Factory.factory("Pickle").dumps(self.testdict))
        self.yaml_dict = Factory.factory("Yaml").loads(Factory.factory("Yaml").dumps(self.testdict))
        self.toml_dict = Factory.factory("Toml").loads(Factory.factory("Toml").dumps(self.testdict))
        self.json_obj = Factory.factory("Json").loads(Factory.factory("Json").dumps(self.testobj))
        self.pickle_obj = Factory.factory("Pickle").loads(Factory.factory("Pickle").dumps(self.testobj))
        self.yaml_obj = Factory.factory("Yaml").loads(Factory.factory("Yaml").dumps(self.testobj))
        self.toml_obj = Factory.factory("Toml").loads(Factory.factory("Toml").dumps(self.testobj))
        self.json_function = Factory.factory("Json").loads(Factory.factory("Json").dumps(testfunction))
        self.pickle_function = Factory.factory("Pickle").loads(Factory.factory("Pickle").dumps(testfunction))
        self.yaml_function = Factory.factory("Yaml").loads(Factory.factory("Yaml").dumps(testfunction))
        self.toml_function = Factory.factory("Toml").loads(Factory.factory("Toml").dumps(testfunction))

    def test_get(self):
        self.assertEqual(gettype("Json").__class__, Factory.factory("Json").__class__)
        self.assertEqual(gettype("Yaml").__class__, Factory.factory("Yaml").__class__)
        self.assertEqual(gettype("Toml").__class__, Factory.factory("Toml").__class__)
        self.assertEqual(gettype("Pickle").__class__, Factory.factory("Pickle").__class__)

    def test_dictionary(self):
        self.assertEqual(self.json_dict, self.checkdict)
        self.assertEqual(self.pickle_dict, self.checkdict)
        self.assertEqual(self.yaml_dict, self.checkdict)
        self.assertEqual(self.toml_dict, self.checkdict)

    def test_object(self):
        self.assertEqual(self.json_obj, self.checkobj)
        self.assertEqual(self.pickle_obj, self.checkobj)
        self.assertEqual(self.yaml_obj, self.checkobj)
        self.assertEqual(self.toml_obj, self.checkobj)

    def test_function(self):
        self.assertEqual(self.json_function(), "testing")
        self.assertEqual(self.pickle_function(), self.checkfunction)
        self.assertEqual(self.yaml_function(), self.checkfunction)

    def test_load(self):
        Factory.factory("Pickle").dump(mult, "./func.pickle")
        pickle_obj = Factory.factory("Pickle").load("./func.pickle")
        self.assertEqual(pickle_obj(4, 3), 12)

if __name__ == "__main__":
    unittest.main()