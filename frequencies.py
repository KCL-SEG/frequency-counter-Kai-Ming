"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""


def frequencies(items):

    frequencies = {}
    for item in items:
        try:
            item % 1 == 0
            item = str(item)
            if item in frequencies: 
                frequency = frequencies[item]
                frequency += 1
                frequencies[item] = frequency
            else:
                frequencies[item] = 1
        except TypeError:
            if item in frequencies: 
                frequency = frequencies[item]
                frequency += 1
                frequencies[item] = frequency
            else:
                frequencies[item] = 1
        """
        try:
            frequency = frequencies[item]
            frequency += 1
            frequencies[item] = frequency
        except KeyError:
            frequencies[item] = 1
        """
    #print(frequencies)
    return frequencies
"""
items = ['a', 'a', 'b', 'b', 'b', 'c']
frequencies(items)

if ('1' == 1):
    print('t')
else:
    print('f')
    """