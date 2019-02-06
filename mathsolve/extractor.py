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
    evenAndFlag = False
    lastNumberWord = -1
    group = []
    groupPos = []
    for idx, word in enumerate(split_words):
        if word == 'and':
            andCount += 1
            if andCount % 2 == 0:
                evenAndFlag = True
        if word in math_thesaurus.NON_SEPERATORS and not evenAndFlag:
            if len(group) == 0:
                groupPos.append(idx)
            group.append(word)
            lastNumberWord = idx
        else:
            if evenAndFlag:
                evenAndFlag = False
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


while True:
    sentence = raw_input("Enter Sentence : ")
    print _extractGroups(sentence)
