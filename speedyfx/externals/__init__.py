# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


try:
    from sklearn.feature_extraction.text import VectorizerMixin
    from sklearn.base import BaseEstimator
except ImportError:
    from .sklearn_base import BaseEstimator, VectorizerMixin
