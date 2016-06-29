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
            status = self.spellchecker.check_and_generate(word)['status']
            if self.verbosity:
                print("%s  :  %s" % (word, status))
            assert status

        false_list = [u'ആബത്തിന്റെ',
                      u'അദ്യാപഗൻ',
                      u'ദേബി'
                      ]
        for word in false_list:
            status = self.spellchecker.check_and_generate(word)['status']
            if self.verbosity:
                print("%s  :  %s" % (word, status))
            assert not status

        custom_words = [u'സ്യൂഡോനാഷണലിസ്റ്റ്']
        # Words that are not found in dictionary, but unique and thus deemed
        # valid
        for word in custom_words:
            status = self.spellchecker.check_and_generate(word)['status']
            if self.verbosity:
                print("%s  :  %s" % (word, status))
            assert status

    def test_suggestion_generation(self):
        '''
        Test if correct word is in the list of suggestions generated.
        '''
        words = collections.OrderedDict({u'ബാരതം': u'ഭാരതം',
                                         u'അദ്യാപകന്‍': u'അധ്യാപകൻ',
                                         u'ഹലാകലം': u'ഹലാഹലം',
                                         u'ബാരതത്തിന്റെ': u'ഭാരതത്തിന്റെ',
                                         u'അദ്യാപഗനോട്': u'അധ്യാപകനോട്'
                                         })
        for incorrect_word, correct_word in words.items():
            suggestion_list = self.spellchecker.suggest(incorrect_word)
            if self.verbosity:
                print(incorrect_word + "\n")
                for word in suggestion_list:
                    print("\t" + word)
            self.assertIn(correct_word, suggestion_list)
