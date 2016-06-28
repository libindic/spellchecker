#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os

import Levenshtein
import marisa_trie
from libindic.stemmer import Malayalam as Stemmer
from soundex import Soundex

_characters = [u'\u0d05',
               u'\u0d06',
               u'\u0d07',
               u'\u0d08',
               u'\u0d09',
               u'\u0d0a',
               u'\u0d0b',
               u'\u0d0c',
               u'\u0d0e',
               u'\u0d0f',
               u'\u0d10',
               u'\u0d11',
               u'\u0d13',
               u'\u0d14',
               u'\u0d15',
               u'\u0d16',
               u'\u0d17',
               u'\u0d18',
               u'\u0d19',
               u'\u0d1a',
               u'\u0d1b',
               u'\u0d1c',
               u'\u0d1d',
               u'\u0d1e',
               u'\u0d1f',
               u'\u0d20',
               u'\u0d21',
               u'\u0d22',
               u'\u0d23',
               u'\u0d24',
               u'\u0d25',
               u'\u0d26',
               u'\u0d27',
               u'\u0d28',
               u'\u0d29',
               u'\u0d2a',
               u'\u0d2b',
               u'\u0d2c',
               u'\u0d2d',
               u'\u0d2e',
               u'\u0d2f',
               u'\u0d30',
               u'\u0d31',
               u'\u0d32',
               u'\u0d33',
               u'\u0d34',
               u'\u0d35',
               u'\u0d36',
               u'\u0d37',
               u'\u0d38',
               u'\u0d39']


class Suggestion:
    '''
    Class to hold each suggestion for an incorrect word.
    '''

    def __init__(self, input_word, value, lev, sound):
        self.input_word = input_word
        self.value = value
        self.lev = lev
        self.sound = sound


class Malayalam:

    def __init__(self):
        '''
        Initialize necessary resources.
        '''
        self.dictionary_file = open(os.path.join(
            os.path.dirname(__file__), 'data/ml_rootwords.txt'))
        self.dictionary = self.dictionary_file.readlines()
        self.dictionary_file.close()
        try:
            self.dictionary = marisa_trie.Trie([x.strip().decode('utf-8')
                                                for x in self.dictionary])
        except:
            self.dictionary = marisa_trie.Trie(
                [x.strip() for x in self.dictionary])
        self.stemmer = Stemmer()
        self.soundex = Soundex()

    def check(self, word):
        '''
        Returns if a word is spelled correctly or not.
        '''
        root_word = self.stemmer.stem(word)[word]['stem']
        if root_word in self.dictionary:
            return True
        else:
            return False

    def suggest(self, input_word, n=10):
        '''
        Returns n suggestions that is similar to word.
        '''
        first_char = input_word[0]
        if first_char == _characters[0]:
            prev_char = first_char
        else:
            prev_char_pos = _characters.index(first_char) - 1
            prev_char = _characters[prev_char_pos]
        if first_char == _characters[-1]:
            next_char = first_char
        else:
            next_char_pos = _characters.index(first_char) + 1
            next_char = _characters[next_char_pos]
        possible_words = self.dictionary.keys(first_char) +\
            self.dictionary.keys(next_char) +\
            self.dictionary.keys(prev_char)
        final = []
        for word in possible_words:
            lev, sound = self.compare(input_word, word)
            suggestion_item = Suggestion(input_word, word, lev, sound)
            final.append(suggestion_item)
        sorted_list = sorted(final, key=lambda x: x.lev)[:n]
        return [x.value for x in sorted_list]

    def compare(self, word1, word2):
        '''
        Returns the similarity measure between two words.
        '''
        levenshtein_distance = Levenshtein.distance(word1, word2)
        soundex_comparison = self.soundex.compare(word1, word2)
        return levenshtein_distance, soundex_comparison

    def check_and_generate(self, word):
        '''
        Receives a word as input, checks if it is a valid word and returns
        the suggestions if it is not.
        '''
        status = self.check(word)
        if status:
            return {'status': True, 'suggestions': []}
        else:
            suggestions = self.suggest(word)
            if suggestions:
                return {'status': False, 'suggestions': suggestions}
            else:
                # If there were no suggestions, it means the word was not
                # similar to any of the existing root words. So, that was not a
                # mistake, but an intended insertion. Hence, it is deemed as a
                # valid word
                return {'status': True, 'suggestions': []}
