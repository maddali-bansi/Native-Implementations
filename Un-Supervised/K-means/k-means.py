# Author Bansi Maddali
import numpy.random
import pandas as pd
import math


# Where x and y are two data points
def euclidean_distance(cx, cy, x, y):
    return math.sqrt((cx - x) ** 2 + (cy - y) ** 2)


def k_means(k_clusters, data_df):
    clusters = data_df.sample(k_clusters, replace=False)
    data_df['cluster'] = 0
    converge = False
    iteration = 0
    assigned_cluster = 0
    while not converge:
        # Assign Clusters
        # print("Clusters = ", clusters)
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

        # print(data_df)
        # print(clusters)
        # print("=============================")
        if iteration != 0 and prev_df.equals(data_df):
            converge = True
        else:
            # Re-Compute Centroids(Clusters)
            clusters = data_df.groupby('cluster').mean()
            prev_df = data_df
        iteration += 1
    return data_df, clusters, iteration


if __name__ == '__main__':
    k = 50
    data = {'x': numpy.random.randint(low=1, high=10, size=1000),
            'y': numpy.random.randint(low=2, high=8, size=1000)
            }
    df = pd.DataFrame(data)
    df, cluster_centers, itr = k_means(k, df)
    print("K Mean converged after ", itr, " iterations : ")
    # print("============")
    # print("Clustered Rows")
    # print(df)
    # print("Cluster Co-ordinates")
    print(cluster_centers)
