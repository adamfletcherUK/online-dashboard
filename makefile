# Usage:
# make        # compile all binary
# make clean  # remove ALL binaries and objects

test:
	python src/tests/startup_test.py
	python src/tests/test_streamlit.py

requirements:
#	python -m  pipreqs.pipreqs . --force
	pip freeze > requirements.txt


