import pickle
import datetime
import quad_tree
import pandas as pd
#quad_tree.data_preprocess()

depth=30

f = open('data/quad_tree_'+str(depth)+'.pckl', 'rb')
data = pickle.load(f)
f.close()

df = pd.read_csv('data/worldcitiespop.csv')
df = df[['Region', 'Latitude', 'Longitude']]

try:
    _iter = df.iterrows()
    start = datetime.datetime.now()
    print('start time -> ' + str(start))
    for index, row in _iter:
        quad_seq = quad_tree.binary_direction(row['Latitude'],row['Longitude'], depth=depth)
        if index == 100002:
            break
    finish = datetime.datetime.now()
    print('finish time -> ' + str(finish))
    print('taking time -> ' +str(finish - start))

except KeyError:
    print('Key Error !')
except Exception as e:
    print('Something happened')
    print(e)

