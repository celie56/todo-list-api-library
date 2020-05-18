"""Ensure our interface will produce valid data."""
import interface


def test_interface():
    list_name = 'interface_test'
    interface.create_list(list_name)
    _lists = interface.get_lists()

    task_name = 'task_1'
    interface.create_task(list_name, task_name)
    _list = interface.get_list(list_name)
    assert task_name in _list['list']['items']
