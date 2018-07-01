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
def f(x):
    return (x+15)**0.5 + x**0.5 == 15
print(solveit(f))

#### This test case prints 0 ####
def f(x):
    return x == 0
print(solveit(f))

#Final