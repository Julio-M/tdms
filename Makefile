setup:
	# Create virtual environment and activate it
	python3 -m venv venv &&\
		source venv/bin/activate
	

	# Install dependencies
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	# Run setup
	make setup

	# Run the tests
	pytest

coverage:
	# Run the setup step above first
	make setup

	# Run the coverage
	pytest --cov=tdms
