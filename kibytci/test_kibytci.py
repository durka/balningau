from django.test import TestCase

class HelloWorldTestCase(TestCase):
    def setUp(self):
        pass

    def test_test(self):
        print('Hello, world!')
        self.assertEqual(1, 1)

