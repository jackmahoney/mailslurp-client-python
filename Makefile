setup:
	python3 -m pip install --user --upgrade setuptools wheel
	python3 -m pip install --user --upgrade twine

dist: setup
	python3 setup.py sdist bdist_wheel

publish: dist
	python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*

install:
	python3 setup.py install --prefix ~/.local



