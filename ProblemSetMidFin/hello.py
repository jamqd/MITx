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

#final

def is_triangular(k):
    """
    k, a positive integer
    returns True if k is triangular and False if not
    """
    sum = 0
    count = 1
    while sum < k:
        sum += count
        if sum == k:
            return True
        count += 1
    return False

def largest_odd_times(L):
    """ Assumes L is a non-empty list of ints
        Returns the largest element of L that occurs an odd number
        of times in L. If no such element exists, returns None """
    freq = {}
    for n in range (0, len(L)):
        if L[n] in freq:
            freq[L[n]] += 1
        else:
            freq[L[n]] = 1

    largestL = None

    for i in freq:
        if (largestL == None or i > largestL) and freq[i] % 2 == 1:
            largestL = i
    return largestL

def cipher(map_from, map_to, code):
    """ map_from, map_to: strings where each contain
                          N unique lowercase letters.
        code: string (assume it only contains letters also in map_from)
        Returns a tuple of (key_code, decoded).
        key_code is a dictionary with N keys mapping str to str where
        each key is a letter in map_from at index i and the corresponding
        value is the letter in map_to at index i.
        decoded is a string that contains the decoded version
        of code using the key_code mapping. """
    key_code = {}
    for n in range(0, len(map_from)):
        key_code[map_from[n]] = map_to[n]

    decoded = ''

    for n in code:
        decoded += key_code[n]

    return (key_code, decoded)


## DO NOT MODIFY THE IMPLEMENTATION OF THE Person CLASS ##
class Person(object):
    def __init__(self, name):
        # create a person with name name
        self.name = name
        try:
            firstBlank = name.rindex(' ')
            self.lastName = name[firstBlank + 1:]
        except:
            self.lastName = name
        self.age = None

    def getLastName(self):
        # return self's last name
        return self.lastName

    def setAge(self, age):
        # assumes age is an int greater than 0
        # sets self's age to age (in years)
        self.age = age

    def getAge(self):
        # assumes that self's age has been set
        # returns self's current age in years
        if self.age == None:
            raise ValueError
        return self.age

    def __lt__(self, other):
        # return True if self's name is lexicographically less
        # than other's name, and False otherwise
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName

    def __str__(self):
        # return self's name
        return self.name


class USResident(Person):
    """
    A Person who resides in the US.
    """

    def __init__(self, name, status):
        """
        Initializes a Person object. A USResident object inherits
        from Person and has one additional attribute:
        status: a string, one of "citizen", "legal_resident", "illegal_resident"
        Raises a ValueError if status is not one of those 3 strings
        """
        Person.__init__(self, name)
        if status == 'citizen' or status == 'legal_resident' or status == 'illegal_resident':
            self.status = status
        else:
            raise ValueError

    def getStatus(self):
        """
        Returns the status
        """
        return self.status


class myDict(object):
    """ Implements a dictionary without using a dictionary """

    def __init__(self):
        """ initialization of your representation """
        self.key = []
        self.val = []

    def assign(self, k, v):
        """ k (the key) and v (the value), immutable objects  """
        if k not in self.key:
            self.key.append(k)
            self.val.append(v)
        else:
            index = self.key.index(k)
            self.val[index] = v


    def getval(self, k):
        """ k, immutable object  """
        if k not in self.key:
            raise KeyError
        else:
            index = self.key.index(k)
            return self.val[index]

    def delete(self, k):
        """ k, immutable object """
        if k not in self.key:
            raise KeyError
        else:
            index = self.key.index(k)
            self.key.pop(index)
            self.val.pop(index)

a = myDict()
a.assign(1,2)
a.assign(3,4)
print(a.key)
print(a.val)
a.delete(1)
print(a.key)
print(a.val)
print(a.getval(4))

