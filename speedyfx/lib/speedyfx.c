#include <sys/mman.h>
#include <sys/stat.h>
#include <ctype.h>
#include <err.h>
#include <fcntl.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/*
 * SpeedyFx algorithm
 * ==================
 *
 * Tokenize/hash large amount of strings efficiently.
 * Original Java implementation: http://www.hpl.hp.com/techreports/2008/HPL-2008-91R1.pdf
 * Ported to C by Stanislaw Pusep (https://github.com/creaktive)
 * Compile with:
 *      clang -lm -O3 -o speedyfx speedyfx.c
 * or:
 *      gcc -lm -O3 -o speedyfx speedyfx.c
 * Then use as:
 *      ./speedyfx enwik9 > fv.bin
 * To generate 128KB feature vector for enwik9 text file.
 *
 * Benchmark
 * =========
 *
 * Test data: https://cs.fit.edu/~mmahoney/compression/enwik9.bz2
 * Hardware: Intel(R) Xeon(R) CPU E5620 @ 2.40GHz
 * Average feature vector build speed: 213.83 MB/s
 */

#define SetBit(a, b) (((unsigned char *) a)[(b) >> 3] |= (1 << ((b) & 7)))

unsigned char *speedyfx_fv(const unsigned char *s, unsigned int *code_table,
                                        unsigned int n, unsigned int length) {
    unsigned int code, c;
    unsigned int wordhash = 0;
    unsigned char *fv;

    fv = calloc(ceil((float) n / 8.0), sizeof(unsigned char));

    while (*s) {
        c = *s++;
        if ((code = code_table[c % length]) != 0)
            wordhash = (wordhash >> 1) + code;
        else if (wordhash) {
            SetBit(fv, wordhash % n);
            wordhash = 0;
        }
    }

    if (wordhash)
        SetBit(fv, wordhash % n);

    return fv;
}


int speedyfx_free(unsigned char * fv) {
    free(fv);
    return 0;
}
    
