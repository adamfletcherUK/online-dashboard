# Usage:
# make        # compile all binary
# make clean  # remove ALL binaries and objects

all: say_hello say_goodbye

say_hello:
	@echo "Hello World"

say_goodbye:
	@echo "Goodbye"

test:
	python src/tests/startup_test.py

requirements:
	python -m  pipreqs.pipreqs . --force


