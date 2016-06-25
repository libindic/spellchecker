#!/usr/bin/env python
# -*- coding: utf-8 -*-

import collections

from libindic import spellchecker
from testtools import TestCase


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

    def test_suggestion_generation(self):
        '''
        Test if correct word is in the list of suggestions generated.
        '''
        words = collections.OrderedDict({u'ബാരതം': u'ഭാരതം',
                                         })
        for incorrect_word, correct_word in words.items():
            suggestion_list = self.spellchecker.suggest(incorrect_word)
            if self.verbosity:
                print(incorrect_word + "\n")
                for word in suggestion_list:
                    print("\t" + word)
            self.assertIn(correct_word, suggestion_list)
