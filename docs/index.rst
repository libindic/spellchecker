.. spellchecker documentation master file, created by
   sphinx-quickstart on Thu Sep 12 18:10:42 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to LibIndic Spell Checker's documentation!
==================================================


LibIndic's spell checker module may be used to check if a word has the correct
spelling or not. It is also able to generate suggestions that have higher
probability to be the word actually intended. It is able to handle inflections
in input words and generate suggestions in the same inflectious form. It can
also differentiate from spelling mistakes and intended words that are not in
dictionary. It follows a rule based model and uses the LibIndic's stemmer
module. Right now, spell checker module supports Malayalam language only.

Usage
-----


 >>> from libindic.spellchecker import Malayalam as mlspellchecker
 >>> spellchecker = mlspellchecker()
 >>> spellchecker.check('മൊതലാളിയോട്')
 False
 >>> suggestions = spellchecker.suggest('മൊതലാളിയോട്')
 >>> for item in suggestions:
 ...     print item
 ...
 മുതലാളിയോട്
 മാതലിയോട്
 മാലതിയോട്
 മാതുലിയോട്
 മലയാളിയോട്
 >>> spellchecker.check('മുതലാളിയോട്')
 True

``spellchecker`` API
---------------------

.. automodule:: spellchecker.Malayalam
   :members:




Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
