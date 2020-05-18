export FLASK_APP := fake_list_service.py
export FLASK_ENV := development

mock-server:
	python -m flask run