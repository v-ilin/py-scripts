import scipy.io
import numpy as np

data = scipy.io.loadmat("cars_meta.mat")

for i in data:
    print(i)
    if '__' not in i and 'readme' not in i:
        np.savetxt(("output/"+i+".csv"),
                   data[i][0], fmt='%s', delimiter='\r\n')
