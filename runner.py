"""Debug file to ease testing."""
from click.testing import CliRunner
import cli
import interface


def run():
    runner = CliRunner()
    result = runner.invoke(cli.get_lists, [])

    _lists = interface.get_lists()
    list_name = 'interface_test'
    interface.create_list(list_name)
    _lists = interface.get_lists()

    my_list = interface.get_list(list_name)
    items = my_list['items']
    open_items = [
        item['name'] for item in items if item['finished_at'] is None
    ]

    task_name = 'task_1'
    if task_name not in open_items:
        interface.create_task(list_name, task_name)

    interface.complete_task(list_name, task_name)
    _list = interface.get_list(list_name)


if __name__ == '__main__':
    run()