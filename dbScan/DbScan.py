def dbscan(data, eps, minPts):
    """
    Implements DBSCAN clustering algorithm.
    :param data:
    :param eps:
    :param minPts:
    :return:
    """
    # Mark all points as noise
    labels = [None] * len(data)
    # Assign cluster label to each point
    cluster_id = 0
    for point_id, point in enumerate(data):
        # Skip points that are already labeled
        if labels[point_id] is not None:
            continue
        # Find all points that are within eps distance
        neighbors = epsilonVoisinnage(data, point_id, eps)
        # If number of neighbors is less than minPts, mark point as noise
        if len(neighbors) < minPts:
            labels[point_id] = 0
        else:
            # If number of neighbors is greater than minPts, expand cluster
            cluster_id += 1
            labels[point_id] = cluster_id
            etendreCluster(data, labels, point_id, neighbors, cluster_id, eps, minPts)
    return labels


def epsilonVoisinnage(data, point_id, eps):
    """
    Finds all points within eps distance of point_id
    :param data:
    :param point_id:
    :param eps:
    :return:
    """
    neighbors = []
    for point_i, point in enumerate(data):
        if point_i == point_id:
            continue
        if distance_jaccard(data[point_id], point) <= eps:
            neighbors.append(point_i)
    return neighbors


def distance_jaccard(point1, point2):
    """
    Calculates Jaccard distance between two points
    :param point1:
    :param point2:
    :return:
    """
    return 1 - len(set(point1).intersection(set(point2))) / len(set(point1).union(set(point2)))


def etendreCluster(data, labels, point_d, neighbors, cluster_id, eps, minPts):
    """
    Expands cluster by finding all neighbors of each neighbor and applying DBSCAN
    :param data:
    :param labels:
    :param point_d:
    :param neighbors:
    :param cluster_id:
    :param eps:
    :param minPts:
    :return:
    """
    for neighbor in neighbors:
        # Skip points that are already labeled
        if labels[neighbor] is not None:
            continue
        # Find all points that are within eps distance
        neighbors_neighbors = epsilonVoisinnage(data, neighbor, eps)
        # If number of neighbors is greater than minPts, apply DBSCAN
        if len(neighbors_neighbors) >= minPts:
            # Add neighbors of neighbors to neighbors
            neighbors += neighbors_neighbors
        # Assign cluster label to point
        labels[neighbor] = cluster_id
