# -*- coding: utf-8 -*-
# cython: boundscheck=False
# cython: cdivision=True
# cython: wraparound=False
## cython: profile=True



import numpy as np
cimport numpy as np

cimport cython

cdef extern from "lib/speedyfx.h":
    cdef unsigned char *speedyfx_fv(const unsigned char *s, unsigned int *code_table,
                                        unsigned int n, unsigned int length);
    cdef int speedyfx_free(unsigned char * fv);


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


cpdef _speedy_transform(list X, unsigned int [:] code_table, int length):
    cdef size_t fv_length = 1024 * 1024;
    cdef size_t idx;
    cdef unsigned int n = 256

    j_indices = []
    indptr = []
    values = []
    indptr.append(0)
    cdef unsigned char *doc
    cdef str doc_enc
    cdef unsigned char* fv
    for doc_enc in X:
        doc_tmp = str.encode(doc_enc)
        doc = doc_tmp
        #result = _transform_single_ascii(doc_dec, code_table, length)
        #print(type(doc_dec))
        

        fv = speedyfx_fv(&doc[0], &code_table[0], fv_length, n)

        #for idx in range(fv_length//8):
        #    if fv[idx] != 0:
        #        #print(idx, fv[idx])


        #j_indices.extend(result.keys())
        #values.extend(result.values())
        #indptr.append(len(j_indices))
        speedyfx_free(fv)

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

# http://semashare.net/ngrams/linux/index.htm
# https://en.wikipedia.org/wiki/Suffix_array
