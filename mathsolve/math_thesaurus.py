import math


'''
import re
>>> str = "h3110 23 cat 444.4 rabbit 11 -2 dog"
>>> [float(s) for s in re.findall(r'-?\d+\.?\d*', str)]

'''

# Opperations related to these operators only possible
BINARY_OPERATORS = {
    '^', '*', '/', '+', '-'
}

# Opperations related to these operators only possible but only one operand needed
UNARY_OPERATORS =  {
    'square', 'cube', 'sqrt', 'log'
}


NUMBER_SYSTEM = {
    'zero'     : 0,
    'one'      : 1,
    'two'      : 2,
    'three'    : 3,
    'four'     : 4,
    'five'     : 5,
    'six'      : 6,
    'seven'    : 7,
    'eight'    : 8,
    'nine'     : 9,
    'ten'      : 10,
    'eleven'   : 11,
    'twelve'   : 12,
    'thirteen' : 13,
    'fourteen' : 14,
    'fifteen'  : 15,
    'sixteen'  : 16,
    'seventeen': 17,
    'eighteen' : 18,
    'nineteen' : 19,
    'twenty'   : 20,
    'thirty'   : 30,
    'forty'    : 40,
    'fifty'    : 50,
    'sixty'    : 60,
    'seventy'  : 70,
    'eighty'   : 80,
    'ninety'   : 90,
    'hundred'  : 100,
    'thousand' : 1000,
    'million'  : 1000000,
    'billion'  : 1000000000,
    'point'    : '.'
}

# only single digit decimals written because when it comes to decimals we write `fifty three point six six seven > 53.667`
DECIMAL_WORDS = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

NON_SEPERATORS = NUMBER_SYSTEM.keys()
NON_SEPERATORS.extend(['and'])
