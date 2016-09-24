# -*- coding: utf-8 -*-
# The API was strongly adapted from scikit-learn's HashingVectorizer
# https://github.com/scikit-learn/scikit-learn/blob/51a765a/sklearn/feature_extraction/text.py#L287
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys
import numpy as np
from .externals import BaseEstimator, VectorizerMixin


class SpeedyFxVectorizer(BaseEstimator, VectorizerMixin):
    """Convert a collection of text documents to a matrix of token occurrences

    Parameters
    ----------
    input : string {'filename', 'file', 'content'}
        If 'filename', the sequence passed as an argument to fit is
        expected to be a list of filenames that need reading to fetch
        the raw content to analyze.
        If 'file', the sequence items must have a 'read' method (file-like
        object) that is called to fetch the bytes in memory.
        Otherwise the input is expected to be the sequence strings or
        bytes items are expected to be analyzed directly.
    encoding : string, default='utf-8'
        If bytes or files are given to analyze, this encoding is used to
        decode.
    decode_error : {'strict', 'ignore', 'replace'}
        Instruction on what to do if a byte sequence is given to analyze that
        contains characters not of the given `encoding`. By default, it is
        'strict', meaning that a UnicodeDecodeError will be raised. Other
        values are 'ignore' and 'replace'.
    strip_accents : {'ascii', 'unicode', None}
        Remove accents during the preprocessing step.
        'ascii' is a fast method that only works on characters that have
        an direct ASCII mapping.
        'unicode' is a slightly slower method that works on any characters.
        None (default) does nothing.
    analyzer : string, {'word', 'char', 'char_wb'} or callable
        Whether the feature should be made of word or character n-grams.
        Option 'char_wb' creates character n-grams only from text inside
        word boundaries.
        If a callable is passed it is used to extract the sequence of features
        out of the raw, unprocessed input.
    preprocessor : callable or None (default)
        Override the preprocessing (string transformation) stage while
        preserving the tokenizing and n-grams generation steps.
    tokenizer : callable or None (default)
        Override the string tokenization step while preserving the
        preprocessing and n-grams generation steps.
        Only applies if ``analyzer == 'word'``.
    ngram_range : tuple (min_n, max_n), default=(1, 1)
        The lower and upper boundary of the range of n-values for different
        n-grams to be extracted. All values of n such that min_n <= n <= max_n
        will be used.
    stop_words : string {'english'}, list, or None (default)
        If 'english', a built-in stop word list for English is used.
        If a list, that list is assumed to contain stop words, all of which
        will be removed from the resulting tokens.
        Only applies if ``analyzer == 'word'``.
    lowercase : boolean, default=True
        Convert all characters to lowercase before tokenizing.
    token_pattern : string
        Regular expression denoting what constitutes a "token", only used
        if ``analyzer == 'word'``. The default regexp selects tokens of 2
        or more alphanumeric characters (punctuation is completely ignored
        and always treated as a token separator).
    n_features : integer, default=(2 ** 20)
        The number of features (columns) in the output matrices. Small numbers
        of features are likely to cause hash collisions, but large numbers
        will cause larger coefficient dimensions in linear learners.
    norm : 'l1', 'l2' or None, optional
        Norm used to normalize term vectors. None for no normalization.
    binary: boolean, default=False.
        If True, all non zero counts are set to 1. This is useful for discrete
        probabilistic models that model binary events rather than integer
        counts.
    dtype: type, optional
        Type of the matrix returned by fit_transform() or transform().
    non_negative : boolean, default=False
        Whether output matrices should contain non-negative values only;
        effectively calls abs on the matrix prior to returning it.
        When True, output values can be interpreted as frequencies.
        When False, output values will have expected value zero.
    See also
    --------
    CountVectorizer, TfidfVectorizer
    """
    length = 256
    code_table = [0] * length

    def __init__(self, input='content', encoding='utf-8',
                 decode_error='strict', strip_accents=None,
                 lowercase=True, preprocessor=None, tokenizer=None,
                 stop_words=None, token_pattern=r"(?u)\b\w\w+\b",
                 ngram_range=(1, 1), analyzer='word', n_features=(2 ** 20),
                 binary=False, norm='l2', non_negative=False,
                 dtype=np.float64):
        self.input = input
        self.encoding = encoding
        self.decode_error = decode_error
        self.strip_accents = strip_accents
        self.preprocessor = preprocessor
        self.tokenizer = tokenizer
        self.analyzer = analyzer
        self.lowercase = lowercase
        self.token_pattern = token_pattern
        self.stop_words = stop_words
        self.n_features = n_features
        self.ngram_range = ngram_range
        self.binary = binary
        self.norm = norm
        self.non_negative = non_negative
        self.dtype = dtype


    def partial_fit(self, X, y=None):
        """Does nothing: this transformer is stateless.
        This method is just there to mark the fact that this transformer
        can work in a streaming setup.
        """
        return self

    def fit(self, X, y=None):
        """Does nothing: this transformer is stateless."""
        return self

    def transform(self, X, y=None):
        """Transform a sequence of documents to a document-term matrix.
        Parameters
        ----------
        X : iterable over raw text documents, length = n_samples
            Samples. Each sample must be a text document (either bytes or
            unicode strings, file name or file object depending on the
            constructor argument) which will be tokenized and hashed.
        y : (ignored)
        Returns
        -------
        X : scipy.sparse matrix, shape = (n_samples, self.n_features)
            Document-term matrix.
        """
        #analyzer = self.build_analyzer()
        #X = self._get_hasher().transform(analyzer(doc) for doc in X)
        #if self.binary:
        #    X.data.fill(1)
        #if self.norm is not None:
        #    X = normalize(X, norm=self.norm, copy=False)
        #return X
        result = {}
        wordhash = 0

        for c in X:
            code = self.code_table[ord(c) % self.length]
            if (code):
                wordhash = (wordhash >> 1) + code
            elif (wordhash):
                if (wordhash in result):
                    result[wordhash] += 1
                else:
                    result[wordhash] = 1
                wordhash = 0

        if (wordhash):
            if (wordhash in result):
                result[wordhash] += 1
            else:
                result[wordhash] = 1

        return result

    # Alias transform to fit_transform for convenience
    fit_transform = transform


    def _init_hashing_table(self, seed=1):
        fold_table = [0] * self.length
        rand_table = [seed] + [0] * (self.length - 1)

        for i in range(1, self.length):
            #j = unichr(i)
            j = chr(i)
            if (j.isalnum()):
                fold_table[i] = ord(j.lower())
            else:
                fold_table[i] = 0
            rand_table[i] = rand_table[i - 1]
            rand_table[i] *= 0x10a860c1
            rand_table[i] &= 0xffffffff
            rand_table[i] %= 0xfffffffb

        for i in range(self.length):
            if (fold_table[i]):
                self.code_table[i] = rand_table[fold_table[i]]


    def hash_min(self, string):
        minhash = sys.maxint
        wordhash = 0

        for c in string:
            code = self.code_table[ord(c) % self.length]
            if (code):
                wordhash = (wordhash >> 1) + code
            elif (wordhash):
                minhash = min(minhash, wordhash)
                wordhash = 0

        if (wordhash):
            minhash = min(minhash, wordhash)

        return minhash

#sfx = SpeedyFx()
#str = 'To be or not to be?'
#print sfx.hash(str)
#print sfx.hash_min(str)
