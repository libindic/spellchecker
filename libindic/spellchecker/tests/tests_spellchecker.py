#!/usr/bin/env python
# -*- coding: utf-8 -*-

from libindic.stemmer.Malayalam import Malayalam as stemmer
from testtools import TestCase

from ..Malayalam import BaseMalayalam as spellchecker


class MalayalamSpellcheckerTest(TestCase):

    def setUp(self):
        super(MalayalamSpellcheckerTest, self).setUp()
        self.spellchecker = spellchecker()
        self.stemmer = stemmer()
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
        words = [
            (u'ബാരതം', u'ഭാരതം'),
            (u'അദ്യാപകന്‍', u'അധ്യാപകൻ'),
            (u'ഹലാകലം', u'ഹലാഹലം'),
            (u'ബാരതത്തിന്റെ', u'ഭാരതത്തിന്റെ'),
            (u'അദ്യാപഗനോട്', u'അധ്യാപകനോട്'),
            (u'ബർത്താവിനോട്', u'ഭർത്താവിനോട്'),
            (u'ബാര്യയുടെ', u'ഭാര്യയുടെ'),
            (u'ശോബയാൽ', u'ശോഭയാൽ'),
            (u'ദേബിയോട്', u'ദേവിയോട്'),
            (u'കേരലം', u'കേരളം'),
            (u'ഗരുഢൻ', u'ഗരുഡൻ'),
            (u'വിഞാനം', u'വിജ്ഞാനം'),
            (u'അചൻ', u'അച്ഛൻ'),
            (u'അചൻ', u'അച്ചൻ'),
            (u'മൊതലാളിയോട്', u'മുതലാളിയോട്')
        ]
        for incorrect_word, correct_word in words:
            incorrect_word = self.stemmer.singleencode(incorrect_word)
            correct_word = self.stemmer.singleencode(correct_word)
            suggestion_list = self.spellchecker.suggest(incorrect_word)
            if self.verbosity:
                print(incorrect_word + "\n")
                for word in suggestion_list:
                    print("\t" + word)
            self.assertIn(correct_word, suggestion_list)
