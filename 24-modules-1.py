### Built-in Modules

import math

print(math.sqrt(16))
print(math.pi)
print(math.e)
print(math.cos(1))

import calendar

print(calendar.month(2021, 1))
print(calendar.isleap(2021))
print(calendar.weekday(1997, 8, 28))

import random as rand

print(rand.random())

from random import randint
from math import cos, sin, tan
from calendar import *  # Avoid using this

print(randint(1, 10))
print(cos(1))
print(isleap(2021))

### Custom Modules

import utils

# from .utils import add_five # ImportError: attempted relative import with no known parent package

print(utils.add_five([1, 2, 3, 4, 5]))

### 3rd Party Modules

# pip install art, OR
# python3 -m pip install art

import art

print(art.text2art("Python"))

import translate

german_translator = translate.Translator(to_lang="de")
id_translator = translate.Translator(to_lang="id")
print(german_translator.translate("Good Morning!"))
print(id_translator.translate("Good Morning!"))
