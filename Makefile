build:
	python3 -m build
install: build
	pip install dist/*.whl

test:
	pytest