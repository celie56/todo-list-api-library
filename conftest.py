"""Configuration for tests."""
import pytest
import fake_list_service
import interface
from unittest import mock

# To run tests, you will need to start the fake list service
# export FLASK_APP=fake_list_service.py
# export FLASK_ENV=development
# python -m flask run
interface.RequestMaker.url = 'http://127.0.0.1:5000'
