#!/bin/python3

import math
import os
import random
import re
import sys


class RLEDecoder:
    def __init__(self, code):
        response = ""
        i = 0
        print(code)
        while i < len(code) - 1:
            j = i + 1
            while j < len(code):
                if code[j].isdigit():
                    j += 1
                else:
                    break
            response = f"{response}{code[i] * int(code[i + 1:j])}"
            i = j
        self.response = response

    def count(self, char):
        return self.response.count(char)

    def __len__(self):
        return len(self.response)

    def __str__(self):
        return self.response
