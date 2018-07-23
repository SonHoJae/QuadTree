# Data set is from https://www.kaggle.com/max-mind/world-cities-database#worldcitiespop.csv
import pickle

import pandas as pd
from collections import defaultdict

depth = 25
def binary_direction(lat, long, left=-54.933333, right=82.483333, down=-179.9833333, up=180.0,  depth=1):
    location = ''
    for idx in range(depth):
        if idx % 2 == 0:
            mid = (left + right)/ 2
            if lat > mid:
                location +='1'
                left = mid
            else:
                location += '0'
                right = mid
        else:
            mid = (down + up) / 2
            if long > mid:
                location += '1'
                down = mid
            else:
                location += '0'
                up = mid
    return location

def data_preprocess():
    df = pd.read_csv('data/worldcitiespop.csv')
    df = df[['Region','Latitude','Longitude']]

    right_most = max(df['Latitude'])
    left_most = min(df['Latitude'])
    up_most = max(df['Longitude'])
    down_most = min(df['Longitude'])

    quad_tree = defaultdict(set)

    for index, row in df.iterrows():
        quad_loc =binary_direction(row['Latitude'], row['Longitude'], left_most, right_most, down_most, up_most,
                                   depth=depth)
        quad_tree[row['Region']].add(quad_loc)

    geo_index = {}
    for k, v in quad_tree.items():
        geo_index.update(
            **dict.fromkeys(list(v),k)
        )

    f = open('data/quad_tree_'+str(depth)+'.pckl', 'wb')
    pickle.dump(geo_index, f)
    f.close()
