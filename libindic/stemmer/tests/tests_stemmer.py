#!/usr/bin/env python
# -*- coding: utf-8 -*-

from testtools import TestCase
from libindic import stemmer
import collections


class MalayalamStemmerTest(TestCase):

    def setUp(self):
        super(MalayalamStemmerTest, self).setUp()
        self.stemmer = stemmer.Malayalam()
        self.verbosity = False

    def test_accusative(self):
        '''
        Accusative - പ്രതിഗ്രാഹിക
        '''
        words = collections.OrderedDict({u'അവനെ': u'അവൻ',
                                         u'അവളെ': u'അവൾ',
                                         u'രമയെ': u'രമ',
                                         u'കഴിവിനെ': u'കഴിവ്',
                                         u'ആപത്തിനെ': u'ആപത്ത്',
                                         u'വാകയെ': u'വാക',
                                         u'അനിലിനെ': u'അനിൽ',
                                         u'അവരെ': u'അവർ',
                                         u'ചെമ്മണ്ണിനെ': u'ചെമ്മണ്ണ്',
                                         u'വാസുകിയെ': u'വാസുകി',
                                         u'വാസ്കോയെ': u'വാസ്കോ',
                                         u'വാത്മീകത്തിനെ': u'വാത്മീകം',
                                         u'ചക്കിനെ': u'ചക്ക്',
                                         u'അച്ചിനെ': u'അച്ച്',
                                         u'പട്ടിനെ': u'പട്ട്',
                                         u'കത്തിനെ': u'കത്ത്',
                                         u'തേപ്പിനെ': u'തേപ്പ്',
                                         u'പയ്യിനെ': u'പയ്യ്',
                                         u'കല്ലിനെ': u'കല്ല്',
                                         u'രാമുവിനെ': u'രാമു',
                                         u'കാടിനെ': u'കാട്',
                                         u'മകൾ': u'മകൾ',
                                         u'രാമൻ.': u'രാമൻ'
                                         })
        for word, expected in words.items():
            word = self.stemmer.singleencode(word)
            obtained = self.stemmer.stem(word)[word]["stem"]
            if self.verbosity:
                print("\t", expected)
                print("\t", obtained)
            assert obtained == expected

    def test_conjuctive(self):
        '''
        Conjuctive - സംയോജിക
        '''
        words = collections.OrderedDict({u'അവനോട്': u'അവൻ',
                                         u'അവളോട്': u'അവൾ',
                                         u'രമയോട്': u'രമ',
                                         u'കഴിവിനോട്': u'കഴിവ്',
                                         u'ആപത്തിനോട്': u'ആപത്ത്',
                                         u'വാകയോട്': u'വാക',
                                         u'അനിലിനോട്': u'അനിൽ',
                                         u'അവരോട്': u'അവർ',
                                         u'ചെമ്മണ്ണിനോട്': u'ചെമ്മണ്ണ്',
                                         u'വാസുകിയോട്': u'വാസുകി',
                                         u'വാസ്കോയോട്': u'വാസ്കോ',
                                         u'വാത്മീകത്തിനോട്': u'വാത്മീകം',
                                         u'ചക്കിനോട്': u'ചക്ക്',
                                         u'അച്ചിനോട്': u'അച്ച്',
                                         u'പട്ടിനോട്': u'പട്ട്',
                                         u'കത്തിനോട്': u'കത്ത്',
                                         u'തേപ്പിനോട്': u'തേപ്പ്',
                                         u'പയ്യിനോട്': u'പയ്യ്',
                                         u'കല്ലിനോട്': u'കല്ല്',
                                         u'രാമുവിനോട്': u'രാമു',
                                         u'കാടിനോട്': u'കാട്'
                                         })
        for word, expected in words.items():
            word = self.stemmer.singleencode(word)
            obtained = self.stemmer.stem(word)[word]["stem"]
            if self.verbosity:
                print(expected, obtained)
            assert obtained == expected

    def test_dative(self):
        '''
        Dative - ഉദ്ദേശിക
        '''
        words = collections.OrderedDict({u'അവന്': u'അവൻ',
                                         u'അവൾക്ക്': u'അവൾ',
                                         u'രമയ്ക്ക്': u'രമ',
                                         u'കഴിവിന്': u'കഴിവ്',
                                         u'ആപത്തിന്': u'ആപത്ത്',
                                         u'വാകയ്ക്ക്': u'വാക',
                                         u'അനിലിന്': u'അനിൽ',
                                         u'അവർക്ക്': u'അവർ',
                                         u'ചെമ്മണ്ണിന്': u'ചെമ്മണ്ണ്',
                                         u'വാസുകിയ്ക്ക്': u'വാസുകി',
                                         u'വാസ്കോയ്ക്ക്': u'വാസ്കോ',
                                         u'വാത്മീകത്തിന്': u'വാത്മീകം',
                                         u'ചക്കിന്': u'ചക്ക്',
                                         u'അച്ചിന്': u'അച്ച്',
                                         u'പട്ടിന്': u'പട്ട്',
                                         u'കത്തിന്': u'കത്ത്',
                                         u'തേപ്പിന്': u'തേപ്പ്',
                                         u'പയ്യിന്': u'പയ്യ്',
                                         u'കല്ലിന്': u'കല്ല്',
                                         u'രാമുവിന്': u'രാമു',
                                         u'കാടിന്': u'കാട്'
                                         })
        for word, expected in words.items():
            word = self.stemmer.singleencode(word)
            obtained = self.stemmer.stem(word)[word]["stem"]
            if self.verbosity:
                print(expected, obtained)
            assert obtained == expected

    def test_instrumental(self):
        '''
        Instrumental - പ്രയോജിക
        '''
        words = collections.OrderedDict({u'അവനാൽ': u'അവൻ',
                                         u'അവളാൽ': u'അവൾ',
                                         u'രമയാൽ': u'രമ',
                                         u'കഴിവിനാൽ': u'കഴിവ്',
                                         u'ആപത്തിനാൽ': u'ആപത്ത്',
                                         u'വാകയാൽ': u'വാക',
                                         u'അനിലിനാൽ': u'അനിൽ',
                                         u'അവരാൽ': u'അവർ',
                                         u'ചെമ്മണ്ണിനാൽ': u'ചെമ്മണ്ണ്',
                                         u'വാത്മീകത്തിനാൽ': u'വാത്മീകം',
                                         u'ചക്കിനാൽ': u'ചക്ക്',
                                         u'അച്ചിനാൽ': u'അച്ച്',
                                         u'പട്ടിനാൽ': u'പട്ട്',
                                         u'കത്തിനാൽ': u'കത്ത്',
                                         u'തേപ്പാൽ': u'തേപ്പ്',
                                         u'പയ്യാൽ': u'പയ്യ്',
                                         u'കല്ലാൽ': u'കല്ല്',
                                         u'രാമുവാൽ': u'രാമു',
                                         u'രാമുവിനാൽ': u'രാമു',
                                         u'കാടിനാൽ': u'കാട്'
                                         })
        for word, expected in words.items():
            word = self.stemmer.singleencode(word)
            obtained = self.stemmer.stem(word)[word]["stem"]
            if self.verbosity:
                print(expected, obtained)
            assert obtained == expected

    def test_possessive(self):
        '''
        Possessive - സംബന്ധിക
        '''
        words = collections.OrderedDict({u'അവന്റെ': u'അവൻ',
                                         u'അവന്റെ': u'അവൻ',
                                         u'അവളുടെ': u'അവൾ',
                                         u'രമയുടെ': u'രമ',
                                         u'കഴിവിന്റെ': u'കഴിവ്',
                                         u'ആപത്തിന്റെ': u'ആപത്ത്',
                                         u'വാകയുടെ': u'വാക',
                                         u'അനിലിന്റെ': u'അനിൽ',
                                         u'അവരുടെ': u'അവർ',
                                         u'ചെമ്മണ്ണിന്റെ': u'ചെമ്മണ്ണ്',
                                         u'വാത്മീകത്തിന്റെ': u'വാത്മീകം',
                                         u'ചക്കിന്റെ': u'ചക്ക്',
                                         u'അച്ചിന്റെ': u'അച്ച്',
                                         u'പട്ടിന്റെ': u'പട്ട്',
                                         u'കത്തിന്റെ': u'കത്ത്',
                                         u'തേപ്പിന്റെ': u'തേപ്പ്',
                                         u'പയ്യിന്റെ': u'പയ്യ്',
                                         u'കല്ലിന്റെ': u'കല്ല്',
                                         u'രാമുവിന്റെ': u'രാമു',
                                         u'അവന്റേത്': u'അവൻ',
                                         u'കാടിന്റെ': u'കാട്',
                                         u'കാടിന്റേത്': u'കാട്'
                                         })
        for word, expected in words.items():
            word = self.stemmer.singleencode(word)
            obtained = self.stemmer.stem(word)[word]["stem"]
            if self.verbosity:
                print(expected, obtained)
            assert obtained == expected

    def test_locative(self):
        '''
        Locative - ആധാരിക
        '''
        words = collections.OrderedDict({u'അവനിൽ': u'അവൻ',
                                         u'അവളിൽ': u'അവൾ',
                                         u'രമയിൽ': u'രമ',
                                         u'കഴിവിൽ': u'കഴിവ്',
                                         u'ആപത്തിൽ': u'ആപത്ത്',
                                         u'വാകയിൽ': u'വാക',
                                         u'അനിലിൽ': u'അനിൽ',
                                         u'അവരിൽ': u'അവർ',
                                         u'ചെമ്മണ്ണിൽ': u'ചെമ്മണ്ണ്',
                                         u'വാത്മീകത്തിൽ': u'വാത്മീകം',
                                         u'ചക്കിൽ': u'ചക്ക്',
                                         u'അച്ചിൽ': u'അച്ച്',
                                         u'പട്ടിൽ': u'പട്ട്',
                                         u'കത്തിൽ': u'കത്ത്',
                                         u'തേപ്പിൽ': u'തേപ്പ്',
                                         u'പയ്യിൽ': u'പയ്യ്',
                                         u'കല്ലിൽ': u'കല്ല്',
                                         u'രാമുവിൽ': u'രാമു',
                                         u'കാട്ടിൽ': u'കാട്'
                                         })
        for word, expected in words.items():
            word = self.stemmer.singleencode(word)
            obtained = self.stemmer.stem(word)[word]["stem"]
            if self.verbosity:
                print(expected, obtained)
            assert obtained == expected

    def test_and(self):
        '''
       And operator - ും
        '''
        words = collections.OrderedDict({u'അവനും': u'അവൻ',
                                         u'അവളും': u'അവൾ',
                                         u'രമയും': u'രമ',
                                         u'കഴിവും': u'കഴിവ്',
                                         u'മനുഷ്യരും': u'മനുഷ്യർ',
                                         u'അതിലും': u'അത്',
                                         u'ഇന്നും': u'ഇന്ന്',
                                         u'ആപത്തും': u'ആപത്ത്',
                                         u'വാകയും': u'വാക',
                                         u'അനിലും': u'അനിൽ',
                                         u'അവരും': u'അവർ',
                                         u'ചെമ്മണ്ണും': u'ചെമ്മണ്ണ്',
                                         u'വാത്മീകവും': u'വാത്മീകം',
                                         u'ചക്കും': u'ചക്ക്',
                                         u'അച്ചും': u'അച്ച്',
                                         u'പട്ടും': u'പട്ട്',
                                         u'കത്തും': u'കത്ത്',
                                         u'തേപ്പും': u'തേപ്പ്',
                                         u'പയ്യും': u'പയ്യ്',
                                         u'കല്ലും': u'കല്ല്',
                                         u'പാനീയവും': u'പാനീയം',
                                         u'രാമുവും': u'രാമു',
                                         u'കാടും': u'കാട്'
                                         })
        for word, expected in words.items():
            word = self.stemmer.singleencode(word)
            obtained = self.stemmer.stem(word)[word]["stem"]
            if self.verbosity:
                print(expected, obtained)
            assert obtained == expected

    def test_plurals(self):
        '''
        Plurals - Experimental
        '''
        words = collections.OrderedDict({u'അണ്ണാന്മാർ': u'അണ്ണാൻ',
                                         u'അവളുമാർ': u'അവൾ',
                                         u'കാക്കകൾ': u'കാക്ക',
                                         u'പശുക്കൾ': u'പശു',
                                         u'കഴിവുകൾ': u'കഴിവ്',
                                         u'അതിലും': u'അത്',
                                         u'ആപത്തുകൾ': u'ആപത്ത്',
                                         u'വാകകൾ': u'വാക',
                                         u'വാത്മീകങ്ങൾ': u'വാത്മീകം',
                                         u'ചക്കുകൾ': u'ചക്ക്',
                                         u'അച്ചുകൾ': u'അച്ച്',
                                         u'പട്ടുകൾ': u'പട്ട്',
                                         u'കത്തുകൾ': u'കത്ത്',
                                         u'തേപ്പുകൾ': u'തേപ്പ്',
                                         u'പയ്യുകൾ': u'പയ്യ്',
                                         u'കല്ലുകൾ': u'കല്ല്',
                                         u'ഭൂതങ്ങൾ': u'ഭൂതം',
                                         u'കാടുകൾ': u'കാട്',
                                         u'മാനുകൾ': u'മാൻ',
                                         u'മൊല്ലാക്കമാർ': u'മൊല്ലാക്ക',
                                         })
        for word, expected in words.items():
            word = self.stemmer.singleencode(word)
            obtained = self.stemmer.stem(word)[word]["stem"]
            if self.verbosity:
                print(expected, obtained)
            assert obtained == expected

    def test_failures(self):
        '''
        Will fail
        '''
        words = collections.OrderedDict({u'അവിടേക്ക്': u'അവിടെ',
                                         u'വന്നു': u'വരുക',
                                         u'ചെന്നു': u'ചെല്ലുക'
                                         })
        for word, expected in words.items():
            word = self.stemmer.singleencode(word)
            obtained = self.stemmer.stem(word)[word]["stem"]
            if self.verbosity:
                print(expected, obtained)
            assert obtained != expected

    def test_verb(self):
        words = collections.OrderedDict({u'പഠിച്ചു': u'പഠിക്കുക',
                                         u'അമർത്തി': u'അമർത്തുക',
                                         u'കിടന്നു': u'കിടക്കുക',
                                         u'മലർന്നു': u'മലരുക',
                                         u'അനക്കി': u'അനക്കുക',
                                         u'പറഞ്ഞു': u'പറയുക',
                                         u'പഠിക്കുന്നു': u'പഠിക്കുക',
                                         u'അമർത്തുന്നു': u'അമർത്തുക',
                                         u'കിടക്കുന്നു': u'കിടക്കുക',
                                         u'പറയുന്നു': u'പറയുക',
                                         u'തുടരുന്നു': u'തുടരുക',
                                         u'കമിഴ്ന്നു': u'കമിഴുക',
                                         u'പറന്നു': u'പറക്കുക',
                                         u'പഠിക്കുന്ന': u'പഠിക്കുക',
                                         })
        for word, expected in words.items():
            word = self.stemmer.singleencode(word)
            obtained = self.stemmer.stem(word)[word]["stem"]
            if self.verbosity:
                print(expected, obtained)
            assert obtained == expected
