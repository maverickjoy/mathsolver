import math_thesaurus

'''
Extract group of alphabetic numbers
'''
def _extractGroups(sentence):
    groups = []
    groupsPos = []
    sentence = sentence.lower()  # converting input to lowercase
    split_words = sentence.strip().split()  # strip extra spaces and split sentence into words
    andCount = 0
    andFlag = False
    lastNumberWord = -1
    group = []
    groupPos = []
    scaleMultiplierForPresentGroupPresent = False
    for idx, word in enumerate(split_words):
        if word == 'and':
            andCount += 1
            if andCount % 2 == 0:
                andFlag = True
            # if and comes without a SCALE Multiplier it is a seperator hence make it even say 2
            if not scaleMultiplierForPresentGroupPresent:
                andCount = 2
                andFlag = True

        if word in math_thesaurus.NON_SEPERATORS and not andFlag:
            if len(group) == 0:
                groupPos.append(idx)
            if word in math_thesaurus.SCALES:
                scaleMultiplierForPresentGroupPresent = True
            group.append(word)
            lastNumberWord = idx
        else:
            scaleMultiplierForPresentGroupPresent = False
            if andFlag:
                andFlag = False
            if len(group) > 0:
                groups.append(group)
                groupPos.append(lastNumberWord)
                groupsPos.append(groupPos)

            group = []
            groupPos = []

    if len(group) > 0:
        groups.append(group)
        groupPos.append(lastNumberWord)
        groupsPos.append(groupPos)

    return (groups, groupsPos)


def _numberFormation(number_words):
    numbers = []
    for number_word in number_words:
        numbers.append(math_thesaurus.NUMBER_SYSTEM[number_word])
    if len(numbers) == 4:
        return (numbers[0] * numbers[1]) + numbers[2] + numbers[3]
    elif len(numbers) == 3:
        return numbers[0] * numbers[1] + numbers[2]
    elif len(numbers) == 2:
        if 100 in numbers:
            return numbers[0] * numbers[1]
        else:
            return numbers[0] + numbers[1]
    else:
        return numbers[0]


def _getDecimalSum(decimal_digit_words):
    decimal_number_str = []
    for dec_word in decimal_digit_words:
        if(dec_word not in math_thesaurus.DECIMAL_WORDS):
            return 0
        else:
            decimal_number_str.append(math_thesaurus.NUMBER_SYSTEM[dec_word])
    final_decimal_string = '0.' + ''.join(map(str,decimal_number_str))
    return float(final_decimal_string)


def _extractNumber(wordList):
    clean_numbers = []
    clean_decimal_numbers = []

    # removing and, & etc.
    for word in wordList:
        if word in math_thesaurus.NUMBER_SYSTEM:
            clean_numbers.append(word)

    # Error if user enters million,billion, thousand or decimal point twice
    if clean_numbers.count('thousand') > 1 or clean_numbers.count('million') > 1 or clean_numbers.count('billion') > 1 or clean_numbers.count('point')> 1:
        return (False, "Redundant number word! Please enter a valid number word (eg. two million twenty three thousand and forty nine)")

    # separate decimal part of number (if exists)
    if clean_numbers.count('point') == 1:
        clean_decimal_numbers = clean_numbers[clean_numbers.index('point')+1:]
        clean_numbers = clean_numbers[:clean_numbers.index('point')]

    billion_index = clean_numbers.index('billion') if 'billion' in clean_numbers else -1
    million_index = clean_numbers.index('million') if 'million' in clean_numbers else -1
    thousand_index = clean_numbers.index('thousand') if 'thousand' in clean_numbers else -1

    if (thousand_index > -1 and (thousand_index < million_index or thousand_index < billion_index)) or (million_index>-1 and million_index < billion_index):
        return (False, "Malformed number! Please enter a valid number word (eg. two million twenty three thousand and forty nine)")

    total_sum = 0  # storing the number to be returned

    if len(clean_numbers) > 0:
        if len(clean_numbers) == 1:
                total_sum += math_thesaurus.NUMBER_SYSTEM[clean_numbers[0]]
        else:
            if billion_index > -1:
                billion_multiplier = _numberFormation(clean_numbers[0:billion_index])
                total_sum += billion_multiplier * 1000000000

            if million_index > -1:
                if billion_index > -1:
                    million_multiplier = _numberFormation(clean_numbers[billion_index+1:million_index])
                else:
                    million_multiplier = _numberFormation(clean_numbers[0:million_index])
                total_sum += million_multiplier * 1000000

            if thousand_index > -1:
                if million_index > -1:
                    thousand_multiplier = _numberFormation(clean_numbers[million_index+1:thousand_index])
                elif billion_index > -1 and million_index == -1:
                    thousand_multiplier = _numberFormation(clean_numbers[billion_index+1:thousand_index])
                else:
                    thousand_multiplier = _numberFormation(clean_numbers[0:thousand_index])
                total_sum += thousand_multiplier * 1000

            if thousand_index > -1 and thousand_index != len(clean_numbers)-1:
                hundreds = _numberFormation(clean_numbers[thousand_index+1:])
            elif million_index > -1 and million_index != len(clean_numbers)-1:
                hundreds = _numberFormation(clean_numbers[million_index+1:])
            elif billion_index > -1 and billion_index != len(clean_numbers)-1:
                hundreds = _numberFormation(clean_numbers[billion_index+1:])
            elif thousand_index == -1 and million_index == -1 and billion_index == -1:
                hundreds = _numberFormation(clean_numbers)
            else:
                hundreds = 0
            total_sum += hundreds

    # adding decimal part to total_sum (if exists)
    if len(clean_decimal_numbers) > 0:
        decimal_sum = _getDecimalSum(clean_decimal_numbers)
        total_sum += decimal_sum

    return (True, total_sum)

def replaceAlphabeticalNumbers(sentence):
    groups, groupsPos = _extractGroups(sentence)

    if len(groups) == 0:
        return (True, sentence)

    split_words = sentence.strip().split()  # strip extra spaces and split sentence into words
    numbers = []
    for group in groups:
        data = _extractNumber(group)
        if not data[0]:
            return data
        numbers.append(data[1])

    numberCnt = 0
    replaceList = []
    for idx, word in enumerate(split_words):
        if len(groupsPos) > numberCnt and  idx >= groupsPos[numberCnt][0] and idx <= groupsPos[numberCnt]:
            if idx == groupsPos[numberCnt][1]:
                replaceList.append(str(numbers[numberCnt]))
                numberCnt += 1
        else:
            replaceList.append(word)
    return (True, ' '.join(replaceList))


if __name__ == "__main__":
    print replaceAlphabeticalNumbers("What is sum of 5 and 6")
    print replaceAlphabeticalNumbers("What is sum of 5 and seven")
    print replaceAlphabeticalNumbers("What is sum of five hundred and seven and five and six")
    print replaceAlphabeticalNumbers("What is sum of five hundred and seven and five and six hundred and six")
    print replaceAlphabeticalNumbers("what is five hundred divided by forty five point six seven when added with three hundred and forty two")
    while True:
        sentence = raw_input("Please enter a sentence : ")
        print solve(sentence)
