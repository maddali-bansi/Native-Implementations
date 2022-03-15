# Author Bansi Maddali

import pandas as pd
import math


# Where x and y are two data points
def euclidean_distance(cx, cy, x, y):
    return math.sqrt((cx - x) ^ 2 + (cy - y) ^ 2)


def k_means(k_clusters, data_df):
    global min
    clusters = data_df.sample(k_clusters, replace=False)  # Randomly Choose Clusters from available Data Points
    final_clusters = list()
    assigned_cluster = 0
    if k_clusters <= len(data_df):  # Number of clusters should be less or equal to actual data points
        for index, datapoint in data_df.iterrows():
            min = math.inf
            x = datapoint['x']
            y = datapoint['y']

            # Find the nearest Cluster
            cluster_id = 1
            for index1, cluster in clusters.iterrows():
                cx = cluster['x']
                cy = cluster['y']
                distance = euclidean_distance(cx, cy, x, y)
                if distance < min:
                    min = distance
                    assigned_cluster = cluster_id
                cluster_id += 1
            print(x, y, " assigned cluster = ", assigned_cluster, "Cluster Co-ordinates = ",
                  clusters.values[assigned_cluster - 1])


if __name__ == '__main__':
    k = 3
    data = {'x': [1, 2, 3, 4, 5],
            'y': [100, 200, 300, 400, 500]
            }
    df = pd.DataFrame(data)
    k_means(k, df)
