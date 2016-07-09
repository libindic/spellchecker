travis:
	python setup.py test --coverage \
		--coverage-package-name=libindic.spellchecker
	flake8 --max-complexity 10 libindic/spellchecker
clean:
	find . -iname "*.pyc" -exec rm -vf {} \;
	find . -iname "__pycache__" -delete
	sudo rm -rf build dist *egg* .tox .coverage .testrepository
