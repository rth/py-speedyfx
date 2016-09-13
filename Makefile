sdist:
	make stamp; make release_notes; python setup.py sdist --formats=zip; 

test2: 
	python2 /usr/bin/nosetests -s speedyfx --with-coverage --cover-package=speedyfx
test3: 
	python3 /usr/bin/nosetests -s speedyfx --with-coverage --cover-package=speedyfx
