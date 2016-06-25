#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os

import marisa_trie
from libindic.stemmer import Malayalam as Stemmer


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

    def check(self, word):
        '''
        Returns if a word is spelled correctly or not.
        '''
        root_word = self.stemmer.stem(word)[word]['stem']
        if root_word in self.dictionary:
            return True
        else:
            return False

    def suggest(self, word, n=10):
        '''
        Returns n suggestions that is similar to word.
        '''
        pass

    def compare(self, word1, word2):
        '''
        Returns the similarity measure between two words.
        '''
        pass
