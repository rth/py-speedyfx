# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from .run_suite import skip_if_sklearn_missing
from unittest import SkipTest


def test_external_imports():
    from ..externals import BaseEstimator, VectorizerMixin



@skip_if_sklearn_missing
def test_sklearn_compatibility():
    from sklearn.utils.estimator_checks import check_estimator
    from ..core import SpeedyFxVectorizer
    raise SkipTest
    check_estimator(SpeedyFxVectorizer)

