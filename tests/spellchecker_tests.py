# -*- coding: utf-8 -*-
#! /usr/bin/python
import unittest
from spellchecker  import getInstance


class TestSpellChecker(unittest.TestCase):

    def setUp(self):
        self.instance = getInstance()

    def test_info(self):
        self.assertEqual('Indic Spellchecker',
                         self.instance.get_info())

    def test_english(self):
        self.assertTrue(self.instance.check("Judicious"),
                        True)
        self.assertFalse(self.instance.check("Judecious"))

    def test_malayalam(self):
        self.assertTrue(self.instance.check(u"മധുരം"))
        self.assertTrue(self.instance.check(u"മാങ്ങ"))

    def test_hindi(self):
        self.assertTrue(self.instance.check(u"खुला"))

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSpellChecker)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == "__main__":
    main()
