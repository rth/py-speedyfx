# -*- coding: utf-8 -*-

import os
import sys
import pytest

_base_dir, _ = os.path.split(__file__)

def run(coverage=True):
    import nose
    argv=['', '-s', '--where={}'.format(_base_dir), '--verbosity=2']
    if coverage:
        argv += ['--with-coverage', '--cover-package=koondalai']
    result = nose.run(argv=argv)
    status = int(not result)
    return status

def run_cli(coverage=False):
    status = run(coverage=coverage)
    print('Exit status: {}'.format(status))
    sys.exit(status)



def _sklearn_installed():
    try:
        import sklearn
        return 1
    except ImportError:
        return 0

skip_if_sklearn_missing = pytest.mark.skipif(
                        not  _sklearn_installed,
                        reason="scikit-learn not instaled")



if __name__ == '__main__':
    run_cli()


