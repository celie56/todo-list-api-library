"""Methods that connect to list service."""
import json
import requests
from requests.auth import HTTPBasicAuth
from typing import Callable


class RequestMaker:
    # TODO: you must fill in the below to make this work
    url = 'YOUR_URL'
    auth = None
    user = 'YOUR_USER'
    pswd = 'YOUR_PASSWORD'

    @classmethod
    def _acquire_auth(cls):
        full_url = f'{cls.url}/authenticate'
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = requests.post(
            full_url,
            headers=headers,
            auth=HTTPBasicAuth(cls.user, cls.pswd),
        )
        cls.auth = response.json()['token']

    @classmethod
    def _request_details(cls, endpoint: str) -> dict:
        if not cls.auth:
            cls._acquire_auth()
        full_url = f'{cls.url}/{endpoint}'
        headers = {'Authorization': f'Token token="{cls.auth}"'}
        return dict(url=full_url, headers=headers)

    @classmethod
    def get(cls, endpoint: str) -> dict:
        response = requests.get(**cls._request_details(endpoint))
        return response.json()

    @classmethod
    def post(cls, endpoint: str, data: dict) -> dict:
        response = requests.post(json=data, **cls._request_details(endpoint))
        return response.json() if response.content else None

    @classmethod
    def delete(cls, endpoint: str) -> dict:
        response = requests.delete(**cls._request_details(endpoint))
        return response.json() if response.content else None

    @classmethod
    def put(cls, endpoint: str) -> dict:
        response = requests.put(**cls._request_details(endpoint))
        return response.json() if response.content else None


# ----------------------------------------------------------------------------
# Lists
# ----------------------------------------------------------------------------


def get_lists():
    """Retrieves all lists."""
    return RequestMaker.get('lists')


def _get_list_id(list_name: str):
    all_lists = get_lists()['lists']
    name_to_id = {obj['name']: obj['id'] for obj in all_lists}
    return name_to_id[list_name]


def _get_list(list_id: int):
    """Retrieve the list information by id."""
    return RequestMaker.get(f'lists/{list_id}')


def get_list(list_name: str):
    """Retrieve the list information by name."""
    list_id = _get_list_id(list_name)
    return _get_list(list_id)


def create_list(list_name: str):
    """Creates a list."""
    data = dict(list=dict(name=list_name))
    return RequestMaker.post('lists', data)


def delete_list(list_name: str):
    list_id = _get_list_id(list_name)
    return RequestMaker.delete(f'lists/{list_id}')


# ----------------------------------------------------------------------------
# Tasks
# ----------------------------------------------------------------------------


def _get_task_id(list_id, task_name):
    all_tasks = _get_list(list_id)['items']
    name_to_id = {obj['name']: obj['id'] for obj in all_tasks}
    return name_to_id[task_name]


def get_task(list_name: str, task_name: str):
    list_id = _get_list_id(list_name)
    task_id = _get_task_id(list_id, task_name)
    endpoint = f'lists/{list_id}/items/{task_id}'
    return RequestMaker.get(endpoint)


def create_task(list_name: str, task_name: str):
    data = dict(item=dict(name=task_name))
    list_id = _get_list_id(list_name)
    endpoint = f'lists/{list_id}/items'
    return RequestMaker.post(endpoint, data)


def complete_task(list_name: str, task_name: str):
    list_id = _get_list_id(list_name)
    task_id = _get_task_id(list_id, task_name)
    endpoint = f'lists/{list_id}/items/{task_id}/finish'
    return RequestMaker.put(endpoint)
