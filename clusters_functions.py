import numpy as np
import datetime
from distance_functions import get_distance
from math import sqrt




def get_distances_matrix(N, latitudes, longitudes):
    distances_matrix = np.zeros((N,N))
    for i in range(N):
        
        for j in range(N):
            distances_matrix[i,j] = get_distance(latitudes[i], longitudes[i], latitudes[j],longitudes[j])
    return distances_matrix

def get_time_diff_matrix(N, dates, times):
        
    datetime_string = [str(dates[i])[:10]+';'+str(times[i]) for i in range(N)]
    datetimes = np.array([datetime.datetime.strptime(datetime_string[i], "%Y-%m-%d;%H:%M:%S.%f") for i in range(N)])
    time_diff_matrix = np.zeros((N,N),dtype=datetime.timedelta)
    for i in range(N):
        for j in range(N):
            td = datetimes[j]-datetimes[i]
            time_diff_matrix[i,j] = td.total_seconds()/3600/24

    return datetimes, time_diff_matrix

def get_dst_matrix(N, distances_matrix, time_diff_matrix):
   
    C=1
    dst_matrix = np.zeros((N, N))
    for i in range(N):
        for j in range(N):
            dst_matrix[i,j] = sqrt(distances_matrix[i,j]**2+C**2*time_diff_matrix[i,j]**2)  
    return dst_matrix

def get_minimum_dst(dst_matrix):
        
    np.fill_diagonal(dst_matrix,float('inf')) # чтобы не выбирал сам себя ближайшим соседом
    minimum_dst = np.min(dst_matrix,1)
    return minimum_dst

def get_D(dst_matrix):
    
    minimum_dst = get_minimum_dst(dst_matrix)
    S1 = np.median(minimum_dst)
    print(S1)
    D = 9.4 * sqrt(S1) - 25.2
    print(D)
    return S1, D

def get_if_clustered_matrix(N, dst_matrix, D):
    if_clustered_matrix = np.empty((N,N))
    for i in range(N):
        for j in range(N):
            if_clustered_matrix[i,j] = True if dst_matrix[i,j] < D else False

    return if_clustered_matrix

def get_clusters(if_clustered_matrix):
    def find_cluster(id,ids_in_that_cluster,if_clustered_matrix):

        ids_in_that_cluster.append(id) # he himself is in his cluster
        
    
        neighbour_ids = set(np.where(if_clustered_matrix[id] == 1)[0])
        
        global not_watched
        not_watched.update(  set(neighbour_ids) -  set(ids_in_that_cluster) ) # в непросмотренные добавляем обнаруженных соседей - те которые уже посмотрели (ids in that cluster)
        not_watched.discard(id)
        
        for cur_id in not_watched & neighbour_ids: 
            if cur_id in not_watched: # костыль из-за смены not_watched. Доп проверка чтобы избежать повторного захода туда где уже были
                find_cluster(cur_id,ids_in_that_cluster,if_clustered_matrix)
        
        if len(not_watched)==0:
            return ids_in_that_cluster

    Clusters = []
    ids_not_clustered = list(range(0,len(if_clustered_matrix)))
    
    while len(ids_not_clustered)!=0:
        global not_watched
        not_watched =  set()
        cur_id_to_find_cluster_of = ids_not_clustered[0]
        
        cluster_ids = find_cluster(cur_id_to_find_cluster_of, [], if_clustered_matrix)
    

        for id in cluster_ids:
            ids_not_clustered.remove(id)
        Clusters.append(cluster_ids)
    return Clusters

# Список id событий, являющихся частью КАКОГО-ЛИБО роя, и список, не являющихся
def classify_ids_not_specific(Clusters):
    min_len_of_swarm = 6
    ids_of_swarms = []
    ids_not_swarms = []
    ids_of_swarms_exact = []
    for i in range(len(Clusters)):
        if len(Clusters[i]) >= min_len_of_swarm:
            ids_of_swarms.extend(Clusters[i])
            ids_of_swarms_exact.append(Clusters[i])
        else:
            ids_not_swarms.extend(Clusters[i])
    return ids_of_swarms_exact, ids_of_swarms, ids_not_swarms


def year_fraction(date):
    start = datetime.date(date.year, 1, 1).toordinal()
    year_length = datetime.date(date.year+1, 1, 1).toordinal() - start
    return date.year + float(date.toordinal() - start) / year_length


def calculate_lengths_frequencies(var_arr):
    lengths = list(map(len, var_arr)) 
    bins = np.arange(0, max(lengths)+1)+0.5

    return lengths,bins

