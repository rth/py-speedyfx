# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals


from time import time
from imp import reload

from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import HashingVectorizer
import speedyfx
reload(speedyfx)



def size_mb(docs):
    return sum(len(s.encode('utf-8')) for s in docs) / 1e6

categories = ['sci.space',
         'rec.motorcycles',
         'rec.sport.baseball',
         'rec.sport.hockey',
         'sci.crypt',
         'sci.electronics',
        ]

data = fetch_20newsgroups(categories=categories)

data_size_mb = size_mb(data.data)

print('\nPerformance benchmark on 20 newsgroups dataset ({:.2} MB)\n'.format(data_size_mb))
for vect in [HashingVectorizer, speedyfx.SpeedyFxVectorizer]:
    hv = vect(norm=None, encoding='latin1')
    t0 = time()
    X = hv.transform(data.data)
    dt = time() - t0
    print(' * {:20}: {:>9.2f} MB/s'.format(type(hv).__name__, data_size_mb/dt))


