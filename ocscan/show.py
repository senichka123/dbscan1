import numpy as np

def NumberOfClusters(labels):
    """Show results of clustering for DBSCAN"""
    n_clusters_ = len(set(labels) - {-1})
    print('Estimated number of clusters: {0}'.format(n_clusters_))
    return n_clusters_

									
									 

