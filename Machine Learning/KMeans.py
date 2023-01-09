import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import random
style.use('ggplot')

data_points = np.array([[1, 4], [1, 1], [2, 3], [4, 1], [3, 2], [2, 1], [1, 3],
                        [10, 5], [13, 7], [15, 8], [13, 6], [11, 9], [14, 10], [15, 5],
                        [6, 17], [6, 18], [7, 15], [5, 19], [8, 16], [9, 16], [5, 20]])

#test_data = np.array([[1, 1, 2, 4], [2, 4, 3, 1]])
#plt.scatter(test_data[0], test_data[1])
plt.scatter(data_points[:, 0], data_points[:, 1])

def get_first_centroid(data, k):
    centroid_list = []
    filled = False

    while not filled:
        viable = True
        if len(centroid_list) == k:
            filled = True
            break
        selected_index = random.choice(range(len(data)))
        if len(centroid_list) > 0:
            for i in centroid_list:
                if i[0] == data[selected_index][0] and i[1] == data[selected_index][1]:
                    viable = False
                    break

        if viable:
            centroid_list.append([data[selected_index][0], data[selected_index][1]])

    return centroid_list

## np.linalg.norm(vector)
def find_closest_points(data, centroid, k):
    cluster_size = round(len(data) / k)
    distances = []
    #for point in data:
        #.append(np.linalg.norm([1, 1], ))



centroids = get_first_centroid(data_points, 3)
#print(centroids)

plt.scatter([centroids[0][0], centroids[1][0], centroids[2][0]], [centroids[0][1], centroids[1][1], centroids[2][1]])
#plt.show()





