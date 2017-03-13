# Code to generate data files from old files on zoltans account
import urllib
testfile = urllib.URLopener()
fname, _ = testfile.retrieve("http://www.gatsby.ucl.ac.uk/~szabo/teaching/adaptive_modelling/TextData.mat", "TextData.mat")

import os
import scipy.io as sio
import numpy as np
mat_data = sio.loadmat(fname)

data = {}
data['Docs'] = []
for d in mat_data['Docs'][0]:
    data['Docs'].append(str(d[0]).strip())
data['Docs'] = np.array(data['Docs'])

docs_sport = data['Docs'][np.arange(400)]
docs_aviation = data['Docs'][np.arange(400) + 400]

with open("docs_sport.txt", 'w') as f:
    for doc in docs_sport:
        f.write(doc + os.linesep)

with open("docs_aviation.txt", 'w') as f:
    for doc in docs_aviation:
        f.write(doc + os.linesep)

