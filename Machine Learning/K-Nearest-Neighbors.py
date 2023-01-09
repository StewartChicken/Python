import warnings
from math import sqrt

#Calculates the euclidean distance between two points of n dimensions
def euclidean_distance(point_a, point_b):

    #Points must be of the same dimensional size to compare distance
    if not len(point_a) == len(point_b):
        warnings.warn('points are not of the same dimensional size')

    values = []

    for i in range(len(point_a)):
        values.append((point_a[i] - point_b[i]) ** 2)

    #Returns the euclidean distance (using distance formula)
    return sqrt(sum(values))

def classify(data, point):

    #Creates a 'k' value which tells the algorithm how many points to compare to the to-be-classified point
    if len(data) % 2 == 0:
        k = len(data) + 1
    else:
        k = len(data) + 2

    distances = []

    for i in data:
        for ii in data[i]:
            distances.append([i, euclidean_distance(ii, point)])

    #dictionary of distance each point is from the to-be-classified point, sorted by distance 
    sorted_distances = sorted(distances, key = lambda x: x[1])

    #Dictionary containing the counts of each classification's appearance within the first
    #'k' data points of the data
    counts = {}

    for i in data:
        counts[i] = 0

    #Keeps count of how many times each class appeared in the closest 'k' points 
    for i in range(k):
        counts[sorted_distances[i][0]] += 1

    #Determines the most likely classification as well as the number of closest data points that classification had. 
    max_class = None
    num_max = 0
    for i in counts:
        if counts[i] > num_max:
            num_max = counts[i]
            max_class = i

    print("This data point has been classified under the '" + max_class + "' class with a confidence of " + (str)(num_max / k))

    return max_class, num_max / k




