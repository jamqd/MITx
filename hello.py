#midterm
import string
from builtins import print


def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    n = 0
    minN = -1
    while base ** n <= num:
        if n == 0 :
            minDif = abs(num - base ** n)
            minN = n
        elif abs(num - base ** n) < minDif:
            minDif = abs(num - base ** n)
            minN = n
        n += 1
    if abs(num - base ** n) < minDif:
        minDif = abs(num - base ** n)
        minN = n
    return minN

def getSublists(L, n):
    subs = []
    if isinstance(L, range):
        for x in range(0, abs(L.stop - L.start) - n + 1, abs(L.step)):
            if L.step < 0:
                subs.append(range(L.start - x, L.start - x - n, L.step))
            else:
                subs.append(range(L.start + x, L.start + x + n, L.step))
    else:
        for x in range(0, len(L) - n + 1):
            a = []
            for y in range(0, n):
                a.append(L[x + y])
            subs.append(a)
    return subs

def keysWithValue(aDict, target):
    '''
    aDict: a dictionary
    target: an integer
    '''
    a = []
    keys = list(aDict.keys())
    for n in keys:
        if aDict[n] == target:
            a.append(n)
    a.sort()
    return a

def flatten(aList):
    '''
    aList: a list
    Returns a copy of aList, which is a flattened version of aList
    '''
    a = []
    if len(aList) == 1 and not isinstance(aList[0], list):
        return aList
    else:
        for n in aList:
            if isinstance(n, list):
                a += flatten(n)
            else:
                 a.append(n)
    return a


def f(x, y):
    return x + y


def score(word, f):
    """
       word, a string of length > 1 of alphabetical
             characters (upper and lowercase)
       f, a function that takes in two int arguments and returns an int

       Returns the score of word as defined by the method:

    1) Score for each letter is its location in the alphabet (a=1 ... z=26)
       times its distance from start of word.
       Ex. the scores for the letters in 'adD' are 1*0, 4*1, and 4*2.
    2) The score for a word is the result of applying f to the
       scores of the word's two highest scoring letters.
       The first parameter to f is the highest letter score,
       and the second parameter is the second highest letter score.
       Ex. If f returns the sum of its arguments, then the
           score for 'adD' is 12
    """
    ascii = string.ascii_letters
    locDict = {}
    count = 1
    for n in ascii:
        locDict[n] = count
        if count == 26:
            count = 1
        else:
            count += 1
    letterScores = []
    for n in range(0, len(word)):
        letterScores.append(locDict[word[n]] * n)
    high1 = max(letterScores)
    letterScores.remove(high1)
    high2 = max(letterScores)
    if high1 > high2:
        return f(high1, high2)
    else:
        return f(high2, high1)

