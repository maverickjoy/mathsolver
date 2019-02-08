import re
import math
import extractor
import math_thesaurus



def _extractOperators(sentence):
    operatorsList = []
    operatorsFound = []
    # There is a reason for appending unary operators first
    operatorsList.extend(math_thesaurus.UNARY_OPERATORS)
    operatorsList.extend(math_thesaurus.BINARY_OPERATORS)
    for operator in operatorsList:
        if any(synonym in sentence for synonym in math_thesaurus.OPERATOR_SYNONYMS[operator]):
            operatorsFound.append(operator)

    return operatorsFound

'''
    Returns a tuple => (status, description, value)
'''
def solve(sentence):
    res = extractor.replaceAlphabeticalNumbers(sentence)
    if not res[0]:
        return (False, res[1], 0)

    mathString = res[1].lower()
    operands = [float(s) for s in re.findall(r'-?\d+\.?\d*', mathString)]
    operators = _extractOperators(mathString)
    # print operators
    if len(operators) < 1:
        return (False, "No operator found for operations", 0)

    # TODO: For now only doing for single operator
    operator = operators[0]

    if operator == '^':
        if len(operands) < 2:
            return (False, "Less operands specified for doing power, Two Needed", 0)
        res = math.pow(operands[0], operands[1])
        return (True, "Power of {} and {} is {}".format(operands[0], operands[1], res), res)

    if operator == '*':
        if len(operands) < 2:
            return (False, "Less operands specified for doing multiplication, Two Needed", 0)
        res = operands[0] * operands[1]
        return (True, "Multiplication of {} and {} is {}".format(operands[0], operands[1], res), res)

    if operator == '/':
        if len(operands) < 2:
            return (False, "Less operands specified for doing division, Two Needed", 0)
        res = float(operands[0]) / operands[1]
        return (True, "Division of {} and {} is {}".format(operands[0], operands[1], res), res)

    if operator == '+':
        if len(operands) < 2:
            return (False, "Less operands specified for doing sum, Two Needed", 0)
        res = math.fsum(operands)
        return (True, "Sum of numbers is {}".format(res), res)

    if operator == '-':
        if len(operands) < 2:
            return (False, "Less operands specified for doing subtraction, Two Needed", 0)
        res = operands[0] - operands[1]
        return (True, "Subtraction of {} and {} is {}".format(operands[0], operands[1], res), res)

    if operator == 'square':
        if len(operands) < 1:
            return (False, "Less operands specified for doing square, One Needed", 0)
        res = operands[0] * operands[0]
        return (True, "Square of {} is {}".format(operands[0], res), res)

    if operator == 'cube':
        if len(operands) < 1:
            return (False, "Less operands specified for doing cube, One Needed", 0)
        res = operands[0] * operands[0] * operands[0]
        return (True, "Cube of {} is {}".format(operands[0], res), res)

    if operator == 'sqrt':
        if len(operands) < 1:
            return (False, "Less operands specified for doing square root, One Needed", 0)
        res = math.sqrt(operands[0])
        return (True, "Square root of {} is {}".format(operands[0], res), res)

    if operator == 'log':
        # Assuming log base 10 which is default for logarithmic operations
        if len(operands) < 1:
            return (False, "Less operands specified for doing logarithm, One Needed", 0)
        res = math.log10(operands[0])
        return (True, "Log of {} is {}".format(operands[0], res), res)

    return (False , "Mathematical equation if any in the sentence could not be decoded", 0)



if __name__ == "__main__":
    print solve("What is sum of 5 and 6")
    print solve("What is multiplication of 5 and seven")
    print solve("What is division of five hundred and seven and five")
    print solve("what will be result of when 11 is multiplied with seven")
    print solve("What is sum of five hundred and seven and five and six hundred and six")
    while True:
        sentence = raw_input("Please enter a sentence : ")
        print solve(sentence)
