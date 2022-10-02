"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""


def frequencies(items):

    frequencies = {}
    for item in items:
        """
        key_list = list(frequencies.keys())
        for key in key_list:
            if item == key:
                frequency = frequencies[key]
                frequency += 1
                frequencies[item] = frequency
            elif key.isDigit():
                if item == int(key):
                    frequency = frequencies[key]
                    frequency += 1
                    frequencies[key] = frequency
            else:
                frequencies[item] = 1
        """
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