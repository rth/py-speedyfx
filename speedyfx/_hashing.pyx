# -*- coding: utf-8 -*-
# cython: boundscheck=False
# cython: cdivision=True
# cython: wraparound=False
## cython: profile=True



import numpy as np
cimport numpy as np

cimport cython


cpdef _transform_single_ascii(doc, long [:] code_table, int length):
    cdef long wordhash = 0
    cdef long code
    cdef dict result = {}
    cdef int idx
    for c in doc:
        idx = ord(c) % length
        code = code_table[idx]
        if code:
            wordhash = (wordhash >> 1) + code
        elif wordhash:
            if wordhash in result:
                result[wordhash] += 1
            else:
                result[wordhash] = 1
            wordhash = 0


    if wordhash:
        if wordhash in result:
            result[wordhash] += 1
        else:
            result[wordhash] = 1
    return result


cpdef _speedy_transform(list X,  code_table, int length):
    j_indices = []
    indptr = []
    values = []
    indptr.append(0)
    for doc_dec in X:
        result = _transform_single_ascii(doc_dec, code_table, length)

        j_indices.extend(result.keys())
        values.extend(result.values())
        indptr.append(len(j_indices))

    return j_indices, indptr, values


#cpdef _transform_single_unicode(doc, long [:] code_table, int length):
#    cdef dict result = {}
#    cdef long wordhash = 0
#    for c in doc:
#        code = code_table[ord(c) % length]
#        if code:
#            wordhash = (wordhash >> 1) + code
#        elif wordhash:
#            if wordhash in result:
#                result[wordhash] += 1
#            else:
#                result[wordhash] = 1
#            wordhash = 0
#
#
#    if wordhash:
#        if wordhash in result:
#            result[wordhash] += 1
#        else:
#            result[wordhash] = 1
#    return result

