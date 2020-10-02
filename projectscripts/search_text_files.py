import os
import re
import sys
import argparse

class text_search:
    def __init__(self, string2, path1, i=None):
        self.path1 = path1
        self.string1 = string2
        self.i = i
        if self.i:
            string2 = string2.lower()
            self.string2 = re.compile(string2)