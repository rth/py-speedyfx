# py-speedyfx

py-SpeedyFx: Fast Text Feature Extraction for Classification and Indexing (Python implementation)

[![Build Status](https://travis-ci.org/rth/py-speedyfx.svg?branch=master)](https://travis-ci.org/rth/py-speedyfx) 
[![Build status](https://ci.appveyor.com/api/projects/status/6qdvqc475g5pyflm/branch/master?svg=true)](https://ci.appveyor.com/project/rth/py-speedyfx/branch/master)

The goal of this package is to provide an implementation of the SpeedyFx algorithm with a scikit-learn compatible API, so it can be used as a drop in replacement for scikit-learn's `HashingVectorizer`.


**Note:** this package is in early development phase and should not be used in production. The public API can change in a non backward compatible manner without warning.


## Installation notes

 This package requires Python 2.7 or 3.2-3.5 with the following modules installed: `numpy>=1.9`, `scipy`, `cython`, `setuptools`, `six` (and optionally `pytest`, `scikit-learn` and `nose` [for the running the test suite only] ).

 To install this module run,
    
    pip install git+https://github.com/rth/py-speedyfx.git

## References
  
  * ["Extremely fast text feature extraction for classification and indexing"](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.170.8670&rep=rep1&type=pdf) by G Forman, E Kirshenbaum (2008)
  * This package also adapted work on SpeedyFx in other languages, including the [Perl implementation](https://github.com/creaktive/Text-SpeedyFx) and the [C implementation](https://github.com/creaktive/speedyfx).

## Licence

This package is release under the [revised BSD Licence](./LICENSE.txt).
