sdist:
	make stamp; make release_notes; python setup.py sdist --formats=zip; 

test: 
	py.test -s speedyfx
