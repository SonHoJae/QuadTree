import pickle
import datetime
from binary_direction import binary_direction
f = open('data/quad_tree.pckl', 'rb')
data = pickle.load(f)
f.close()

i = 0
geo_index = {}
for k, v in data.items():
    geo_index.update(
        **dict.fromkeys(list(v),k)
    )
    i += 1

try:
    right_most = 82.483333
    left_most = -54.933333
    top_most = 180.0
    down_most = -179.9833333
    start = datetime.datetime.now()
    print('start time -> ' + str(start))
    for i in range(100002):
        quad_seq = binary_direction(left_most,right_most,down_most,top_most,42.466667,1.500000, depth=30)  # Region 6
    print(geo_index[quad_seq])
    finish = datetime.datetime.now()
    print('finish time -> ' + str(finish))
    print('taking time -> ' +str(finish - start))
except KeyError:
    print('Key Error !')
except Exception as e:
    print('Something happened')
    print(e)

