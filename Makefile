clean:
	rm -rf __pycache__

venv/bin/activate:
	pipenv install

run: venv/bin/activate app.py
	pipenv run python3 app.py
