# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from .run_suite import skip_if_sklearn_missing
from unittest import SkipTest
from ..core import SpeedyFxVectorizer
from numpy.testing import assert_allclose


def test_external_imports():
    from ..externals import BaseEstimator, VectorizerMixin



@skip_if_sklearn_missing
def test_sklearn_compatibility():
    from sklearn.utils.estimator_checks import check_estimator
    from sklearn.feature_extraction.text import HashingVectorizer
    raise SkipTest # the HashingVecotorizer itself fails this test
    #check_estimator(SpeedyFxVectorizer)
    #check_estimator(HashingVectorizer)



def test_speedy_tiny():
    """Adapted from
    https://github.com/creaktive/Text-SpeedyFx/blob/master/t/10-tiny.t"""

    doc = ['Hello, World!']

    vect = SpeedyFxVectorizer(norm=None, encoding='latin1')
    res = vect.transform(doc)
    for idx in [828691033, 2983498205]:
        assert res[0, idx] == 1.0


def test_speedy_tiny_stacked():
    """Testing multidocument collection"""
    doc = ['Hello, World!']*2

    vect = SpeedyFxVectorizer(norm=None, encoding='latin1')
    res = vect.transform(doc)
    for ridx in range(2):
        for idx in [828691033, 2983498205]:
            assert res[ridx, idx] == 1.0

    assert (res[0]!=res[1]).nnz == 0


def test_speedy_small():
    """Adapted from
    https://github.com/creaktive/Text-SpeedyFx/blob/master/t/20-small.t"""

    doc = ['The quick brown fox jumps over the lazy dog',
           'Pójdźże, kiń tę chmurność w głąb flaszy!',
           'Victor jagt zwölf Boxkämpfer quer über den großen Sylter Deich',
           'Любя, съешь щипцы, — вздохнёт мэр, — кайф жгуч',
           'أبجد هوَّز حُطّي كلَمُن سَعْفَص قُرِشَت ثَخَدٌ ضَظَغ']

    vect = SpeedyFxVectorizer(norm=None, encoding='latin1')
    res = vect.transform(doc)
    #print(res)
