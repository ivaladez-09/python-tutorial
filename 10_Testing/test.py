import unittest
import script


class Testscript(unittest.TestCase):
    def setUp(self):
        print("About to to test a function")
        # return super().setUp()

    def test_do_stuff(self):
        """Hii!!!"""
        test_param = 10
        # Call function to test
        result = script.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        test_param = "dget"
        # Call function to test
        result = script.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)

    def test_do_stuff3(self):
        test_param = None
        # Call function to test
        result = script.do_stuff(test_param)
        self.assertEqual(result, "Please enter number")

    def test_do_stuff4(self):
        test_param = ""
        # Call function to test
        result = script.do_stuff(test_param)
        self.assertEqual(result, "Please enter number")

    def tearDown(self):
        print("Clean Up")
        # return super().tearDown()


if __name__ == "__main__":
    # Run all the tests
    unittest.main()

# You can run in terminal "python3 -m unittest -v"
