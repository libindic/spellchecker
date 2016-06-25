#!/usr/bin/env python
# -*- coding: utf-8 -*-

from testtools import TestCase
from libindic import spellchecker


class MalayalamSpellcheckerTest(TestCase):

    def setUp(self):
        super(MalayalamSpellcheckerTest, self).setUp()
        self.spellchecker = spellchecker.Malayalam()
        self.verbosity = False

    def test_checking(self):
        '''
        Test if spelling mistake detection works fine.
        '''
        true_list = [u'രമയുടെ',
                     u'ആപത്തിലേക്ക്',
                     u'ദേവി'
                     ]
        for word in true_list:
            status = self.spellchecker.check(word)
            if self.verbosity:
                print("%s  :  %s" % (word, status))
            assert status

        false_list = [u'ആബത്തിന്റെ',
                      u'അദ്യാപഗൻ',
                      u'ദേബി'
                      ]
        for word in false_list:
            status = self.spellchecker.check(word)
            if self.verbosity:
                print("%s  :  %s" % (word, status))
            assert not status
