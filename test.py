import pickle
import datetime
import quad_tree

#quad_tree.data_preprocess()

f = open('data/quad_tree_30.pckl', 'rb')
data = pickle.load(f)
f.close()

try:
    start = datetime.datetime.now()
    print('start time -> ' + str(start))
    for i in range(100002):
        quad_seq = quad_tree.binary_direction(42.466667, 1.500000, depth=30)  # Region 6
    print(data[quad_seq])
    finish = datetime.datetime.now()
    print('finish time -> ' + str(finish))
    print('taking time -> ' +str(finish - start))
except KeyError:
    print('Key Error !')
except Exception as e:
    print('Something happened')
    print(e)

