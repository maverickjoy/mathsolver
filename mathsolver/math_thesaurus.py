import math

# Opperations related to these operators only possible
BINARY_OPERATORS = [ '^', '*', '/', '+', '-']

# Opperations related to these operators only possible but only one operand needed
UNARY_OPERATORS =  ['square', 'cube', 'sqrt', 'log']

# Operator Synonyms
OPERATOR_SYNONYMS = {
    '^'      : ["power", '^'],
    '*'      : ["multiply", "multiplication", "multiple", "multiplying", "multiplied", "*"],
    '/'      : ["divide", "division", "dividing", "divided", "/"],
    '+'      : ["sum", "add", "addition", "summing", "plus", "summision", "added", "+"],
    '-'      : ["minus", "negation", "negating", "subtract", "subtraction", "subtracted", "-"],
    'square' : ["square", "squaring", "power of 2", "multiplied by itself"],
    'cube'   : ["cube", "cubing", "power of 3", "multiplied by itself three times"],
    'sqrt'   : ["square root", "squareroot", "sqrt"],
    'log'    : ["log", "logarithm"]
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

SCALES = ['hundred', 'thousand', 'million', 'billion']

# only single digit decimals written because when it comes to decimals we write `fifty three point six six seven > 53.667`
DECIMAL_WORDS = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

NON_SEPERATORS = NUMBER_SYSTEM.keys()
NON_SEPERATORS.extend(['and'])
