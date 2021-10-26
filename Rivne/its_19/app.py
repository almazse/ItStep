# RegEx
# - words
# - letters
# - special commands need to use ecran symbol \
# - \d - one digit
# - \D - all without digits
# - . - any symbol
# - \w - any digit or letter
# - \W - any symbol but not digit or letter
# - \s - breakspace
# - \S - all but not or breakspace
# - \w+ - words or numbers
# - + - 1 and more
# - ? - 0 or 1
# - * - 0 or more
# - ^ - begin of line
# - $ - end of line
# - [] - group
# - {n} - n count repeat
# - {n, m} - from n to m count repeat

import re

TEST_STRING = """
Guido van Rossum began working on Python in the late 1980s, as a successor 
to the ABC programming language, and first released it in 1991 as Python 
0.9.0. [32] Python 2.0 was released in 2000 Guido and introduced new 
features, such as list comprehensions and a garbage collection system 
using reference counting. Guido Python 3.0 was released in 2008 and was a 
major revision of the language that is not completely backward-compatible. 
Python 2 was discontinued with version 2.7.18 in 2020. Guido

email@valid.com
email@valid.ua
email@valid.ru
email@valid.mil

email@@valid.com

127.0.0.1

https://regex101.com/
http://regex101.com/1/
http://www.regex101.com/
"""

# pattern = re.compile(r'https?://(www\.)?([a-zA-Z-0-9]+)(\.[\w/]+)')
# matches = pattern.findall(TEST_STRING)
# matches = pattern.finditer(TEST_STRING)
#
# for match in matches:
#     print(match.group(0))
#     print(match.group(1))
#     print(match.group(2))
#     print(match.group(3))
#     print(match.group(4))

# pattern = re.compile(f'([a-zA-Z0-9-_\*\.]+)@([a-zA-Z0-9]+\.?)+')

TEST_TEXT = """
Guido van Rossum began working on Python in the late 1980s, as a successor 
to the ABC programming language, and first released it in 1991 as Python 
0.9.0.
"""

pattern = re.compile(f'Python')
matches = pattern.finditer(TEST_TEXT)

rez = pattern.sub()