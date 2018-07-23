# Data set is from https://www.kaggle.com/max-mind/world-cities-database#worldcitiespop.csv
import pickle

import pandas as pd
from binary_direction import binary_direction
from collections import defaultdict

df = pd.read_csv('data/worldcitiespop.csv')
print(df.head())
df = df[['Region','Latitude','Longitude']]

right_most = max(df['Latitude'])
left_most = min(df['Latitude'])
up_most = max(df['Longitude'])
down_most = min(df['Longitude'])

print(right_most)
print(left_most)
print(up_most)
print(down_most)
print(df.describe())

quad_tree = defaultdict(set)

for index, row in df.iterrows():
    quad_loc =binary_direction(left_most, right_most, down_most, up_most, row['Latitude'], row['Longitude'], depth=30)
    quad_tree[row['Region']].add(quad_loc)
print(quad_tree)

f = open('quad_tree_25.pckl', 'wb')
pickle.dump(quad_tree, f)
f.close()
