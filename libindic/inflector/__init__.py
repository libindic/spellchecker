#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import os


class Malayalam(object):

    def __init__(self):
        self.rules_file = os.path.join(
            os.path.dirname(__file__), 'data/ml_inflection.json')
        self.rules_object = open(self.rules_file, 'r')
        self.rulesDict = json.loads(self.rules_object.read())

    def inflect(self, word, tag_list):
        try:
            word = word.decode('utf-8')
        except:
            pass
        for tag in tag_list[::-1]:
            rules = self.rulesDict[tag]
            flag = False
            for lhs, rhs in rules.items():
                length = len(lhs)
                suffix = word[-length:]
                if suffix == lhs:
                    flag = True
                    word = word[:-length] + rhs
                    break
            if not flag:
                word = word + rules['default']
        try:
            word = word.decode('utf-8')
        except:
            pass
        return word
