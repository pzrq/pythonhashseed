from django.test import TestCase


class PythonHashSeedTest(TestCase):
    def test_sometimes_passes(self):
        expect = ['a', 'bb']
        actual = list({'a': 5, 'bb': 8}.keys())
        self.assertEqual(expect, actual)
