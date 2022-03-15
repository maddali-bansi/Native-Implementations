Input :  k-number of clusters and D-set of data objects
Output : Set of K-Clusters

Algorithm 

1.Randomly choose 'k' objects from D as initial cluster centers
2.repeat:
    2.1 re-assign each object to cluster to which the object is most similar(nearest)
    2.2 Update the cluster means for each cluster
  untill no change
