# Author Bansi Maddali

import pandas as pd
import math


# Where x and y are two data points
def euclidean_distance(cx, cy, x, y):
    return math.sqrt((cx - x) ** 2 + (cy - y) ** 2)


def k_means(k_clusters, data_df):
    clusters = data_df.sample(k_clusters, replace=False)
    data_df['cluster'] = 0
    converge = False
    assigned_cluster = 0
    while not converge:
        # Assign Clusters
        for index, datapoint in data_df.iterrows():
            minimum = math.inf

            # Single data point
            x = datapoint['x']
            y = datapoint['y']

            # Find the nearest Cluster
            cluster_id = 1
            for index1, cluster in clusters.iterrows():
                cx = cluster['x']
                cy = cluster['y']
                distance = euclidean_distance(cx, cy, x, y)
                if distance < minimum:
                    minimum = distance
                    data_df.at[index, 'cluster'] = cluster_id
                cluster_id += 1
        print(data_df)
        print(clusters)
        print("=============================")
        if clusters.equals(data_df.groupby('cluster').mean()):
            converge = True
        else:
            clusters = data_df.groupby('cluster').mean()


if __name__ == '__main__':
    k = 3
    data = {'x': [800, 10, 30, 40, 500],
            'y': [900, 20, 40, 50, 600]
            }
    df = pd.DataFrame(data)
    k_means(k, df)
