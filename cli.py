"""CLI commands.

To see help, run:
    $ python cli.py
"""
import click
import interface


@click.group()
def cli():
    pass


# ----------------------------------------------------------------------------
# Lists
# ----------------------------------------------------------------------------


@cli.command()
def get_lists():
    lists = interface.get_lists()
    lists = [obj['name'] for obj in lists['lists']]
    click.echo(lists)


@cli.command()
@click.argument('list_name')
def get_list(list_name):
    my_list = interface.get_list(list_name=list_name)
    items = my_list['items']
    open_items = [
        item['name'] for item in items if item['finished_at'] is None
    ]
    finished_items = [
        item['name'] for item in items if item['finished_at'] is not None
    ]
    click.echo(f'list_name: my_list["name"]')
    click.echo(f'open items: {open_items}')
    click.echo(f'finished items: {finished_items}')


@cli.command()
@click.argument('list_name')
def create_list(list_name):
    interface.create_list(list_name=list_name)


@cli.command()
@click.argument('list_name')
def delete_list(list_name):
    interface.delete_list(list_name=list_name)


# ----------------------------------------------------------------------------
# Tasks
# ----------------------------------------------------------------------------


@cli.command()
@click.argument('list_name')
@click.argument('task_name')
def create_task(list_name, task_name):
    interface.create_task(list_name=list_name, task_name=task_name)


@cli.command()
@click.argument('list_name')
@click.argument('task_name')
def complete_task(list_name, task_name):
    interface.complete_task(list_name=list_name, task_name=task_name)


if __name__ == '__main__':
    cli()