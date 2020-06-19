# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Initiation time
"""
__all__ = ["Corpus", "corn"]
__author__ = "Jason Nguyen"
__copyright__ = "Copyright 2020, Jason Nguyen"
__credits__ = "TBA"
__license__ = "MIT"
__maintainer__ = "Jason Nguyen"
__email__ = "jnguye21@uoguelph.ca"
__status__ = "Planning"
with open("VERSION", "r") as fd:
    __version__ = fd.read().strip()

from .corpus import Corpus, corn
