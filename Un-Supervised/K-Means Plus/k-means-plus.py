# Author Bansi Maddali
import numpy.random
import pandas as pd
import math


def euclidean_distance(cx, cy, cz, x, y, z):
    return math.sqrt((cx - x) ** 2 + (cy - y) ** 2 + (cz - z) ** 2)


def get_cluster_coordinates_k_mean_plus(k_clusters, data_df):
    initial_point_index = data_df.sample(1, replace=False).index
    initial_point = data_df.loc[initial_point_index]
    clusters_df = initial_point
    while k_clusters > 1:
        global max
        max = -math.inf
        max_index = initial_point_index
        for index, datapoint in data_df.iterrows():

            # Single data point
            x = datapoint['x']
            y = datapoint['y']
            z = datapoint['z']

            distance = euclidean_distance(initial_point['x'], initial_point['y'], initial_point['z'], x, y, z)
            if distance > max:
                max = distance
                max_index = index

        # print("Max Distance Points ", data_df.loc[initial_point_index], " and ",
        #       data_df.loc[max_index], " with distance ", max)

        initial_point = data_df.loc[max_index]
        clusters_df = clusters_df.append(initial_point)
        k_clusters -= 1
    print(clusters_df)
    return clusters_df


def k_means(k_clusters, data_df):
    # clusters = data_df.sample(k_clusters, replace=False)
    clusters = get_cluster_coordinates_k_mean_plus(k_clusters, data_df)
    data_df['cluster'] = 0
    converge = False
    iteration = 0
    while not converge:
        cost = 0
        # Assign Clusters
        # print("Clusters = ", clusters)
        prev_clusters = clusters
        for index, datapoint in data_df.iterrows():
            minimum = math.inf

            # Single data point
            x = datapoint['x']
            y = datapoint['y']
            z = datapoint['z']

            # Find the nearest Cluster
            cluster_id = 1
            for index1, cluster in clusters.iterrows():
                cx = cluster['x']
                cy = cluster['y']
                cz = cluster['z']
                distance = euclidean_distance(cx, cy, cz, x, y, z)
                cost = cost + distance
                if distance < minimum:
                    minimum = distance
                    data_df.at[index, 'cluster'] = cluster_id
                cluster_id += 1

        # Find the centroids and re-assign the cluster mean
        clusters = data_df.groupby('cluster').mean()
        print("Iteration= ", iteration, " Cost = ", cost)
        # print(data_df)
        # print(clusters)
        # print("=============================")
        # Iterate till cluster mean is constant
        if iteration != 0 and prev_clusters.equals(clusters):
            converge = True
        iteration += 1
    return data_df, clusters, iteration


if __name__ == '__main__':
    k = 3
    data = {'x': numpy.random.randint(low=10, high=100, size=1000),
            'y': numpy.random.randint(low=20, high=100, size=1000),
            'z': numpy.random.randint(low=30, high=100, size=1000)
            }
    df = pd.DataFrame(data)
    df, cluster_centers, itr = k_means(k, df)
    print("K Mean converged after ", itr, " iterations : ")
    print("============")
    print("Clustered Rows")
    print(df)
    print("Cluster Co-ordinates")
    print(cluster_centers)
