###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    cow_dict = cows.copy()
    trips = []
    orderCows = []

    for i in range(0, len(cow_dict)):
        largest = 0
        largestCow = None
        for n in cow_dict:
            if cow_dict[n] > largest:
                largest = cow_dict[n]
                largestCow = n
        orderCows.append(largestCow)
        del cow_dict[largestCow]


    while len(orderCows) > 0:
        trip = []
        count = 0
        loaded = 0
        while loaded < limit and len(orderCows) > 0 and count < len(orderCows):
            if cows[orderCows[count]] <= limit - loaded:
                trip.append(orderCows[count])
                loaded += cows[orderCows[count]]
                orderCows.pop(count)
            else:
                count += 1
        trips.append(trip)

    return trips






# Problem 2
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    count = 0
    partitions = []
    for n in get_partitions(cows):
        partitions.append(n)
    partitions.sort(key = len)
    for n in partitions:

        passed = True
        for i in n:
            sum = 0
            for o in i:
                sum += cows[o]
            if sum > limit:

                passed = False
                break
        if passed:
            return n
    return None
        
# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    pass


"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

cows = load_cows("ps1_cow_data.txt")
limit = 10
print(cows)

print()

start = time.time()
print(greedy_cow_transport(cows, limit))
end = time.time()
print(end - start)


start = time.time()
print(brute_force_cow_transport(cows, limit))
end = time.time()
print(end - start)






