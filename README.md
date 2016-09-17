# py-speedyfx

SpeedyFx: Fast Text Feature Extraction for Classification and Indexing (Python implementation)

[![Build Status](https://travis-ci.org/rth/py-speedyfx.svg?branch=master)](https://travis-ci.org/rth/py-speedyfx)


## Installation notes

 This package requires Python 2.7 or 3.2-3.5 with the following modules installed: `numpy>=1.9`, `scipy`, `six`, `setuptools`, `nose`.

 To install this module run,
    
    python setup.py git+https://github.com/rth/py-speedyfx.git


## Unit tests

 The unit tests suite can be run from the command line,

    $ nosetests -s speedyfx/tests/

or from within Python with,
 
    import speedyfx.tests; speedyfx.tests.run()
    
## References
  
  * ["Extremely fast text feature extraction for classification and indexing"](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.170.8670&rep=rep1&type=pdf) by G Forman, E Kirshenbaum (2008)
