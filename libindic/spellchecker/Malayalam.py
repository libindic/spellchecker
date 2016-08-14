#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright: 2016 Balasankar C <balasankarc@autistici.org>
#            2008-2010 Santhosh Thottingal <santhosh.thottingal@gmail.com>
#            http://www.smc.org.in
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.

import os
from collections import namedtuple
from operator import attrgetter

import marisa_trie
from indicsyllabifier import Syllabalizer
from libindic.ngram import Ngram
from libindic.stemmer import Malayalam as Stemmer
from libindic.stemmer import inflector
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

Suggestion = namedtuple('Suggestion', 'word sound lev jac weight tag_list')


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
        self.inflector = inflector.Inflector(lang='ml')
        self.soundex = Soundex()
        self.syllabalizer = Syllabalizer()
        self.ngrammer = Ngram()

    def check(self, word):
        '''
        Returns if a word is spelled correctly or not.
        '''
        root_word = self.stemmer.stem(word)[word]['stem']
        if root_word in self.dictionary:
            return True
        else:
            return False

    def get_best_intermediate(self, word, input_word,
                              intermediate_words, original_tag_list):
        '''
        Return the best intermediate form from those generated during stemming.
        '''
        lev = []
        sound = []
        jac = []
        weight = []
        word_tags_map = {}
        selected_word = input_word
        highest_weight = 0
        for intr_counter in range(len(intermediate_words)):
            intermediate_word = intermediate_words[intr_counter]
            lev_tmp, sound_tmp, jac_tmp, weight_tmp = self.compare(
                intermediate_word, word)
            lev.append(lev_tmp)
            sound.append(sound_tmp)
            jac.append(jac_tmp)
            weight.append(weight_tmp)
            word_tags_map[intermediate_word] = original_tag_list[:intr_counter]
        if len(weight) > 0:
            highest_weight = max(weight)
            position = weight.index(highest_weight)
            selected_word = intermediate_words[position]
            lev = lev[position]
        return word_tags_map, highest_weight, selected_word

    def get_unique(self, list_of_items):
        '''
        Remove duplicates from the input list.
        '''
        result = []
        for item in list_of_items:
            if item not in result:
                result.append(item)
        return result

    def suggest(self, input_word, n=5):
        '''
        Returns n suggestions that is similar to word.
        '''
        stemmer_result = self.stemmer.stem(input_word)[input_word]
        input_word = stemmer_result['stem']
        tag_list = stemmer_result['inflection']
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
        intermediate_words = []
        original_tag_list = tag_list
        intermediate_words.append(input_word)
        for tag_counter in range(len(tag_list)):
            new_word = self.inflector.inflect(
                input_word, tag_list[-tag_counter - 1:])
            intermediate_words.insert(0, new_word)
        for word in possible_words:
            lev, sound, jac, weight1 = self.compare(input_word, word)
            word_tags_map, highest_weight, selected_word =\
                self.get_best_intermediate(
                    word, input_word, intermediate_words, original_tag_list)
            tag_list = original_tag_list
            if highest_weight >= weight1 and selected_word != input_word:
                tag_list = word_tags_map[selected_word]
            weight = max(weight1, highest_weight)
            suggestion_item = Suggestion(
                word, sound, lev, jac, weight, tag_list)
            if weight > 50:
                final.append(suggestion_item)
        sorted_list = sorted(final, key=attrgetter('weight'), reverse=True)[:n]
        final_list = []
        for item in sorted_list:
            word = item.word
            tag_list = item.tag_list
            try:
                inflected_form = self.inflector.inflect(word, tag_list)
                final_list.append(inflected_form)
            except:
                final_list.append(word)
                continue
        return self.get_unique(final_list)

    def levenshtein_distance(self, tokens1, tokens2):
        '''
        Takes two lists containing tokens of one word each and returns the
        levenshtein distance between them.
        '''
        if len(tokens1) < len(tokens2):
            return self.levenshtein_distance(tokens2, tokens1)

        if len(tokens2) == 0:
            return len(tokens1)

        previous_row = range(len(tokens2) + 1)
        for i, c1 in enumerate(tokens1):
            current_row = [i + 1]
            for j, c2 in enumerate(tokens2):
                # j+1 instead of j since previous_row and current_row are one
                # character longer
                insertions = previous_row[j + 1] + 1
                deletions = current_row[j] + 1       # than tokens2
                substitutions = previous_row[j] + (c1 != c2)
                current_row.append(min(insertions, deletions, substitutions))
            previous_row = current_row

        return previous_row[-1]

    def compare(self, word1, word2):
        '''
        Returns the similarity measure between two words.
        '''
        soundex_comparison = self.soundex.compare(word1, word2)
        tokens1 = self.syllabalizer.syllabify_ml(word1)
        tokens2 = self.syllabalizer.syllabify_ml(word2)
        levenshtein_distance = self.levenshtein_distance(tokens1, tokens2)
        ngram1 = self.ngrammer.letterNgram(word1, 1)
        ngram2 = self.ngrammer.letterNgram(word2, 1)
        total = ngram1 + ngram2
        union = []
        for counter in range(len(total)):
            item = total[counter]
            if item not in union:
                union.append(item)
        final = [x for x in ngram1 if x in ngram2] +\
            [x for x in ngram2 if x in ngram1]
        intersection = []
        for counter in range(len(final)):
            item = final[counter]
            if item not in intersection:
                intersection.append(item)
        jaccards = float(len(intersection)) / float(len(union))
        if soundex_comparison == 1 or soundex_comparison == 0:
            weight = 100
        elif levenshtein_distance <= 2 and jaccards > 0.5:
            weight = 75 + (1.5 * jaccards)
        elif levenshtein_distance < 5 and jaccards > 0.5:
            weight = 65 + (3 * jaccards)
        else:
            weight = 0
        return levenshtein_distance, soundex_comparison, jaccards, weight

    def check_and_generate(self, word):
        '''
        Receives a word as input, checks if it is a valid word and returns
        the suggestions if it is not.
        Returns 0 along with suggestions if an incorrect word.
        Returns 1 along with blank list of suggestions if word in dictionary.
        Returns 2 along with blank list of suggestions if word is unique.
        '''
        status = self.check(word)
        if status:
            return {'status': 1, 'suggestions': []}
        else:
            suggestions = self.suggest(word)
            if suggestions:
                return {'status': 0, 'suggestions': suggestions}
            else:
                # If there were no suggestions, it means the word was not
                # similar to any of the existing root words. So, that was not a
                # mistake, but an intended insertion. Hence, it is deemed as a
                # valid word
                return {'status': 2, 'suggestions': []}
