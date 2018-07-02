#Quiz
def song_playlist(songs, max_size):
    """
    songs: list of tuples, ('song_name', song_len, song_size)
    max_size: float, maximum size of total songs that you can fit

    Start with the song first in the 'songs' list, then pick the next
    song to be the one with the lowest file size not already picked, repeat

    Returns: a list of a subset of songs fitting in 'max_size' in the order
             in which they were chosen.
    """

    songsCopy = songs[:]
    listS = []
    if songsCopy[0][2] > max_size:
        return listS
    listS.append(songsCopy[0][0])
    filled = songsCopy[0][2]
    songsCopy.remove(songsCopy[0])
    n = 0
    while filled < max_size and n != len(songsCopy) - 1:
        smallest = max_size
        smallestI = -1
        for n in range(len(songsCopy)):
            if songsCopy[n][2] < smallest:
                smallest = songsCopy[n][2]
                smallestI = n
        if smallestI != -1 and songsCopy[smallestI][2] < max_size - filled:
            listS.append(songsCopy[smallestI][0])
            songsCopy.remove(songsCopy[smallestI])
            filled += smallest
        else:
            break
    return listS
#
# songs =  [('a', 4.4, 4.0), ('b', 3.5, 7.7), ('c', 5.1, 6.9), ('d', 2.7, 1.2)]
# print(song_playlist(songs, 20))

def max_contig_sum(L):
    """ L, a list of integers, at least one positive
    Returns the maximum sum of a contiguous subsequence in L """
    maxSum = L[0]
    for n in range(len(L) + 1):
        sum = 0
        for i in range(len(L) - n + 1):
            sum = 0
            for k in range(n):
                sum += L[i + k]
            if sum > maxSum:
                maxSum = sum
    return maxSum

#print(max_contig_sum([3, 4, -1, 5, -4]))

def solveit(test):
    """ test, a function that takes an int parameter and returns a Boolean
        Assumes there exists an int, x, such that test(x) is True
        Returns an int, x, with the smallest absolute value such that test(x) is True
        In case of ties, return any one of them.
    """
    count = 0
    while True:
        if test(count) == True:
            return count
        elif test(-count) == True:
            return -count
        else:
            count += 1

#### This test case prints 49 ####
# def f(x):
#     return (x+15)**0.5 + x**0.5 == 15
#print(solveit(f))

#### This test case prints 0 ####
# def f(x):
#     return x == 0
# print(solveit(f))

#Final

#import random
def drawing_without_replacement_sim(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    4 red and 4 green balls. Balls are not replaced once
    drawn. Returns a float - the fraction of times 3
    balls of the same color were drawn in the first 3 draws.
    '''
    suc = 0
    for n in range(numTrials):
        bucket = [1,1,1,1,0,0,0,0]
        drawn = []
        for i in range(3):
            a = random.choice(bucket)
            drawn.append(a)
            bucket.remove(a)
        if sum(drawn) == 0 or sum(drawn) == 3:
            suc += 1
    return suc/numTrials

#print(drawing_without_replacement_sim(100))

import random, pylab


# You are given this function
def getMeanAndStd(X):
    mean = sum(X) / float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean) ** 2
    std = (tot / len(X)) ** 0.5
    return mean, std


# You are given this class
class Die(object):
    def __init__(self, valList):
        """ valList is not empty """
        self.possibleVals = valList[:]

    def roll(self):
        return random.choice(self.possibleVals)


# Implement this -- Coding Part 1 of 2
def makeHistogram(values, numBins, xLabel, yLabel, title=None):
    """
      - values, a sequence of numbers
      - numBins, a positive int
      - xLabel, yLabel, title, are strings
      - Produces a histogram of values with numBins bins and the indicated labels
        for the x and y axis
      - If title is provided by caller, puts that title on the figure and otherwise
        does not title the figure
    """
    if title != None:
        pylab.title(title)
    pylab.hist(values, bins=numBins)
    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel)
    pylab.show()

#makeHistogram([1,2,3,3,4,5,6,6,6,7,8,8,8,8,8,8,9], 4, 'x', 'y')

# Implement this -- Coding Part 2 of 2
def getAverage(die, numRolls, numTrials):
    """
      - die, a Die
      - numRolls, numTrials, are positive ints
      - Calculates the expected mean value of the longest run of a number
        over numTrials runs of numRolls rolls
      - Calls makeHistogram to produce a histogram of the longest runs for all
        the trials. There should be 10 bins in the histogram
      - Choose appropriate labels for the x and y axes.
      - Returns the mean calculated
    """
    longestRuns = []
    for n in range(numTrials):
        rolled = []
        for i in range(numRolls):
            rolled.append(die.roll())
        longestCount = 0
        currentCount = 0
        current = -1
        for j in range(len(rolled)):
            if j == 0:
                currentCount = 1
                current = rolled[j]
                longestCount = 1
            else:
                if rolled[j] == current:
                    currentCount += 1
                    if currentCount > longestCount:
                        longestCount = currentCount
                else:
                    if currentCount > longestCount:
                        longestCount = currentCount
                    current = rolled[j]
                    currentCount = 1
        longestRuns.append(longestCount)
    makeHistogram(longestRuns, 10, 'Longest Runs', 'Frequency')
    return sum(longestRuns)/len(longestRuns)


# One test case
#print(getAverage(Die([1, 2, 3, 4, 5, 6, 6, 6, 7]), 500, 10000))

import numpy as np
def find_combination(choices, total):
    """
    choices: a non-empty list of ints
    total: a positive int

    Returns result, a numpy.array of length len(choices)
    such that
        * each element of result is 0 or 1
        * sum(result*choices) == total
        * sum(result) is as small as possible
    In case of ties, returns any result that works.
    If there is no result that gives the exact total,
    pick the one that gives sum(result*choices) closest
    to total without going over.
    """
    # bestSum = -1
    # best = np.array([])
    # for n in range(len(choices) + 1):
    #     template = []
    #     for i in range(n):
    #         template.append(1)
    #     for v in range(len(choices) - n):
    #         template.append(0)
    #     perms = list(itertools.permutations(template, len(choices)))
    #     for d in range(len(perms)):
    #         perms[d] = np.array(perms[d])
    #     for b in perms:
    #         sum = np.sum(np.array(b) * np.array(choices))
    #         if sum == total:
    #             return b
    #         elif sum < total and sum > bestSum:
    #             best = np.array(b)
    #             bestSum = sum
    # return best
    bestSum = -1
    best = []
    for n in range(len(choices) + 1):
        for i in range(len(choices) - n + 1):
            result = []
            for k in range(i):
                result.append(0)
            for j in range(n):
                result.append(1)
            for h in range(len(choices) - n - i):
                result.append(0)
            sum = np.sum(np.array(choices) * np.array(result))
            if sum == total:
                return np.array(result)
            elif sum < total and sum > bestSum:
                best = np.array(result)
                bestSum = sum
    return best

a = find_combination([45,6,7,4,9], 2)
print(a)
print(type(a))
